
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv("dataset/processed_crowd_data.csv")

# Create output folder
os.makedirs("notebooks/outputs", exist_ok=True)

# GRAPH 1: Average crowd count by location
location_data = df.groupby(
    "location"
)["crowd_count"].mean()

location_data.plot(
    kind="bar",
    title="Average Crowd Count by Location",
    xlabel="Location",
    ylabel="Average Crowd Count"
)

plt.tight_layout()
plt.savefig("notebooks/outputs/location_crowd.png")
plt.show()
plt.close()

# GRAPH 2: Average crowd count by hour
hour_data = df.groupby(
    "hour"
)["crowd_count"].mean()

hour_data.plot(
    kind="line",
    marker="o",
    title="Crowd Count by Hour",
    xlabel="Hour of Day",
    ylabel="Average Crowd Count"
)

plt.xticks(range(24))
plt.tight_layout()
plt.savefig("notebooks/outputs/hourly_crowd.png")
plt.show()
plt.close()

# GRAPH 3: Crowd density distribution
density_data = df["crowd_density"].value_counts()

density_data.plot(
    kind="bar",
    title="Crowd Density Distribution",
    xlabel="Density Level",
    ylabel="Number of Records"
)

plt.tight_layout()
plt.savefig("notebooks/outputs/density_distribution.png")
plt.show()
plt.close()

print("All graphs generated successfully!")
