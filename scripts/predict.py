import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from utils.predictor import predict_image


IMAGE_PATH = r"D:\Projects\AI-Plant-Disease-Detection-System\data\sample_images\test.png"

result = predict_image(IMAGE_PATH)

print("=" * 60)
print("PLANT DISEASE DETECTION RESULT")
print("=" * 60)

print(f"Crop       : {result['crop']}")
print(f"Disease    : {result['disease']}")
print(f"Severity   : {result['severity']}")
print(f"Confidence : {result['confidence']}%")

print("\nDescription")
print("-" * 60)
print(result["description"])

print("\nPossible Causes")
print("-" * 60)
for cause in result["causes"]:
    print(f"• {cause}")

print("\nTreatment Recommendations")
print("-" * 60)
for item in result["treatment"]:
    print(f"• {item}")

print("\nPreventive Measures")
print("-" * 60)
for item in result["prevention"]:
    print(f"• {item}")

