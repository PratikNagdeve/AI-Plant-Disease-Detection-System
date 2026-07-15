import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

from models.plant_disease_model import create_model


# Paths
train_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\train"

val_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\val"


# Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 2


# Load datasets
train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


val_dataset = tf.keras.utils.image_dataset_from_directory(
    val_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


# Improve performance
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(AUTOTUNE)
val_dataset = val_dataset.prefetch(AUTOTUNE)


# Create model
model = create_model()


# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# Callbacks

checkpoint = ModelCheckpoint(
    "models/best_model.keras",
    monitor="val_accuracy",
    save_best_only=True,
    mode="max"
)


early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)


# Training
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS,
    callbacks=[
        checkpoint,
        early_stop
    ]
)


print("Training completed successfully")