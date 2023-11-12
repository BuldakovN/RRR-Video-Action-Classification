import torchvision.transforms as transforms


# Dataset
train_dataset_path = "dataset/train"
test_dataset_path = "dataset/test"
classes_num = 24
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((256, 256), antialias=True),
    transforms.Normalize(
        mean=(0.45, 0.45, 0.45),
        std=(0.225, 0.225, 0.225),
    ),
])

# Model
device = "cuda"
basemodel = "slowfast_r50"
pretrained = True
save_path = "weights/slowfast_r50_3epochs.pt"

# Optimizer
lr = 3e-4
weight_decay = 1e-9

# Training
epochs_num = 3
