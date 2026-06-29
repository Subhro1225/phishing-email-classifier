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
git clone https://github.com/Subhro1225/phishing-email-classifier.git
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

### Phase 2 — Feature Engineering
> Convert raw email text into numbers the model can learn from.

- [ ] Combine subject + body into one text field
- [ ] Apply TF-IDF vectorization (converts text to weighted word numbers)
- [ ] Extract hand-crafted features:
  - [ ] urgency word count (urgent, verify, click here, suspended...)
  - [ ] number of links in body
  - [ ] caps ratio (% of uppercase characters)
  - [ ] exclamation mark count
  - [ ] body length
- [ ] Save TF-IDF vectorizer for later use in the API

**File:** `feature_extraction.py`

---

### Phase 3 — Model Training & Evaluation
> Train the ML model and measure how well it detects phishing.

- [ ] Split data: 80% training / 20% testing
- [ ] Train Naive Bayes model (baseline)
- [ ] Train Random Forest model (improved)
- [ ] Evaluate both models using:
  - [ ] Precision
  - [ ] Recall
  - [ ] F1 Score
- [ ] Compare results and pick the best model
- [ ] Save final model to `models/email_model.pkl`

**File:** `train.py`

---

### Phase 4 — FastAPI Endpoint
> Wrap the trained model in an API so the browser extension can call it.

- [ ] Create FastAPI server
- [ ] Load saved model and vectorizer on startup
- [ ] Build `POST /analyze/email` endpoint
- [ ] Build `GET /health` endpoint
- [ ] Test with sample phishing and legitimate emails
- [ ] Server runs on port 8001

**File:** `api/main.py`

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
| priya | ML model, data cleaning, evaluation |

---

*Part of the Email Safety Checker project — 6-person team building a browser extension to detect malicious emails and links.*