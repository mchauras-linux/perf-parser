#! /bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import sys

arguments = sys.argv[1:]
if len(arguments) < 2:
    print(f"Usage: {sys.argv[0]} <Coloumn1> <Coloumn2>")
    print("Optional:")
    print("3rd and 4th argument are for data control in which you can tell which values to consider")
    print("Coloumn Name", "Value to be equal")
    print("Optional 5th Argunment to append to title of graph")
    exit(-1)

file_path = 'data.csv'

# Select columns for the graph
x_column = sys.argv[1]
y_column = sys.argv[2]

for i in range(104, 2081, 104):
# Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
# data = data[data[sys.argv[3]] == sys.argv[4]]
    data = data[data['threads'] == i]
# Get the column names from the CSV file
    column_names = data.columns.tolist()
    print("Available columns:", column_names)

# Plot the graph
    # plt.figure(figsize=(10, 10))  # Adjust figure size if needed
    plt.figure()
    plt.scatter(data[x_column], data[y_column])
    plt.title(f"{x_column} vs {y_column} {i} Threads")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    # plt.show()
    plt.savefig(f"graph/bs-vs-{sys.argv[2]}-{i}T.png")
