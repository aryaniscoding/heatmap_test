from flask import Flask, render_template, jsonify
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Sample dataset: Crop demand vs. supply in different states
data = {
    "State": ["Maharashtra", "Punjab", "Karnataka", "Gujarat", "UP"],
    "Wheat Demand": [500, 600, 450, 480, 700],
    "Wheat Supply": [520, 580, 470, 500, 680],
    "Rice Demand": [700, 800, 600, 750, 900],
    "Rice Supply": [690, 820, 590, 740, 910],
}

df = pd.DataFrame(data)

# Convert data into long format for heatmap
df_melted = df.melt(id_vars=["State"], var_name="Crop_Type", value_name="Quantity")

# Create heatmap figure
fig = px.density_heatmap(df_melted, x="Crop_Type", y="State", z="Quantity", color_continuous_scale="Viridis")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/heatmap')
def heatmap():
    return render_template("heatmap.html")

@app.route('/heatmap_data')
def heatmap_data():
    return jsonify(fig.to_json())  # Send Plotly figure data as JSON

if __name__ == '__main__':
    app.run(debug=True)
