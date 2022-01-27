import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
#import file from your computer
from google.colab import files
uploaded = files.upload()
#dataset: name of your dataset. this reads an xlsx file
import io
dataset = pd.read_excel(io.BytesIO(uploaded[' .xlsx']))
# Dataset is now stored in a Pandas Dataframe
#show the first 5 rows
dataset.head()
#give values for x and y axes, color scheme
scatter_plot = px.scatter(dataset, x='', y='', color='', width=800, height=600)
scatter_plot.update_xaxes(tickvals=[ ], showticklabels=True)
scatter_plot.update_yaxes(tickvals=[ ])
scatter_plot.show()
