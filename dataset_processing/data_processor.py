from abc import ABC, abstractmethod
import os
import csv


class DataProcessor(ABC):

    def __init__(self, directory: str, data_file: str = None) -> None:
        self.dataset_names = ('train', 'validation', 'test')
        # directory that contains all three datasets
        self.directory = directory
        # optinal file with data to process
        self.data_file = data_file

    @abstractmethod
    def process_dataset(self) -> None:
        pass

    def save_to_csv(self, datasets: dict) -> None:
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        for dataset in datasets:
            with open(self.directory + '/' + dataset + '.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(datasets[dataset])
