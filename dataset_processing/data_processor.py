from abc import ABC, abstractmethod
import os
import csv


class DataProcessor(ABC):
    
    def __init__(self, file: str) -> None:
        self.data_file = file

    @abstractmethod
    def divide_dataset(self) -> None:
        pass

    @staticmethod
    def save_to_csv(datasets: dict, directory: str) -> None:
        if not os.path.exists(directory):
            os.mkdir(directory)

        for dataset in datasets:
            with open(directory + '/' + dataset + '.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(datasets[dataset])
