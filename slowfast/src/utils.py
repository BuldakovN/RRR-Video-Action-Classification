from typing import Callable, Tuple
import math
import cv2


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


class FramesGenerator(VideoIterator):
    def __init__(
        self,
        video_path: str,
        transform: Callable,
        window_len: int = 32,
        slowfast_alpha: int = 4,
    ) -> None:
        super().__init__(video_path)
        self.transform = transform
        self.window_len = window_len
        self.slowfast_alpha = slowfast_alpha

    def pack_pathway(self, frames) -> Tuple[torch.Tensor, torch.Tensor]:
        frames_tensor = torch.stack(frames, axis=1)

        fast_pathway = frames_tensor
        slow_pathway = torch.index_select(
            frames_tensor,
            1,
            torch.linspace(
                0, frames_tensor.shape[1] - 1, frames_tensor.shape[1] // self.slowfast_alpha
            ).long(),
        )
        return slow_pathway, fast_pathway

    def __len__(self):
        return math.ceil(super().__len__() / self.window_len)

    def __next__(self):
        frames = []
        for _ in range(self.window_len):
            frame = self.transform((super().__next__() / 255).astype(np.float32))
            frames.append(frame)

        return self.pack_pathway(frames)
