import numpy as np
import joblib

nlp_pipeline = joblib.load('model/simple_nlp.pkl')

def get_weighted_vehicle_type(text, weight):
    types = ['máy', 'ô tô']

    text_lower = str(text).lower()

    for t in types:
        if t in text_lower:
            weighted_string = (t + " ") * weight
            return text + " " + weighted_string.strip()

    return text


def get_vehicle(text):
    process_text = get_weighted_vehicle_type(text, 8)

    probabilities = nlp_pipeline.predict_proba([process_text])[0]

    top_5_indices = np.argsort(probabilities)[::-1][:5]
    classes = nlp_pipeline.classes_

    list = []

    for i, idx in enumerate(top_5_indices):
        predicted_car = classes[idx]
        list.append(predicted_car)

    return list
