# visualizations/heatmaps.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/udise_2021_22.csv")

# Heatmap for classroom quality
room_cols = [
    'classrooms_in_good_condition',
    'classrooms_needs_minor_repair',
    'classrooms_needs_major_repair',
    'total_class_rooms'
]

df_room = df[room_cols].copy()
correlation = df_room.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='Blues')
plt.title("Correlation Between Classroom Conditions")
plt.tight_layout()
plt.show()
