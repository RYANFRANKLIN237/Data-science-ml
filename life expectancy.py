

import plotly.express as px
import numpy as np

# Choose a year that exists in the dataset
year_to_plot = 2002 

df_full = px.data.gapminder()
df = df_full.query(f"year == {year_to_plot}") 

if df.empty:
    print(f"No data found for the year {year_to_plot}")
else:
    # Calculate the midpoint based on the data for the selected year
    midpoint = np.average(df['lifeExp'], weights=df['pop'])

    fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                     color='lifeExp', hover_data=['iso_alpha'],
                     color_continuous_scale='RdBu',
                     color_continuous_midpoint=midpoint) 
    fig.update_layout(
        title=f'Life Expectancy and Population by Country ({year_to_plot})', 
        margin=dict(t=50, l=25, r=25, b=25)
    )
    fig.show()