# 📱 ThaiSMS-ScamGuard: Deep Learning-based Thai SMS Scam Detection

**Term Project: DADS7203 Semester 1/2567**  

ThaiSMS-ScamGuard is a deep learning-based system for detecting scam SMS messages in the Thai language.  
We fine-tuned **OpenThaiGPT 1.5 7b**, a large Thai language model, using transfer learning to classify SMS messages into two categories: **Scam** and **Non-Scam**.

The system applies tokenization, attention mechanisms, and a custom classification head built atop the pre-trained model to predict SMS authenticity with real-world Thai datasets.

---

## 📦 Dataset

- Total messages: **615** (Scam: 306, Non-Scam: 309)
- Data sources:
  - Actual SMS messages received by team members
  - Public datasets collected via Google search
- Data splitting:
  - Train: **70%**, Validation: **10%**, Test: **20%** (using stratified sampling)

---

## ⚙️ Proposed Method

### 1. Transfer Learning Setup
- Used **OpenThaiGPT 1.5 7b** as a **feature extractor** (frozen weights).
- Added a **custom classification head**:  
  - Two fully connected layers (512 → 256 nodes)  
  - Final Softmax layer for binary classification (Scam / Non-Scam)

### 2. Tokenization
- Employed OpenThaiGPT's tokenizer with:
  - `truncation=True`, `padding='max_length'`, max length = 512 tokens
  - Generated attention masks for sequence handling.

### 3. Model Training
- Loss Function: **Binary Cross-Entropy**
- Optimizer: **Adam** (Learning rate: 0.001, Batch size: 16)
- Early Stopping:
  - Patience: 3 epochs
  - Final training completed in **5 epochs** due to early stop.

### 4. Evaluation Metrics
- Accuracy: **72%**
- Precision: **72%**
- Recall: **72%**
- F1-Score: **72%**

**Confusion Matrix** analysis shows a slight bias towards false positives (scam prediction).
![Model Training Progress](https://raw.githubusercontent.com/bubblebolt/dads/main/ThaiSMS-ScamGuard_Group1/Pics/Picture1.png)

---

## 🛠️ Inference Process

- Input text → Tokenization
- Forward pass through OpenThaiGPT
- Classification head outputs prediction
- Model saved and reloadable for unseen SMS classification.

---

## 🧩 Code Structure

- Load and preprocess dataset
- Build and compile model
- Tokenize SMS messages
- Train and validate with Early Stopping
- Evaluate with performance metrics and confusion matrix
- Save model and tokenizer
- Inference on unseen Thai SMS

---

# 🏆 Key Achievements

- Successfully fine-tuned OpenThaiGPT for Thai binary SMS classification.
- Achieved **72% overall accuracy** on unseen test data.
- Built a scalable, deployable model capable of real-time Thai SMS scam detection.

---

  ## 📚 Data Source

- Student project dataset from **Varee Chiangmai School**  

---
**Team Members:**  
- Siriwan Sreebutkot (6520422019)  
- Chalita Iamleelaporn (6610412002)  
- Ranakorn Boonsuankergchai (6610412003)
