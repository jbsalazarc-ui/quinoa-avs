import tensorflow as tf

def export_tflite(model, path="model.tflite"):
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    with open(path, "wb") as f:
        f.write(tflite_model)
