from data_processor import DataProcessor
import os
import shutil

DISEASES = (
    'Atelectasis',
    'Consolidation',
    'Edema',
    'Pleural Effusion',
    'Pneumonia',
    'Pneumothorax',
    'Lung Opacity',
    'Lung Lesion',
    'Fracture'
)

TYPES = ('Sick', 'Healthy')


class SingleLabelProcessor(DataProcessor):
    '''
    Process dataset by adding desired images to proper folder. This solution allows to reduce RAM usage during classification.
    '''

    def __init__(self, directory: str) -> None:
        super().__init__(read_directory=directory)

    def process_dataset(self) -> dict:
        pass

    def make_directory_tree(self, directory: str) -> None:
        if not os.path.exists(directory):
            os.mkdir(directory)
        for dataset in self.dataset_names:
            os.mkdir(directory + '/' + dataset)
            for disease in DISEASES:
                os.mkdir(directory + '/' + dataset + '/' + disease)
                for type in TYPES:
                    os.mkdir(directory + '/' + dataset +
                             '/' + disease + '/' + type)


if __name__ == '__main__':
    processor = SingleLabelProcessor('dataset')
    processor.make_directory_tree('dataset_singlelabel')
    # processed_datasets = processor.process_dataset()
    # processor.save_to_directory('dataset_multilabel')
