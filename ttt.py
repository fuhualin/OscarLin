
import { ChatOpenAI } from "langchain/chat_models/openai";

import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoDataFrame for Canada
canada = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
canada = canada[canada['name'] == 'Canada']

# Plot the Canada map
fig, ax = plt.subplots(figsize=(10, 8))
canada.plot(ax=ax, color='lightblue', edgecolor='black')

# Set plot title and show the map
plt.title('Map of Canada')
plt.show()