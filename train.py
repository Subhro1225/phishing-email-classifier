# # joblib — efficiently saves/loads large Python objects (like ML models and arrays)
# # Why not pickle directly? joblib handles big numpy arrays better
import joblib
# import numpy as np

# # RandomForestClassifier — ensemble model that builds 100 decision trees
# # "Ensemble" = combines multiple models (100 trees) into one
# # Each tree votes on the prediction, final answer is the majority vote
# from sklearn.ensemble import RandomForestClassifier

# from sklearn.model_selection import GridSearchCV

# # precision_score — of emails flagged as phishing, how many actually were?
# # recall_score — of all real phishing emails, how many did we catch?
# # f1_score — balanced score between precision and recall (main metric we optimize for)
# from sklearn.metrics import precision_score, recall_score, f1_score 

# import xgboost as xgb
# import lightgbm as lgb

# # loading the training and testing data
# X_train = joblib.load('models/x_train.pkl')
# X_test = joblib.load('models/x_test.pkl')
# y_train = joblib.load('models/y_train.pkl')
# y_test = joblib.load('models/y_test.pkl')

# # ===== RANDOM FOREST MODEL =====
# rf_param_grid = {
#     'n_estimators': [100, 200],  # number of trees in the forest
#     'max_depth': [10, 20],  # maximum depth of each tree
#     'min_samples_split': [2, 5],  # minimum samples required to split a node
# }

# rf = RandomForestClassifier(random_state=42)
# rf_grid = GridSearchCV(rf, rf_param_grid, cv=5 , scoring='f1', n_jobs=-1)
# rf_grid.fit(X_train, y_train)


# print(f"BEST Random Forest Parameters: {rf_grid.best_params_}")   
# print(f"BEST Random Forest F1 Score (cv): {rf_grid.best_score_ :.4f}")

# rf_best = rf_grid.best_estimator_
# rf_pred = rf_best.predict(X_test)
# rf_precision = precision_score(y_test, rf_pred)
# rf_recall = recall_score(y_test, rf_pred)
# rf_f1 = f1_score(y_test, rf_pred)

# print(f"Random Forest Test Results - Precision: {rf_precision:.4f}, Recall: {rf_recall:.4f}, F1: {rf_f1:.4f}")

# joblib.dump(rf_best, 'models/random_forest_model.pkl')
# print("Random Forest model saved!")

# # ===== Xgboost MODEL =====

# xgb_model = xgb.XGBClassifier(n_estimators=200, max_depth=7, learning_rate=0.1, random_state=42, n_jobs=-1, use_label_encoder=False, eval_metric='logloss')
# xgb_model.fit(X_train, y_train)

# print(f"BEST XGBoost Parameters: {xgb_model.get_params()}")
# print(f"BEST XGBoost F1 Score (cv): {xgb_model.score(X_test, y_test) :.4f}")

# xgb_best = xgb_model
# xgb_pred = xgb_best.predict(X_test)
# xgb_precision = precision_score(y_test, xgb_pred)
# xgb_recall = recall_score(y_test, xgb_pred)
# xgb_f1 = f1_score(y_test, xgb_pred)

# print(f"XGBoost Test Results - Precision: {xgb_precision:.4f}, Recall: {xgb_recall:.4f}, F1: {xgb_f1:.4f}")

# joblib.dump(xgb_model, 'models/xgboost_model.pkl')
# print("XGBoost model saved!")

# # ===== LIGHTGBM =====
# print("\nTraining LightGBM...")

# # Convert sparse matrices to dense
# print("Converting to dense...")
# X_train_dense = X_train.toarray()
# X_test_dense = X_test.toarray()

# print(f"X_train_dense shape: {X_train_dense.shape}")

# lgb_model = lgb.LGBMClassifier(
#     n_estimators=100,
#     max_depth=7,
#     learning_rate=0.1,
#     num_leaves=31,
#     random_state=42,
#     n_jobs=1,  # Changed from -1
#     verbose=-1
# )

# print("Fitting model...")
# lgb_model.fit(X_train_dense, y_train)
# print("Model fitted!")

# lgb_pred = lgb_model.predict(X_test_dense)
# lgb_f1 = f1_score(y_test, lgb_pred)

# print(f"LightGBM F1: {lgb_f1:.4f}")
# joblib.dump(lgb_model, 'models/lightgbm_model.pkl')
# print("LightGBM model saved!")

# ===== EXPORT XGBOOST MODEL TO ONNX =====

import onnxmltools
from onnxmltools.convert.common.data_types import FloatTensorType
import onnx

# Load the best XGBoost model
xgb_best = joblib.load('models/xgboost_model.pkl')

# Define initial types (5000 features from TF-IDF)
initial_types = [('float_input', FloatTensorType([None, 5000]))]

# Convert XGBoost to ONNX
onnx_model = onnxmltools.convert_xgboost(xgb_best, initial_types=initial_types)

# Save ONNX model
onnx.save_model(onnx_model, 'models/xgboost_model.onnx')

print("XGBoost model exported to ONNX format!")

