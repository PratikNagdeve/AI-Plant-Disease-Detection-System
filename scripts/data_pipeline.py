import tensorflow as tf


train_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\train"

val_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\val"


IMG_SIZE = (224, 224)
BATCH_SIZE = 32


# Load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


# Load validation dataset
val_dataset = tf.keras.utils.image_dataset_from_directory(
    val_path,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


# Class names
class_names = train_dataset.class_names


print("\nClasses:")
for i, name in enumerate(class_names):
    print(i, name)


print("\nNumber of classes:", len(class_names))


# Check batch shape
for images, labels in train_dataset.take(1):
    print("\nImage batch shape:", images.shape)
    print("Label batch shape:", labels.shape)