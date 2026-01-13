import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(64,64,3), n_size=4, n_defect=5):
    base = tf.keras.applications.MobileNetV2(
        input_shape=input_shape,
        include_top=False,
        weights=None,
        alpha=0.5
    )

    x = layers.GlobalAveragePooling2D()(base.output)

    size_head = layers.Dense(128, activation="relu")(x)
    size_out = layers.Dense(n_size, activation="softmax", name="size")(size_head)

    defect_head = layers.Dense(128, activation="relu")(x)
    defect_out = layers.Dense(n_defect, activation="softmax", name="defect")(defect_head)

    model = models.Model(inputs=base.input, outputs=[size_out, defect_out])
    return model
