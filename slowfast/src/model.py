import torch
import torch.nn as nn
from pytorchvideo.models.head import ResNetBasicHead


def get_slowfast_model(
    basemodel: str = "slowfast_r50",
    pretrained: bool = True,
    out_features: int = 24,
):
    model = torch.hub.load('facebookresearch/pytorchvideo', basemodel, pretrained=pretrained)
    model.blocks[6] = ResNetBasicHead(
        dropout=nn.Dropout(p=0.5, inplace=False),
        proj=nn.Linear(in_features=2304, out_features=out_features, bias=True),
        output_pool=nn.AdaptiveAvgPool3d(output_size=1),
    )
    return model
