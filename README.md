# 📊 Text Classification Project

A Chinese sentiment analysis and text classification project built with deep learning models including TextCNN, Transformer, TextRNN, and TextRNN_Attention.

---

## 📁 Project Structure

```
├── preprocess/
├── basic_model/
├── model_enhancement/
└── classify.ipynb
```

---

## 1. `preprocess/`

This folder contains the preprocessed datasets and the preprocessing script.

> 📥 **Data Source**: The original data (`DMSC.csv`) comes from the [Douban Movie Short Comments dataset on Kaggle](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments). Download and place it in this folder before running preprocessing.

| File | Description |
|------|-------------|
| `train_pinggu.csv` | Preprocessed training dataset |
| `test_pinggu.csv` | Preprocessed testing dataset |
| `preprocessing.py` | Python script for data cleaning, tokenization, stopword removal, and train-test split |
| `cn_stopwords` | Text file containing Chinese stopwords used during preprocessing |

---

## 2. `basic_model/`

This folder includes code and saved models for baseline experiments.

### `basic_model.ipynb`
A Jupyter notebook implementing four baseline models for text classification:

- **TextCNN** — Convolutional Neural Network for text
- **Transformer** — Attention-based sequence model
- **TextRNN** — Recurrent Neural Network for text
- **TextRNN_Attention** — RNN with attention mechanism

Each model is trained and saved separately.

### `{ModelName}_model.pt`
Trained model files (`.pt`) corresponding to each baseline model. These can be loaded directly for inference on new input texts.

---

## 3. `model_enhancement/`

This folder contains experiments for improving the baseline models.

| Notebook | Description |
|----------|-------------|
| `textcnn_modify.ipynb` | Modified and enhanced version of the TextCNN model |
| `transformer_modify.ipynb` | Modified and enhanced version of the Transformer model |

---

## 4. `classify.ipynb`

An interactive notebook for classifying new text using pre-trained models.

- Input any new piece of text
- Select any of the saved `.pt` model files
- Get classification results on user-provided content

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install torch numpy pandas jieba scikit-learn jupyter
```

### Run Preprocessing

```bash
cd preprocess
python preprocessing.py
```

### Train Baseline Models

Open and run `basic_model/basic_model.ipynb` in Jupyter.

### Classify New Text

Open `classify.ipynb`, select a pre-trained model, and input your text to get predictions.

---

## 📌 Notes

- All models are designed for **Chinese text classification**.
- Stopword removal uses `cn_stopwords` during preprocessing.
- Model files use PyTorch's `.pt` format and can be loaded with `torch.load()`.
