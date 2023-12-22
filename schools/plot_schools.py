import pandas as pd
import plotly.graph_objects as go
import pyautogui

screen_width, screen_height = pyautogui.size()

token = 'pk.eyJ1IjoiZ2xmb3N0ZXIiLCJhIjoiY2xxZXNoNHo1MHFsZjJqb2sxbXBsY3hxdSJ9.hL9lfFDxUKWNAPcut9ar-A'

df = pd.read_csv("Baltimore_City_Schools_Lon_Lat_Added.csv")
# df.dropna(
#     axis=0,
#     how='any',
#     subset=None,
#     inplace=True
# )

latitudes = df["lat"]
longitudes = df["lon"]
names = df['name']
types = df['type']
grades = df['class']

customized_data = types + '    ' + grades

fig = go.Figure()

fig.add_trace(go.Scattermapbox(
    lat=latitudes,
    lon=longitudes,
    name='School',
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=17,
        color='rgb(50, 168, 139)',
        opacity=0.7
    ),
    hoverinfo='text',
    text=names,
    customdata= customized_data,
    hovertemplate=
    "<b>%{text}</b><br>" +
    "%{customdata}" +
    "<extra></extra>"
))

fig.update_layout(
    title='Map of Schools in Baltimore City',
    autosize=True,
    hovermode='closest',
    showlegend=True,
    mapbox=dict(
        accesstoken = token,
        center=dict(
            lat=39.3,
            lon=-76.6
        ),
        bearing=0,
        pitch=0,
        zoom=11,
        style='light'
    ),
    
)

fig.show()

