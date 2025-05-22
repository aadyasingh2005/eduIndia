# dashboard/app.py

import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from visualizations.linegraph import plot_schools_established_over_years


st.set_page_config(page_title="Bangalore Urban School Data", layout="wide")

# Load dataset
df = pd.read_csv("..\data\Bengaluru_Urban_North_Facilities.csv")

st.title("Bengaluru Urban School Data Visualisation (using USIDE+ data)")

# Sidebar filters
st.sidebar.header("Filter by")
infra_option = st.sidebar.selectbox("Infrastructure Element", df.columns[2:])

# --- Bar Chart ---
st.subheader(f"Distribution of {infra_option.replace('_', ' ').title()}")
fig_bar = px.histogram(df, x=infra_option)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Heatmap for Classroom Conditions ---
st.subheader("Classroom Condition Correlation Heatmap")

room_cols = [
    'classrooms_in_good_condition',
    'classrooms_needs_minor_repair',
    'classrooms_needs_major_repair',
    'total_class_rooms'
]

if all(col in df.columns for col in room_cols):
    df_room = df[room_cols].copy()
    correlation = df_room.corr()

    fig_heatmap, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='Blues', ax=ax)
    st.pyplot(fig_heatmap)
else:
    st.warning("One or more classroom condition columns not found in dataset.")

# --- Scatter Plot Section ---
st.subheader("Scatter Plot Between Infrastructure Features")

infra_cols = df.columns[2:]  # assuming first two are ID & school name/district

col1, col2 = st.columns(2)
x_feature = col1.selectbox("X-axis Feature", infra_cols, index=0)
y_feature = col2.selectbox("Y-axis Feature", infra_cols, index=1)

# Optional third variable for color
color_by = st.selectbox("Color by (optional)", [None] + list(infra_cols))

st.markdown(f"Scatter Plot: **{x_feature}** vs **{y_feature}**")

fig_scatter = px.scatter(
    df,
    x=x_feature,
    y=y_feature,
    color=color_by if color_by else None,
    size_max=10,
    opacity=0.7,
    title=f"{x_feature} vs {y_feature}",
    template="plotly_white"
)

st.plotly_chart(fig_scatter, use_container_width=True)

df2=pd.read_csv("../data/Bengaluru_Urban_North_Profile_Part1.csv")
# --- Line Graph Section: School Establishment Trends ---
st.subheader("Number of Schools Established Over Time")

if 'year_of_establishment' in df2.columns:
    fig_line = plot_schools_established_over_years(df2)
    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.warning("The dataset does not contain 'year_of_establishment'.")

# Dynamic Box Plot Section
st.subheader("Custom Box Plot")

num_cols = df2.select_dtypes(include='number').columns.tolist()
cat_cols = df2.select_dtypes(include='object').columns.tolist()

box_y = st.selectbox("Select numerical variable (Y-axis)", num_cols)
box_x = st.selectbox("Select categorical variable (X-axis)", cat_cols)

fig_custom_box = px.box(
    df2,
    x=box_x,
    y=box_y,
    title=f"Box Plot: {box_y} by {box_x}",
    template="plotly_white"
)

st.plotly_chart(fig_custom_box, use_container_width=True)
