from abc import ABC, abstractmethod
import os
import csv


class DataProcessor(ABC):

    def __init__(self, read_directory: str = None,  write_directory: str = None) -> None:
        self.dataset_types = ('train', 'validation', 'test')
        self.read_directory = read_directory
        self.write_directory = write_directory

    @abstractmethod
    def process_dataset(self) -> None:
        pass

    def save_to_directory(self, datasets: dict) -> None:
        if not os.path.exists(self.write_directory):
            os.mkdir(self.write_directory)
        for dataset in datasets:
            with open(self.write_directory + '/' + dataset + '.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(datasets[dataset])
