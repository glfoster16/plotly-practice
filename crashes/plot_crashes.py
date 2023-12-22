import pandas as pd
import plotly.graph_objects as go
import pyautogui
import os

screen_width, screen_height = pyautogui.size()

token = 'pk.eyJ1IjoiZ2xmb3N0ZXIiLCJhIjoiY2xxZXNoNHo1MHFsZjJqb2sxbXBsY3hxdSJ9.hL9lfFDxUKWNAPcut9ar-A'

df = pd.read_csv("CrashMap_data.csv")
# df.dropna(
#     axis=0,
#     how='any',
#     subset=None,
#     inplace=True
# )

latitudes = df["Latitude (generated)"]
longitudes = df["Longitude (generated)"]


fig = go.Figure()


fig.add_trace(go.Scattermapbox(
    lat=latitudes,
    lon=longitudes,
    name ="Crash",
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=17,
        color='rgb(255, 0, 0)',
        opacity=0.7
    ),
    hoverinfo='text',
))

fig.update_layout(
    title='Map of Crashes in Baltimore City',
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



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PLOTLY EXPRESS TESTING


# color_scale = [(0, 'orange'), (1,'red')]

# fig = px.scatter_mapbox(df, 
#                         lat="latitude",
#                         lon="longitude", 
#                         hover_name="storename", 
#                         hover_data={"address":True, "renovationincentiveelig":False, "latitude":False, "longitude":False},
#                         title="Locations of Baltimore Grocery Stores",
#                         color_continuous_scale=color_scale,
#                         zoom=8,
#                         color="renovationincentiveelig",
#                         width=screen_width,
#                         height=screen_height)

# fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






