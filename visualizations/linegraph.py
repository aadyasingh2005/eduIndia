import pandas as pd
import plotly.express as px

def plot_schools_established_over_years(df):
    df['year_of_establishment'] = pd.to_numeric(df['year_of_establishment'], errors='coerce')
    df = df.dropna(subset=['year_of_establishment'])

    year_counts = df['year_of_establishment'].astype(int).value_counts().sort_index()
    df_yearly = pd.DataFrame({
        "Year": year_counts.index,
        "Number of Schools": year_counts.values
    })

    fig = px.line(
        df_yearly,
        x="Year",
        y="Number of Schools",
        markers=True,
        title="Schools Established Per Year",
        labels={"Number of Schools": "Count", "Year": "Year"},
        template="plotly_white"
    )

    return fig
