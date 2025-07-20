# Password-strength-classifier-from-text
We take the text data from file and extract various features using pandas library and create our csv file
We can classify the password as very easy, easy, medium and hard.

# 🔐 Password Strength Classification using Machine Learning

This project performs **password strength classification** using a combination of entropy analysis, character variety, brute-force time estimation, and a machine learning model trained on real-world password data.

## 🚀 Overview

The pipeline consists of two main steps:
1. **Feature Extraction** from a password dataset (`rockyou.txt`) to compute entropy, variety, length, estimated brute-force time, and overall strength classification.
2. **Password Strength Prediction** using a `RandomForestClassifier` trained on TF-IDF character n-gram features.

---

## 📁 File Structure

- `feature_extraction.py`: Extracts features from raw password data and classifies them into four categories: `very easy`, `easy`, `medium`, `hard`.
- `prediction.py`: Builds and evaluates a machine learning model to predict password strength.

---

## 🔍 Features Extracted

Each password is analyzed for the following:

- **Length**: Number of characters
- **Entropy**: Shannon entropy representing randomness
- **Variety**: Number of character types used (uppercase, lowercase, digits, special chars)
- **Estimated Break Time**: Time (in seconds) for brute-force attack assuming 1 billion guesses/sec
- **Strength Label**: Custom label from `very easy` to `hard` based on a scoring system

---

## 🤖 ML Model Details

- **Vectorization**: Character-level TF-IDF (`1-3` gram)
- **Classifier**: Random Forest (`100` trees)
- **Target**: Strength class encoded as numeric labels (0-3)
- **Evaluation**: Accuracy on training & test set, confusion matrix visualization

---

## 📊 Sample Outputs

- Training accuracy: ~99%
- Test accuracy: ~90-95% (depending on entropy thresholds and variety)

Confusion matrix is also plotted to visualize classification performance.

---

## 🧪 Getting Started

### 🔧 Installation

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### ▶️ Run the Pipeline

1. **Feature extraction** (make sure `rockyou.txt` is in your directory):

```bash
python feature_extraction.py
```

2. **Train and evaluate model**:

```bash
python prediction.py
```

---

## 📘 Notes

- Uses a widely known password dataset (`rockyou.txt`) – ensure legal and ethical use.
- Strength scores are heuristic-based and can be tuned further.
- Classifier can be swapped with other models like SVM, XGBoost for experimentation.

---

## 🧠 Future Work

- GUI integration for real-time password evaluation
- Incorporate deep learning models (e.g., LSTM, Transformers)
- Real-world password policy recommendations

---

## 🛡️ Disclaimer

This project is intended for educational purposes only. Do not use it to store, transmit, or test real-world sensitive data or credentials.

---

## 📬 Contact

Made with ❤️ for cybersecurity & machine learning enthusiasts. Contributions welcome!

