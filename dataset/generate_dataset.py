import pandas as pd
import random
from datetime import date, timedelta

# Make the generated data reproducible
random.seed(42)

# Sample locations in Hyderabad
locations = [
    {
        "location": "Ameerpet",
        "latitude": 17.4375,
        "longitude": 78.4483,
        "area_type": "Commercial",
        "base_crowd": 120
    },
    {
        "location": "Kukatpally",
        "latitude": 17.4849,
        "longitude": 78.4138,
        "area_type": "Residential",
        "base_crowd": 90
    },
    {
        "location": "Gachibowli",
        "latitude": 17.4401,
        "longitude": 78.3489,
        "area_type": "Commercial",
        "base_crowd": 110
    },
    {
        "location": "Miyapur",
        "latitude": 17.4968,
        "longitude": 78.3568,
        "area_type": "Residential",
        "base_crowd": 70
    },
    {
        "location": "Secunderabad",
        "latitude": 17.4399,
        "longitude": 78.4983,
        "area_type": "Transport",
        "base_crowd": 130
    }
]

records = []

# Generate 12 weeks of hourly sample data
end_date = date.today()
start_date = end_date - timedelta(days=83)

record_id = 1
current_date = start_date

while current_date <= end_date:

    for place in locations:

        for hour in range(24):

            # Simulated rush-hour pattern
            if hour in [8, 9, 10, 17, 18, 19]:
                multiplier = 2.0
            elif hour in [11, 12, 13, 14, 15, 16]:
                multiplier = 1.4
            elif hour in [0, 1, 2, 3, 4, 5]:
                multiplier = 0.3
            else:
                multiplier = 0.8

            # Simulated weekend variation
            if current_date.weekday() >= 5:
                multiplier *= 1.2

            # Generate sample crowd count
            crowd_count = int(
                place["base_crowd"] * multiplier
                + random.randint(-20, 20)
            )

            crowd_count = max(0, crowd_count)

            # Assign sample density category
            if crowd_count < 100:
                density = "Low"
            elif crowd_count < 250:
                density = "Moderate"
            else:
                density = "High"

            records.append({
                "record_id": record_id,
                "date": current_date,
                "location": place["location"],
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "day_of_week": current_date.strftime("%A"),
                "hour": hour,
                "area_type": place["area_type"],
                "crowd_count": crowd_count,
                "crowd_density": density,
                "data_source": "Simulated"
            })

            record_id += 1

    current_date += timedelta(days=1)

# Convert records into a DataFrame
df = pd.DataFrame(records)

# Save dataset
df.to_csv(
    "dataset/simulated_crowd_data.csv",
    index=False
)

print("Dataset generated successfully!")
print("Total records:", len(df))
print(df.head())

