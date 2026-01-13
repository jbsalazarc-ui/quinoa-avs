import cv2
import numpy as np
import tensorflow as tf

def preprocess(img):
    img = cv2.resize(img, (64,64))
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def infer(model, roi):
    x = preprocess(roi)
    size_pred, defect_pred = model.predict(x)
    return size_pred, defect_pred
