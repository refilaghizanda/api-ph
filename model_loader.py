import tensorflow as tf
from google.cloud import storage
import numpy as np
import os

BUCKET_NAME = "bucket-model-daerah"
MODEL_PATHS = {
    "model1": "models/https://storage.googleapis.com/bucket-model-daerah/models/model_ambon.h5",
    "model2": "models/https://storage.googleapis.com/bucket-model-daerah/models/model_balikpapan.h5",
    "model3": "models/https://storage.googleapis.com/bucket-model-daerah/models/model_banda_aceh.h5",
    "model4": "models/https://storage.googleapis.com/bucket-model-daerah/models/model_bandar_lampung.h5",
    "model5": "models/https://storage.googleapis.com/bucket-model-daerah/models/model_bandung.h5",
}

def download_model():
    """Download the specified model from GCS."""
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(MODEL_PATH)
    local_model_path = "/tmp/model.h5"
    blob.download_to_filename(local_model_path)
    return local_model_path

def load_model():
    """Load the TensorFlow model."""
    local_model_path = download_model()
    model = tf.keras.models.load_model(local_model_path)
    return model

def predict_inflation(model, time_range):
    """Dummy prediction function."""
    # discuss with ML
    dates = ["2024-01", "2024-02"]
    values = [193000, 204000]
    return [{"date": d, "value": v} for d, v in zip(dates, values)]
