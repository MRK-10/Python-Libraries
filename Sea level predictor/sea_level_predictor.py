import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('boilerplate-sea-level-predictor\epa-sea-level.csv')
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit (all data)
    res_all = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(data['Year'].min(), 2051))
    plt.plot(years_extended, res_all.intercept + res_all.slope * years_extended, 'r', label='Best Fit: All Data')

    # Create second line of best fit (from 2000)
    recent = data[data['Year'] >= 2000]
    res_recent = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g', label='Best Fit: 2000+')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()