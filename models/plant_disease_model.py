import tensorflow as tf


NUM_CLASSES = 15


def create_model():

    base_model = tf.keras.applications.EfficientNetB0(
        weights="imagenet",
        include_top=False,
        input_shape=(224, 224, 3)
    )


    # Freeze pretrained layers initially
    base_model.trainable = False


    model = tf.keras.Sequential(
        [
            base_model,

            tf.keras.layers.GlobalAveragePooling2D(),

            tf.keras.layers.Dense(
                256,
                activation="relu"
            ),

            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.Dense(
                NUM_CLASSES,
                activation="softmax"
            )
        ]
    )


    return model


if __name__ == "__main__":

    model = create_model()

    model.summary()