import joblib
from sklearn.ensemble import RandomForestClassifier


def load_model(filename="api/models/iris.joblib") -> RandomForestClassifier:
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model


def predict(model: RandomForestClassifier, features: dict) -> str:
    feature_list = [
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"],
    ]
    prediction = model.predict([feature_list])[0]
    return ["setosa", "versicolor", "virginica"][prediction]
