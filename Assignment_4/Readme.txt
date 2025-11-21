Weather Data Visualizer – Rajvir
-----------------------------------
Project Overview
This project analyzes real weather data using Python. It includes data loading, cleaning, statistical analysis, grouping, and visualization. The objective is to observe temperature, humidity, pressure, and wind patterns over several years.
Dataset
The dataset used is: weather.csv
Columns:
- date
- temperature
- humidity
- wind_speed
- meanpressure
Total rows: 1576
Tools Used
- Python 3
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook or Python script
Features
1. Data Loading
   Loads the CSV file and prints the head, info, and descriptive statistics.
2. Data Cleaning
   Converts date to datetime format, sorts data, and handles missing values.
3. Statistical Analysis
   Computes daily, monthly, and yearly statistics using Pandas and NumPy.
4. Visualizations
   Produces the following charts:
   - Temperature trend
   - Humidity trend
   - Scatter plot of humidity vs temperature
   - Combined subplots
   All charts are saved as PNG files.
5. Export
   Saves the cleaned dataset as cleaned_weather.csv
   Saves all generated plots in PNG format
   Saves final summary as report.md
How to Run
Use the following command:
python Assignment_4.py
This will clean the data, show statistics, and generate all charts.
Output Files
- cleaned_weather.csv
- temperature_trend.png
- humidity_trend.png
- scatter_temp_humidity.png
- combined_plots.png
- report.md
Author

Rajvir
