import os

base_path = r"D:\Projects\AI-Plant-Disease-Detection-System\dataset\PlantVillageDataset\train_val_test"


def analyze_dataset(split_name):

    dataset_path = os.path.join(base_path, split_name)

    classes = os.listdir(dataset_path)

    print("\n" + "=" * 50)
    print(f"{split_name.upper()} DATASET")
    print("=" * 50)

    print("Number of classes:", len(classes))

    total_images = 0

    print("\nImages per class:\n")

    for class_name in sorted(classes):

        class_path = os.path.join(dataset_path, class_name)

        # Count only image files
        images = [
            img for img in os.listdir(class_path)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        count = len(images)

        total_images += count

        print(f"{class_name}: {count}")

    print("\nTotal images:", total_images)


# Analyze all splits
analyze_dataset("train")
analyze_dataset("val")
analyze_dataset("test")