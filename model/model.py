import torchvision
import torch
import torch.nn as nn
from pytorchvideo.models.head import ResNetBasicHead

from utils import FramesGenerator


device = "cpu"

class2label = {
    0: "колесо",
    1: "ловить",
    2: "хлопать",
    3: "взбираться",
    4: "нырять",
    5: "обнажение меча",
    6: "дрибблинг",
    7: "фехтование",
    8: "сальто",
    9: "гольф",
    10: "стоять на руках",
    11: "ударить",
    12: "прыгать",
    13: "взять",
    14: "наливать",
    15: "подтягиваться",
    16: "толкать",
    17: "отжиматься",
    18: "бросать мяч",
    19: "сидеть",
    20: "сесть",
    21: "ударять битой",
    22: "упражнение с мечом",
    23: "бросить",
}

transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Resize((256, 256), antialias=True),
    torchvision.transforms.Normalize(
        mean=(0.45, 0.45, 0.45),
        std=(0.225, 0.225, 0.225),
    ),
])

model = torch.hub.load('facebookresearch/pytorchvideo', 'slowfast_r50', pretrained=False)
# Replace head
model.blocks[6] = ResNetBasicHead(
    dropout=nn.Dropout(p=0.5, inplace=False),
    proj=nn.Linear(in_features=2304, out_features=24, bias=True),
    output_pool=nn.AdaptiveAvgPool3d(output_size=1),
)
model.load_state_dict(torch.load("weights/slowfast_r50_last_layers_epoch2_0.674acc.pt", map_location="cpu"))
model.to(device)
model.eval()

def predict_video(video_path: str) -> str:
    frames_generator = FramesGenerator(
        video_path=video_path,
        transform=transform,
    )

    post_act = nn.Softmax(dim=1).to(device)
    preds = torch.zeros(24).to(device)
    for slow_pathway, fast_pathway in frames_generator:
        input = [
            slow_pathway.to(device).unsqueeze(0),
            fast_pathway.to(device).unsqueeze(0),
        ]

        output = post_act(model(input))
        preds += output.reshape(-1)

        del slow_pathway
        del fast_pathway

    pred = torch.argmax(preds).item()
    return class2label[int(pred)]