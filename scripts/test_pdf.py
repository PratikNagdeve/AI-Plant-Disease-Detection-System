import os
import sys

# ----------------------------------------------------
# Add Project Root to Python Path
# ----------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# ----------------------------------------------------
# Import PDF Generator
# ----------------------------------------------------

from utils.pdf_generator import generate_pdf

# ----------------------------------------------------
# Sample Prediction Result
# ----------------------------------------------------

sample_result = {
    "crop": "Potato",
    "disease": "Early Blight",
    "severity": "Moderate",
    "confidence": 94.21,
    "description": "Early blight is a fungal disease that causes dark brown lesions on potato leaves, reducing photosynthesis and crop yield if left untreated.",
    "causes": [
        "Warm and humid weather",
        "High soil moisture",
        "Fungal spores in infected crop debris",
        "Poor field sanitation"
    ],
    "treatment": [
        "Apply a recommended fungicide",
        "Remove infected leaves",
        "Avoid overhead irrigation",
        "Monitor plants regularly"
    ],
    "prevention": [
        "Practice crop rotation",
        "Use certified disease-free seeds",
        "Maintain proper plant spacing",
        "Keep the field free from infected debris"
    ]
}

# ----------------------------------------------------
# File Paths
# ----------------------------------------------------

image_path = os.path.join(
    PROJECT_ROOT,
    "data",
    "sample_images",
    "test.png"          # Change if your image name is different
)

output_path = os.path.join(
    PROJECT_ROOT,
    "reports",
    "sample_report.pdf"
)

# ----------------------------------------------------
# Generate PDF
# ----------------------------------------------------

generate_pdf(
    sample_result,
    image_path,
    output_path
)

print("\n✅ PDF generated successfully!")
print(f"📄 Report saved at:\n{output_path}")