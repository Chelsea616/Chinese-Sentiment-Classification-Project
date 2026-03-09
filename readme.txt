1. preprocess/
This folder contains the raw data, preprocessed datasets, and the preprocessing script:
DMSC.csv: The original source data before preprocessing.
test_pinggu.csv and train_pinggu.csv: Preprocessed datasets split into testing and training sets.
preprocessing.py: Python script for data cleaning, tokenization, stopword removal, and train-test split.
cn_stopwords: A text file containing Chinese stopwords used during preprocessing.

2. basic_model/
This folder includes code and saved models for baseline experiments:
basic_model.ipynb: Jupyter notebook implementing four baseline models:
TextCNN
Transformer
TextRNN
TextRNN_Attention
Each model is trained for text classification and saved separately.
{ModelName}_model.pt: Trained model files corresponding to each baseline model. These can be loaded for inference on new input texts.

3. model_enhancement/
This folder contains experiments for improving baseline models:
textcnn_modify.ipynb: Modified and enhanced version of the TextCNN model.
transformer_modify.ipynb: Modified and enhanced version of the Transformer model.

4. classify.ipynb
This notebook is used to input a new piece of text and perform classification using the pre-trained models. You can select any of the saved models to classify new user-provided content.
