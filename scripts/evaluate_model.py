import os
import sys

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import tensorflow as tf
import numpy as np
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# -----------------------------
# Paths
# -----------------------------
test_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\test"

model_path = r"D:\Projects\AI-Plant-Disease-Detection-System\models\best_model.keras"

# -----------------------------
# Parameters
# -----------------------------
IMG_SIZE = (224, 224)
BATCH_SIZE = 16

# -----------------------------
# Load Test Dataset
# -----------------------------
test_dataset = tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

class_names = test_dataset.class_names

print("\nClasses:")
for i, c in enumerate(class_names):
    print(f"{i}: {c}")

# -----------------------------
# Load Model
# -----------------------------
model = tf.keras.models.load_model(model_path)

# -----------------------------
# Predict
# -----------------------------
predictions = model.predict(test_dataset)

y_pred = np.argmax(predictions, axis=1)

# True labels
y_true = np.concatenate(
    [labels.numpy() for _, labels in test_dataset],
    axis=0
)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_true, y_pred)

print("\n" + "="*50)
print(f"Test Accuracy: {accuracy*100:.2f}%")
print("="*50)

# -----------------------------
# Classification Report
# -----------------------------
print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names
    )
)

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_true, y_pred)

print("\nConfusion Matrix:\n")
print(cm)