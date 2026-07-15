import os
import tempfile
from datetime import datetime

import streamlit as st
from PIL import Image

from utils.predictor import predict_image
from utils.pdf_generator import generate_pdf

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🌿 Project Information")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Project")

st.sidebar.write("**AI Plant Disease Detection System**")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 Model")

st.sidebar.write("EfficientNet-B0")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Performance")

st.sidebar.metric(
    label="Test Accuracy",
    value="94.21%"
)

st.sidebar.write("**Number of Classes:** 15")

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Dataset")

st.sidebar.write("PlantVillage Dataset")

st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 Developer")

st.sidebar.write("Pratik Nagdeve")

st.sidebar.markdown("---")

st.sidebar.info(
    "Upload a leaf image to identify plant diseases and receive treatment recommendations."
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🌿 AI Plant Disease Detection System")

st.markdown("""
Detect plant diseases using an EfficientNet-B0 deep learning model and receive
disease information, possible causes, treatment recommendations, and preventive measures.
""")

st.divider()

# --------------------------------------------------
# Upload Image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload a Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    # --------------------------------------------------
    # LEFT COLUMN
    # --------------------------------------------------

    with col1:

        st.subheader("🖼 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

        detect = st.button(
            "🔍 Detect Disease",
            use_container_width=True
        )

    # --------------------------------------------------
    # RIGHT COLUMN
    # --------------------------------------------------

    with col2:

        if detect:

            # Save uploaded image temporarily

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".png"
            ) as tmp_file:

                tmp_file.write(uploaded_file.getbuffer())
                temp_path = tmp_file.name

            # Predict

            with st.spinner("Analyzing leaf image..."):

                result = predict_image(temp_path)

            st.success("✅ Disease detection completed!")

            # --------------------------------------------------
            # Generate PDF
            # --------------------------------------------------

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            pdf_filename = f"Plant_Disease_Report_{timestamp}.pdf"

            pdf_path = os.path.join(
                "reports",
                pdf_filename
            )

            generate_pdf(
                result,
                temp_path,
                pdf_path
            )

            with open(pdf_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()

            # --------------------------------------------------
            # Prediction Summary
            # --------------------------------------------------

            st.subheader("Prediction Summary")

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric(
                    "🌱 Crop",
                    result["crop"]
                )

            with metric2:
                st.metric(
                    "🦠 Disease",
                    result["disease"]
                )

            metric3, metric4 = st.columns(2)

            with metric3:
                st.metric(
                    "⚠ Severity",
                    result["severity"]
                )

            with metric4:
                st.metric(
                    "🎯 Confidence",
                    f"{result['confidence']}%"
                )

            st.write("### Confidence Score")

            st.progress(result["confidence"] / 100)

            st.markdown("---")

            # --------------------------------------------------
            # Disease Information
            # --------------------------------------------------

            with st.expander("📖 Description", expanded=True):
                st.write(result["description"])

            with st.expander("🦠 Possible Causes"):
                for cause in result["causes"]:
                    st.write(f"• {cause}")

            with st.expander("💊 Treatment Recommendations"):
                for treatment in result["treatment"]:
                    st.write(f"• {treatment}")

            with st.expander("🛡 Preventive Measures"):
                for prevention in result["prevention"]:
                    st.write(f"• {prevention}")

            st.markdown("---")

            # --------------------------------------------------
            # Download PDF
            # --------------------------------------------------

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name=pdf_filename,
                mime="application/pdf",
                use_container_width=True
            )

else:

    st.info("👆 Upload a plant leaf image to begin disease detection.")