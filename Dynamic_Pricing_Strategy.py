import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("dynamic_pricing.csv")
print(data.head())

print(data.describe())

#Now let’s have a look at the relationship between expected ride duration and the historical cost of the ride:

fig = px.scatter(data, x='Expected_Ride_Duration', 
                 y='Historical_Cost_of_Ride',
                 title='Expected Ride Duration vs. Historical Cost of Ride', 
                 trendline='ols')
fig.show()

#Now let’s have a look at the distribution of the historical cost of rides based on the vehicle type:

fig = px.box(data, x='Vehicle_Type', 
             y='Historical_Cost_of_Ride',
             title='Historical Cost of Ride Distribution by Vehicle Type')
fig.show()

#Now let’s have a look at the correlation matrix:

corr_matrix = data.corr()

fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, 
                                x=corr_matrix.columns, 
                                y=corr_matrix.columns,
                                colorscale='Viridis'))
fig.update_layout(title='Correlation Matrix')
fig.show()

