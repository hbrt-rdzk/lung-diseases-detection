import csv
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor


class BasicProcessor(DataProcessor):
    '''
    Dividing dataset into train, validation and test datasets, randomly, without any data processing.
    '''

    def __init__(self, directory: str) -> None:
        super().__init__(read_directory=directory, write_directory=directory)

    def process_dataset(self, csv_file: str, test_size: float = 0.2) -> dict:
        with open(csv_file, 'r') as file:
            reader = list(csv.reader(file))
        info = reader.pop(0)
        train, test = train_test_split(
            reader, shuffle=True, test_size=test_size)
        valid, test = train_test_split(test, shuffle=True, test_size=0.5)
        for dataset in (train, valid, test):
            dataset.insert(0, info)

        return {
            self.dataset_types[0]: train,
            self.dataset_types[1]: valid,
            self.dataset_types[2]: test
        }


if __name__ == "__main__":
    processor = BasicProcessor('dataset')
    processed_dataset = processor.process_dataset(
        "CheXpert-v1.0-small/train.csv")
    processor.save_to_directory(processed_dataset)
