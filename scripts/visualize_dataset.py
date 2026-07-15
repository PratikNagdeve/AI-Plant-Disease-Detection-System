import os
import matplotlib.pyplot as plt
from PIL import Image
import random


dataset_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test\train"


classes = os.listdir(dataset_path)

# Select random classes
selected_classes = random.sample(classes, 5)


plt.figure(figsize=(12, 8))


for i, class_name in enumerate(selected_classes):

    class_path = os.path.join(dataset_path, class_name)

    image_name = random.choice(os.listdir(class_path))

    image_path = os.path.join(class_path, image_name)

    image = Image.open(image_path)

    plt.subplot(2, 3, i + 1)
    plt.imshow(image)
    plt.title(class_name[:25])
    plt.axis("off")


plt.tight_layout()
plt.show()