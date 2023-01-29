import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor

COLUMNS = [
    'Path',
    'Atelectasis',
    'Consolidation',
    'Edema',
    'Pleural Effusion',
    'Pneumonia',
    'Pneumothorax',
    'Lung Opacity',
    'Lung Lesion',
    'Fracture',
    'No Finding'
]


class MultiLabelProcessing(DataProcessor):
    '''
    Process dataset to contain only important data for multilabel classification.
    '''

    def __init__(self, directory: str) -> None:
        super().__init__(directory)

    def process_dataset(self) -> dict:
        processed_datasets = {}
        for dataset in self.dataset_names:
            file = self.directory + '/' + dataset + '.csv'
            data = pd.read_csv(file)
            data = data.replace(-1, 0)
            data = data.fillna(0)
            data = data[COLUMNS]

            processed_datasets[dataset] = data.values.tolist()
        return processed_datasets


if __name__ == '__main__':
    processor = MultiLabelProcessing('dataset')
    processed_datasets = processor.process_dataset()
    processor.save_to_csv(processed_datasets)
