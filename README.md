# CheXpert based lung diseases classifier

Process of data processing and neural networks training, to classify nine lung diseases on x-ray pictures.

## Dataset

Neural networks models were trained on dataset called CheXpert, that contains of 223,648 labeled, lung, x-ray images.
Considered diseases:

- Lung Lesion
- Lung Opacity
- Edema
- Consolidation
- Pneumonia
- Atelectasis
- Pneumothorax
- Pleural Effusion
- Pleural Other

## CNN Architectures

Trained architectures:

- VGG-16
- ResNet-50
- DenseNet-121

## Set up dataset

1. Make sure you have CheXpert-v1.0-small in your root directory.
2. Run `pip3 install -r python3-requirements.txt` to install packages.
3. Run cells at `dataset_processing/divide_and_process.ipynb` to process and divide dataset into train, validation and test datasets.

## Results

Reults can be found in attached engineer thesis. [PL Only]
