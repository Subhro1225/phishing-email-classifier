# ===== NAIVE BAYES MODEL =====

# joblib — efficiently saves/loads large Python objects (like ML models and arrays)
# Why not pickle directly? joblib handles big numpy arrays better
import joblib

# MultinomialNB — Naive Bayes classifier designed for text/count data
# "Multinomial" = handles multiple word occurrences per email
# "Naive" = assumes each word is independent (oversimplified but works well for text)
from sklearn.naive_bayes import MultinomialNB

# precision_score — of emails flagged as phishing, how many actually were?
# recall_score — of all real phishing emails, how many did we catch?
# f1_score — balanced score between precision and recall (main metric we optimize for)
from sklearn.metrics import precision_score, recall_score, f1_score 

# loading the training and testing data
X_train = joblib.load('models/x_train.pkl')
X_test = joblib.load('models/x_test.pkl')
y_train = joblib.load('models/y_train.pkl')
y_test = joblib.load('models/y_test.pkl')


# print("data loaded successfully")
# print(X_train.shape)

model = MultinomialNB()
model.fit(X_train, y_train)
# print("model trained successfully")

y_pred = model.predict(X_test)
# print(y_pred[:10]) # prints first 10 predictions

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Precision: {precision :.4f}")
print(f"Recall: {recall :.4f}")
print(f"F1 Score: {f1 :.4f}")

joblib.dump(model, 'models/native_bayes_model.pkl')
# print("model saved successfully")

# ===== RANDOM FOREST MODEL =====

# RandomForestClassifier — ensemble model that builds 100 decision trees
# "Ensemble" = combines multiple models (100 trees) into one
# Each tree votes on the prediction, final answer is the majority vote
# More complex than Naive Bayes, usually better accuracy but slower
from sklearn.ensemble import RandomForestClassifier


# n_estimators=100 — build 100 separate decision trees
# random_state=42 — reproducible results (same trees every run)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
print("random forest model trained")

rf_pred = rf_model.predict(X_test)

rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)  
rf_f1 = f1_score(y_test, rf_pred)

print(f"Random Forest Precision: {rf_precision :.4f}")
print(f"Random Forest Recall: {rf_recall :.4f}")    
print(f"Random Forest F1 Score: {rf_f1 :.4f}")

joblib.dump(rf_model, 'models/random_forest_model.pkl')

# ===== MODEL COMPARISON =====
print("\n" + "="*50)
print("MODEL COMPARISON")
print("="*50)
print(f"Naive Bayes  — F1: 0.9649")
print(f"Random Forest — F1: 0.9835")
print("\nDecision: Using Naive Bayes for API")
print("Reason: Excellent accuracy (96.49%) with much faster inference")
print("="*50)
