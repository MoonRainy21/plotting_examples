import numpy as np
import pandas as pd


def generate_barplot_data(num_columns=5, min_value=0, max_value=100):
  """
  Generate data for a box plot.

  Parameters:
    num_datasets (int): Number of datasets.
    num_points (int): Number of data points in each dataset.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  data = np.random.randint(min_value, max_value, size=(1, num_columns))
  df = pd.DataFrame(data, columns=[f"Dataset_{i+1}" for i in range(num_columns)])
  return df


def generate_grouped_barplot_data(categories=["X", "Y", "Z"], groups=["A", "B", "C"], min_value=0, max_value=100):
  """
  Generate data for a grouped bar plot.

  Parameters:
    categories (list): List of categories.
    groups (list): List of groups within each category.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  data = np.random.randint(min_value, max_value, size=(len(categories), len(groups)))
  df = pd.DataFrame(data, columns=groups, index=categories)
  return df


def generate_signal_plot_data(
  num_points=100, min_value=0, max_value=100, noise_level=0.1
):
  """
  Generate data for a signal plot.

  Parameters:
    num_points (int): Number of data points in the signal.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.
    noise_level (float): Level of noise to add to the signal.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  x = np.linspace(0, 10, num_points)
  y = np.sin(x) + np.random.normal(scale=noise_level, size=num_points)
  df = pd.DataFrame({"X": x, "Y": y})
  return df

def generate_multiple_signal_plot_data(
  num_points=100, noise_level=0.1
):
  """
  Generate data for a signal plot.

  Parameters:
    num_points (int): Number of data points in the signal.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.
    noise_level (float): Level of noise to add to the signal.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  x = np.linspace(0, 10, num_points)
  y1 = np.sin(x) + np.random.normal(scale=noise_level, size=num_points)
  y2 = np.cos(x) + np.random.normal(scale=noise_level, size=num_points)
  df = pd.DataFrame({"X": x, "Y1": y1, "Y2": y2})
  return df

def generate_scatterplot_data(num_points=100, min_value=0, max_value=100):
  """
  Generate data for a scatter plot.

  Parameters:
    num_points (int): Number of data points.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  x = np.random.randint(min_value, max_value, size=num_points)
  y = np.random.randint(min_value, max_value, size=num_points)
  df = pd.DataFrame({"X": x, "Y": y})
  return df


def generate_histogram_data(num_points=100000, min_value=0, max_value=100):
  """
  Generate data for a histogram.

  Parameters:
    num_points (int): Number of data points.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  data = np.random.normal(loc=(max_value - min_value) / 2, scale=10, size=num_points)
  df = pd.DataFrame(data, columns=["Value"])
  return df


def generate_heatmap_data(rows=5, cols=5, min_value=0, max_value=100):
  """
  Generate data for a heatmap.

  Parameters:
    rows (int): Number of rows in the heatmap.
    cols (int): Number of columns in the heatmap.
    min_value (int): Minimum value for data points.
    max_value (int): Maximum value for data points.

  Returns:
    DataFrame: Pandas DataFrame containing the generated data.
  """
  data = np.random.randint(min_value, max_value, size=(rows, cols))
  df = pd.DataFrame(
    data,
    columns=[f"Column_{i+1}" for i in range(cols)],
    index=[f"Row_{i+1}" for i in range(rows)],
  )
  return df

if __name__=='__main__':
  import os

  generation_functions = [
    generate_histogram_data, generate_barplot_data, generate_grouped_barplot_data,
    generate_heatmap_data, generate_multiple_signal_plot_data, generate_scatterplot_data, 
    generate_signal_plot_data]
  dataset_name = ['histogram', 'barplot', 'grouped_barplot', 'heatmap', 'multiple_signal_plot', 'scatterplot', 'signal_plot']

  os.makedirs('dataset', exist_ok=True)
  for index, generation_function in enumerate(generation_functions):
    data = generation_function()
    data.to_csv(f'dataset/{dataset_name[index]}.csv', index=False)