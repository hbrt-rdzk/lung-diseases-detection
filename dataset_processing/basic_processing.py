import csv
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor


class BasicProcessing(DataProcessor):
    '''
    Dividing dataset into train, validation and test datasets, randomly, without any data processing.
    '''

    def __init__(self, directory: str, data_file: str) -> None:
        super().__init__(directory, data_file)

    def process_dataset(self, test_size: float = 0.2) -> dict:
        with open(self.data_file, 'r') as file:
            reader = list(csv.reader(file))
        info = reader.pop(0)
        train, test = train_test_split(
            reader, shuffle=True, test_size=test_size)
        valid, test = train_test_split(test, shuffle=True, test_size=0.5)
        for dataset in (train, valid, test):
            dataset.insert(0, info)

        return {
            self.dataset_names[0]: train,
            self.dataset_names[1]: valid,
            self.dataset_names[2]: test
        }


if __name__ == "__main__":
    processor = BasicProcessing('dataset', "CheXpert-v1.0-small/train.csv")
    processed_dataset = processor.process_dataset()
    processor.save_to_csv(processed_dataset)
