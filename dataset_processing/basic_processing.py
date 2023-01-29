import csv
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor


class BasicProcessing(DataProcessor):
    '''
    Dividing dataset into train, validation and test datasets, randomly, without any data processing.
    '''

    def __init__(self, file: str) -> None:
        super().__init__(file)

    def divide_dataset(self, test_size: float = 0.2) -> dict:
        with open(self.data_file, 'r') as file:
            reader = list(csv.reader(file))
        train, test = train_test_split(
            reader, shuffle=True, test_size=test_size)
        valid, test = train_test_split(test, shuffle=True, test_size=0.5)
        return {
            'train': train,
            'validation': valid,
            'test': test
        }


if __name__ == "__main__":
    processor = BasicProcessing("CheXpert-v1.0-small/train.csv")
    divided_dataset = processor.divide_dataset()
    DataProcessor.save_to_csv(divided_dataset, "dataset")
