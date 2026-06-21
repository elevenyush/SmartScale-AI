import pandas as pd
import random

rows = []

for day in range(1, 366):

    month = random.randint(1, 12)

    day_of_week = random.randint(1, 7)

    is_weekend = 1 if day_of_week >= 6 else 0

    is_holiday = 1 if random.random() < 0.05 else 0

    sale_running = 1 if random.random() < 0.10 else 0

    visitors = 5000

    if is_weekend:
        visitors += 2500

    if is_holiday:
        visitors += 5000

    if sale_running:
        visitors += 6000

    visitors += random.randint(-500, 500)

    rows.append([
        month,
        day_of_week,
        is_weekend,
        is_holiday,
        sale_running,
        visitors
    ])

data = pd.DataFrame(
    rows,
    columns=[
        "month",
        "day_of_week",
        "is_weekend",
        "is_holiday",
        "sale_running",
        "visitors"
    ]
)

data.to_csv(
    "data/traffic_data.csv",
    index=False
)

print("Dataset Created Successfully!")
print("Rows:", len(data))