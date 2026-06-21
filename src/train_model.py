import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():

    data = pd.read_csv("data/traffic_data.csv")

    X = data[[
        "month",
        "day_of_week",
        "is_weekend",
        "is_holiday",
        "sale_running"
    ]]

    y = data["visitors"]

    model = LinearRegression()

    model.fit(X, y)

    return model