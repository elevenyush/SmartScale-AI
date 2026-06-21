import pandas as pd
from sklearn.linear_model import LinearRegression
import math

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

month = int(input("Enter month (1-12): "))
day_of_week = int(input("Enter day (1=Mon ... 7=Sun): "))
weekend = int(input("Is it a weekend? (1=Yes, 0=No): "))
holiday = int(input("Is it a holiday? (1=Yes, 0=No): "))
sale = int(input("Is a sale running? (1=Yes, 0=No): "))

input_data = pd.DataFrame({
    "month": [month],
    "day_of_week": [day_of_week],
    "is_weekend": [weekend],
    "is_holiday": [holiday],
    "sale_running": [sale]
})

prediction = model.predict(input_data)

print("\nPredicted Traffic:")
print(round(prediction[0]))

servers_needed = math.ceil(prediction[0] / 5000)

print("\nRecommended Servers:")
print(servers_needed)