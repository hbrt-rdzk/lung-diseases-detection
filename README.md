# CheXpert based lung diseases classifier

Process of data processing and neural networks training, to classify ten lung diseases on x-ray pictures.

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
- Fracture

## Trained CNN Architectures

- VGG-16
- ResNet-50
- DenseNet-121

## Set up dataset

1. Make sure you have CheXpert-v1.0-small in your root directory.
2. Run `pip3 install -r python3-requirements.txt` to install packages.
3. Run cells at `dataset_processing/divide_and_process.ipynb` to process and divide dataset into train, validation and test datasets (Multilabel technic).
4. Run cells at `dataset_processing/folder_tree.ipynb` to make folder tree containing desired diseases (Singlelabel techinc).
5. Now Your environment to train CNN is ready. 

Project structure after those steps, should add these folders:

- 📁 CheXpert-v1.0-small ~ Dataset, can be downloaded from: https://stanfordmlgroup.github.io/competitions/chexpert/
- 📁 dataset
    - 📄 test.csv
    - 📄 train.csv
    - 📄 validation.csv
- 📁 dataset_tree
    - 📁 Atlectasis
        - 📁 Healthy 
        - 📁 Sick
    - 📁 Consolidation
        - 📁 Healthy 
        - 📁 Sick
    - ...
## Results

Reults can be found in owner's engineer thesis, upon request. [PL Only]
