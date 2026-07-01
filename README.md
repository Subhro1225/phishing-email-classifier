# 📧 Phishing Email Classifier — Team 1: Email Intelligence

> A machine learning model that reads an email and decides whether it is a phishing attempt or legitimate. Part of the larger **Email Safety Checker** browser extension project.

---

## 🗂 Project Structure

```
phishing-email-classifier/
│
├── data/
│   ├── *.csv                  → Raw dataset files (7 CSVs)
│   └── cleaned_emails.csv     → Cleaned & combined dataset
│
├── venv/                      → Virtual environment (do not commit)
├── explore_data.py            → Data loading & cleaning pipeline
├── requirements.txt           → All dependencies
└── README.md                  → You are here
```

---

## ⚙️ Setup — Do This First

Make sure you have Python installed. Then:

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/phishing-email-classifier.git
cd phishing-email-classifier

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🎯 Final Deliverable

A running FastAPI endpoint that accepts email data and returns a risk score.

```
POST /analyze/email

Input:
{
  "subject": "Urgent: Verify your account",
  "body": "Dear user, click here to verify...",
  "sender": "security@tatamotors-support.com"
}

Output:
{
  "email_score": 0.87,
  "label": "phishing",
  "confidence": "high"
}
```

---

## ✅ Project Phases

### Phase 1 — Data Collection & Cleaning
> Load, combine and clean the dataset so it's ready for feature extraction.

- [x] Download phishing email dataset (7 CSV files)
- [x] Load and combine all 7 CSV files into one dataframe
- [x] Drop unwanted columns (kept: subject, body, label)
- [x] Remove null rows
- [x] Check and remove duplicates
- [x] Verify class balance (~50% phishing / ~50% legitimate)
- [x] Save cleaned dataset to `data/cleaned_emails.csv`

**File:** `explore_data.py`

---

### Phase 2 — Feature Engineering (TF-IDF)
> Convert raw email text into numbers the model can learn from.

- [x] Combine subject + body into one text field
- [x] Apply TF-IDF vectorization (converts text to weighted word numbers)
- [x] Set max_features=5000 (manageable vocabulary)
- [x] Apply stop_words='english' (remove junk words)
- [x] Train/test split: 80% training / 20% testing
- [x] Save processed data (X_train, X_test, y_train, y_test) as .pkl files
- [x] Save TF-IDF vectorizer for later use in the API

**Note:** Hand-crafted features (urgency words, link count, caps ratio, SPF/DKIM/DMARC) will be added in Phase 4 for better interpretability and to match the team API contract with `top_signals`.

**Files:** `feature_extraction.py`

**Outcome:** 
- 82,138 emails split into (65,710 train) and (16,428 test)
- 5,000 word vocabulary (cleaned from 558k junk words)

---

### Phase 3 — Model Training & Evaluation
> Train ML models and measure how well they detect phishing.

- [x] Split data: 80% training / 20% testing
- [x] Train Naive Bayes model (baseline) → **F1: 0.9649** ✅
- [x] Train Random Forest model (comparison) → **F1: 0.9835** 
- [x] Evaluate both models using:
  - [x] Precision (Naive Bayes: 0.9759, Random Forest: 0.9859)
  - [x] Recall (Naive Bayes: 0.9540, Random Forest: 0.9811)
  - [x] F1 Score (Naive Bayes: 0.9649, Random Forest: 0.9835)
- [x] Compare results — **selected Naive Bayes for API**
- [x] Save both models to `models/` folder

**Decision Rationale:** Naive Bayes chosen for final API due to:
- 96.49% F1 score (excellent accuracy)
- Millisecond inference time (critical for user experience)
- 2% performance difference from Random Forest doesn't justify slower inference

**Files:** `train.py`

---

### Phase 4 — API & Production Features
> Wrap the trained model in FastAPI, add explainability, and match team contract.

- [ ] Create FastAPI server on port 8001
- [ ] Load saved Naive Bayes model and TF-IDF vectorizer on startup
- [ ] Add hand-crafted feature extraction:
  - [ ] Urgency word detection (verify, urgent, confirm, click, suspended...)
  - [ ] Sender domain validation (extract domain, check against known brands)
  - [ ] Link count and analysis in body
  - [ ] SPF/DKIM/DMARC header validation (fail/pass/none)
  - [ ] Caps ratio (% uppercase), exclamation marks, suspicious patterns
- [ ] Integrate SHAP for feature explainability (determines `top_signals`)
- [ ] Build `POST /analyze/email` endpoint with exact contract:
  - **Input:** subject, body, sender, reply_to, spf, dkim, dmarc
  - **Output:** email_score (0.0-1.0), label ('phishing'/'legitimate'), top_signals (list), confidence ('high'/'medium'/'low')
- [ ] Build `GET /health` endpoint
- [ ] Export model to ONNX format (cross-platform compatibility)
- [ ] Robust error handling (missing fields → empty string, no 500 errors)
- [ ] Test with sample phishing and legitimate emails
- [ ] Document API contract for Team 3

**Files:** `api/main.py`, `utils/feature_engineer.py`, `utils/explainer.py`

**API Contract (per Team Guidelines):**
```json
POST /analyze/email
Input: {
  "subject": "Urgent: Verify account",
  "body": "Click here...",
  "sender": "security@bank.com",
  "reply_to": "harvester@xyz.com",
  "spf": "fail",
  "dkim": "fail",
  "dmarc": "fail"
}

Output: {
  "email_score": 0.87,
  "label": "phishing",
  "top_signals": ["urgency_language", "sender_domain_mismatch", "failed_dkim"],
  "confidence": "high"
}
```

---

### Phase 5 — Integration & Handoff
> Connect with the browser extension team (Team 3).

- [ ] Confirm API contract with Team 3
- [ ] Test end-to-end: extension → API → response
- [ ] Document any changes to the API contract
- [ ] Final code review and cleanup

---

## 📦 Dataset

**Source:** Phishing Email Dataset (Kaggle) — 7 CSV files  
**Combined size:** ~82,000 emails  
**Balance:** ~50% phishing / ~50% legitimate  
**Columns used:** `subject`, `body`, `label`  
**Label format:** `1` = phishing, `0` = legitimate

---

## 🧠 Key Concepts

| Concept | Simple Explanation |
|---|---|
| TF-IDF | Converts words to numbers, rewards rare suspicious words, punishes common ones |
| Precision | When model says phishing, how often is it right? |
| Recall | Of all real phishing emails, how many did we catch? |
| F1 Score | Balance between precision and recall — main metric to optimize |
| Overfitting | Model memorizes training data but fails on new emails |
| Data Leakage | Column that accidentally gives away the answer |

---

## 🌿 Git Workflow

```bash
# Always pull before starting work
git pull origin main

# After completing work
git add .
git commit -m "phase2: feature extraction complete"
git push
```

**Commit message format:**
```
phase1: data cleaning pipeline
phase2: tfidf vectorization done
phase3: random forest trained, f1=0.94
phase4: fastapi endpoint live
```

---

## 📋 Requirements

```
pandas
scikit-learn
fastapi
uvicorn
nltk
beautifulsoup4
joblib
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 👥 Team

| Member | Role |
|---|---|
| You | ML model, feature engineering, API |
| Girlfriend | ML model, data cleaning, evaluation |

---

*Part of the Email Safety Checker project — 6-person team building a browser extension to detect malicious emails and links.*
