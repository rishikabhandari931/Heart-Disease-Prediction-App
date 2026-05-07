# Install if needed
# pip install catboost scikit-learn pandas

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('heart_f.csv')

# -----------------------------
# 1. Basic preprocessing
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Separate features and target
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# Identify categorical columns
cat_features = X.select_dtypes(include=['object']).columns.tolist()

print("\nCategorical Columns:", cat_features)

# Fill missing values
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = cat_features

# Numerical → median
num_imputer = SimpleImputer(strategy='median')
X[num_cols] = num_imputer.fit_transform(X[num_cols])

# Categorical → most frequent
cat_imputer = SimpleImputer(strategy='most_frequent')
X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])

# -----------------------------
# 2. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -----------------------------
# 3. CatBoost Model
# -----------------------------
model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=6,
    loss_function='Logloss',
    eval_metric='AUC',
    verbose=100
)

# Train
model.fit(
    X_train,
    y_train,
    cat_features=cat_features,
    eval_set=(X_test, y_test),
    early_stopping_rounds=50
)

# -----------------------------
# 4. Predictions
# -----------------------------
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# -----------------------------
# 5. Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print("\nFinal Results")
print(f"Accuracy: {accuracy:.4f}")
print(f"ROC-AUC: {roc_auc:.4f}")

=======
# Install if needed
# pip install catboost scikit-learn pandas

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('heart_f.csv')

# -----------------------------
# 1. Basic preprocessing
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Separate features and target
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# Identify categorical columns
cat_features = X.select_dtypes(include=['object']).columns.tolist()

print("\nCategorical Columns:", cat_features)

# Fill missing values
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = cat_features

# Numerical → median
num_imputer = SimpleImputer(strategy='median')
X[num_cols] = num_imputer.fit_transform(X[num_cols])

# Categorical → most frequent
cat_imputer = SimpleImputer(strategy='most_frequent')
X[cat_cols] = cat_imputer.fit_transform(X[cat_cols])

# -----------------------------
# 2. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -----------------------------
# 3. CatBoost Model
# -----------------------------
model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=6,
    loss_function='Logloss',
    eval_metric='AUC',
    verbose=100
)

# Train
model.fit(
    X_train,
    y_train,
    cat_features=cat_features,
    eval_set=(X_test, y_test),
    early_stopping_rounds=50
)

# -----------------------------
# 4. Predictions
# -----------------------------
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# -----------------------------
# 5. Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print("\nFinal Results")
print(f"Accuracy: {accuracy:.4f}")
print(f"ROC-AUC: {roc_auc:.4f}")

model.save_model("heart_model.cbm")