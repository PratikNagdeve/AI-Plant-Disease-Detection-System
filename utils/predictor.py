import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

from utils.disease_info import DISEASE_INFO


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "best_model.keras"
)

IMG_SIZE = (224, 224)

CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]


model = tf.keras.models.load_model(MODEL_PATH)


def predict_image(image_path):

    img = image.load_img(
        image_path,
        target_size=IMG_SIZE
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(
        img_array,
        verbose=0
    )

    predicted_index = np.argmax(predictions)

    confidence = float(np.max(predictions))

    predicted_class = CLASS_NAMES[predicted_index]

    info = DISEASE_INFO[predicted_class]

    return {
        "crop": info["crop"],
        "disease": info["display_name"],
        "severity": info["severity"],
        "confidence": round(confidence * 100, 2),
        "description": info["description"],
        "causes": info["causes"],
        "treatment": info["treatment"],
        "prevention": info["prevention"]
    }