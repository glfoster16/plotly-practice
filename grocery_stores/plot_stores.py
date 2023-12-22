import pandas as pd
import plotly.graph_objects as go
import pyautogui
import os

screen_width, screen_height = pyautogui.size()

token = 'pk.eyJ1IjoiZ2xmb3N0ZXIiLCJhIjoiY2xxZXNoNHo1MHFsZjJqb2sxbXBsY3hxdSJ9.hL9lfFDxUKWNAPcut9ar-A'

df = pd.read_csv("Grocery_Stores.csv")
df.dropna(
    axis=0,
    how='any',
    subset=None,
    inplace=True
)

ELIGIBLE_STORES = df[df['renovationincentiveelig'] == "Eligible"]

ELIGIBLE_LATITUDES = ELIGIBLE_STORES.latitude
ELIGIBLE_LONGITUDES = ELIGIBLE_STORES.longitude
ELIGIBLE_STORENAMES = ELIGIBLE_STORES.storename
ELIGIBLE_ADDRESSES = ELIGIBLE_STORES.address


INELIGIBLE_STORES = df[df['renovationincentiveelig'] == "Ineligible"]

INELIGIBLE_LATITUDES = INELIGIBLE_STORES.latitude
INELIGIBLE_LONGITUDES = INELIGIBLE_STORES.longitude
INELIGIBLE_STORENAMES = INELIGIBLE_STORES.storename
INELIGIBLE_ADDRESSES = INELIGIBLE_STORES.address

fig = go.Figure()

fig.add_trace(go.Scattermapbox(
    lat=ELIGIBLE_LATITUDES,
    lon=ELIGIBLE_LONGITUDES,
    name ="Renovation Incentive Eligible",
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=17,
        color='rgb(0, 0, 255)',
        opacity=0.7
    ),
    text=ELIGIBLE_STORENAMES,
    hoverinfo='text',
    customdata=ELIGIBLE_ADDRESSES,
    hovertemplate=
    "<b>%{text}</b><br>" +
    "%{customdata}" +
    "<extra></extra>"
))

fig.add_trace(go.Scattermapbox(
    lat=INELIGIBLE_LATITUDES,
    lon=INELIGIBLE_LONGITUDES,
    name ="Renovation Incentive Ileligible",
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=17,
        color='rgb(255, 0, 0)',
        opacity=0.7
    ),
    text=INELIGIBLE_STORENAMES,
    hoverinfo='text',
    customdata=INELIGIBLE_ADDRESSES,
    hovertemplate=
    "<b>%{text}</b><br>" +
    "%{customdata}" +
    "<extra></extra>"
))

fig.update_layout(
    title='Grocery Store Locations in Baltimore City',
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






