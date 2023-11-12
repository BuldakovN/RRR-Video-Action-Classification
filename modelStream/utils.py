from typing import Callable, Tuple
from collections import defaultdict

import numpy as np
import cv2
import torch


def pack_pathway(frames_tensor: torch.Tensor, slowfast_alpha: int = 4) -> Tuple[torch.Tensor, torch.Tensor]:
    fast_pathway = frames_tensor
    slow_pathway = torch.index_select(
        frames_tensor,
        1,
        torch.linspace(
            0, frames_tensor.shape[1] - 1, frames_tensor.shape[1] // slowfast_alpha
        ).long(),
    )
    return slow_pathway, fast_pathway


class VideoIterator:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path
        self.video_capture = cv2.VideoCapture(video_path)

        self.width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.video_capture.get(cv2.CAP_PROP_FPS))
        self.frame_cnt = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def __len__(self):
        return self.frame_cnt

    def __iter__(self):
        self.video_capture = cv2.VideoCapture(self.video_path)
        return self

    def __next__(self):
        success, frame = self.video_capture.read()

        if success:
            return frame
        else:
            raise StopIteration


class ObjectsCache:
    def __init__(
        self,
        transform: Callable,
        windows_len: int = 32,
    ) -> None:
        self.transform = transform
        self.windows_len = windows_len

        self.objects = defaultdict(list)

    def get_crop(self, frame, box) -> np.array:
        return frame[box[1]:box[3], box[0]:box[2], :]

    def add_objects(self, frame: np.array, ids: np.array, boxes: np.array) -> None:
        for id, box in zip(ids, boxes):
            crop = self.get_crop(frame, box)
            self.objects[id].append(crop)

    def get_tensors(self) -> tuple:
        ids, frames = [], []
        for id in self.objects:
            if len(self.objects[id]) == self.windows_len:
                ids.append(id)
                frames.append(
                    torch.stack(
                        [
                            self.transform((frame / 255).astype(np.float32))
                            for frame in self.objects[id]
                        ],
                       axis=1,
                    )
                )

        for id in ids:
            del self.objects[id]

        return ids, frames