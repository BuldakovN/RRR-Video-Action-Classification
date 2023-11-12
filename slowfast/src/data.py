import os
import os.path as path

from torch.utils.data import Dataset


class VideosDataset(Dataset):
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.paths = []
        self.labels = []
        self.class2label = dict()
        for i, class_folder in enumerate(sorted(os.listdir(self.root_dir))):
            self.class2label[class_folder] = i
            for video in os.listdir(path.join(self.root_dir, class_folder)):
                video_path = path.join(self.root_dir, class_folder, video)
                self.paths.append(video_path)
                self.labels.append((i, class_folder))

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, index):
        return self.paths[index], self.labels[index][0]
