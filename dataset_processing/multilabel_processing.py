import pandas as pd
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


class MultiLabelProcessor(DataProcessor):
    '''
    Process dataset to contain only important data for multilabel classification.
    '''

    def __init__(self, read_directory: str, write_directory: str) -> None:
        super().__init__(read_directory=read_directory, write_directory=write_directory)

    def process_dataset(self) -> dict:
        processed_datasets = {}
        for dataset in self.dataset_types:
            file = self.read_directory + '/' + dataset + '.csv'
            data = pd.read_csv(file)
            data = data.replace(-1, 0)
            data = data.fillna(0)
            data = data[COLUMNS]
            processed_datasets[dataset] = data.values.tolist()
        return processed_datasets


if __name__ == '__main__':
    processor = MultiLabelProcessor('dataset', 'dataset_multilabel')
    processed_datasets = processor.process_dataset()
    processor.save_to_directory(processed_datasets)
