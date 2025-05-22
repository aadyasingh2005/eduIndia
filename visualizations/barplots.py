# visualizations/barplots.py

import pandas as pd
import plotly.express as px

df = pd.read_csv("..\data\Bengaluru_Urban_North_Facilities.csv")

# Barplot for drinking water availability
fig = px.histogram(df, x="drinking_water_available", title="Drinking Water Availability in Schools")
fig.update_layout(xaxis_title="Available (1: Yes, 2: No, 3: NA)", yaxis_title="Number of Schools")
fig.show()

# Barplot for infrastructure availability
infra_cols = [
    'library_availability', 'playground_available',
    'medical_checkups', 'electricity_availability',
    'internet', 'dth'
]

for col in infra_cols:
    fig = px.histogram(df, x=col, title=f"{col.replace('_', ' ').title()} Distribution")
    fig.show()
