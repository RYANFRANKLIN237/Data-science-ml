import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the Digits dataset
digits = load_digits()
X, y = digits.data, digits.target

# Split the dataset (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Define models  beginning of question 1
models = {
    "Logistic Regression": LogisticRegression(max_iter=5000),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(),
    "Decision Tree": DecisionTreeClassifier()
}

# Train and evaluate each model
scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    scores[name] = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {scores[name]:.4f}")

# end of question 1  
  
#beginning of question 2
# Use cross-validation (5-fold)
cv_scores = {name: np.mean(cross_val_score(model, X, y, cv=5)) for name, model in models.items()}
print("\nCross-Validation Scores:")
for name, score in cv_scores.items():
    print(f"{name}: {score:.4f}")

# Find the best model
best_model_name = max(scores, key=scores.get)
best_model = models[best_model_name]

# end of question 2

# beginning of question 3

# Compute confusion matrix
y_pred_best = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred_best)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=digits.target_names, yticklabels=digits.target_names)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title(f"Confusion Matrix for {best_model_name}")
plt.show()
