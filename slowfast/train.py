import numpy as np
from tqdm.auto import tqdm
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score

from src.data import VideosDataset
from src.utils import FramesGenerator
from src.model import get_slowfast_model
from config.train_config import (
    train_dataset_path,
    test_dataset_path,
    classes_num,
    device,
    basemodel,
    pretrained,
    save_path,
    epochs_num,
    lr,
    weight_decay,
    transform,
)


def train_epoch(model, dataset, optimizer, loss):
    indexes = np.arange(len(dataset))
    np.random.shuffle(indexes)

    train_loss = 0
    for index in tqdm(indexes):
        video_path, label = dataset[index]
        frames_generator = FramesGenerator(
            video_path=video_path,
            transform=transform,
        )

        video_loss = 0
        for slow_pathway, fast_pathway in frames_generator:
            input = [
                slow_pathway.to(device).unsqueeze(0),
                fast_pathway.to(device).unsqueeze(0),
            ]

            output = model(input)
            target = torch.zeros(1, device=device, dtype=int) + label

            loss_value = loss(output, target)

            optimizer.zero_grad()
            loss_value.backward()
            optimizer.step()

            video_loss += loss_value.item()
        video_loss /= len(frames_generator)
    train_loss /= len(dataset)

    return train_loss


def test(model, dataset):
    post_act = nn.Softmax(dim=1).to("cuda")

    true = []
    pred = []
    for index in tqdm(range(len(dataset))):
        video_path, label = test_dataset[index]
        frames_generator = FramesGenerator(
            video_path=video_path,
            transform=transform,
        )

        preds = torch.zeros(classes_num).to(device)
        for slow_pathway, fast_pathway in frames_generator:
            input = [
                slow_pathway.to(device).unsqueeze(0),
                fast_pathway.to(device).unsqueeze(0),
            ]

            output = post_act(model(input))
            preds += output.reshape(-1)

            del slow_pathway
            del fast_pathway

        true.append(label)
        pred.append(torch.argmax(preds).item())

    return accuracy_score(true, pred)

if __name__ == "__main__":
    model = get_slowfast_model(basemodel, pretrained, classes_num).to(device)

    train_dataset = VideosDataset(train_dataset_path)
    test_dataset = VideosDataset(test_dataset_path)

    loss = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=lr,
        weight_decay=weight_decay,
    )

    for epoch in range(epochs_num):
        train_loss = train_epoch(model, train_dataset, optimizer, loss)
        test_accuracy = test(model, test_dataset)
        print(f"Epoch: {epoch+1}/{epochs_num}, Train Loss: {train_loss:.5f}, Test Accuracy: {test_accuracy:.3f}")

    torch.save(model.state_dict(), save_path)
