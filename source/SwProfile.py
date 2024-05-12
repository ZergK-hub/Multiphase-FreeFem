import matplotlib.pyplot as plt
import os
import numpy as np

# Get the current working directory
cwd =os.getcwd()+"\\source\\SwData"

# Create a list of all the txt files in the directory
txt_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]
print(txt_files)

# Create a figure and axes
fig, ax = plt.subplots()

# Set the step size
step = 3

# Loop through the txt files
for i, txt_file in enumerate(txt_files):
    # Skip the file if it is not a multiple of the step size
    if i % step != 0:
        continue

    # Read the data from the txt file
    pathind=cwd+"\\"+txt_file
    print(pathind)
    data = np.loadtxt(cwd+"\\"+txt_file, delimiter='\t')

    print(data)

    # Extract the X, Y, and Value columns
    X = data[:, 0]
    Y = data[:, 1]
    Value = data[:, 2]

    # Plot the data
    ax.plot(X, Value, label=txt_file)

# Add a legend
plt.legend()

# Show the plot
plt.show()
