import pandas as pd

def predict_traffic(
    model,
    month,
    day_of_week,
    weekend,
    holiday,
    sale
):

    input_data = pd.DataFrame({
        "month": [month],
        "day_of_week": [day_of_week],
        "is_weekend": [weekend],
        "is_holiday": [holiday],
        "sale_running": [sale]
    })

    prediction = model.predict(input_data)

    return round(prediction[0])


def forecast_next_7_days(
    model,
    month,
    holiday,
    sale
):

    forecasts = []

    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for day in range(1, 8):

        weekend = 1 if day >= 6 else 0

        input_data = pd.DataFrame({
            "month": [month],
            "day_of_week": [day],
            "is_weekend": [weekend],
            "is_holiday": [holiday],
            "sale_running": [sale]
        })

        prediction = model.predict(input_data)

        forecasts.append({
            "Day": day_names[day - 1],
            "Predicted Traffic": round(prediction[0])
        })

    return pd.DataFrame(forecasts)