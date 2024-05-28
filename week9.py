import numpy as np

# Define the features (sepal length, sepal width, petal length, petal width)
features = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2],
    [5.0, 3.6, 1.4, 0.2],
    [5.4, 3.9, 1.7, 0.4],
    [4.6, 3.4, 1.4, 0.3],
    [5.0, 3.4, 1.5, 0.2],
    [4.4, 2.9, 1.4, 0.2],
    [4.9, 3.1, 1.5, 0.1],
    [5.4, 3.7, 1.5, 0.2],
    [4.8, 3.4, 1.6, 0.2],
    [4.8, 3.0, 1.4, 0.1],
    [4.3, 3.0, 1.1, 0.1],
    [5.8, 4.0, 1.2, 0.2]
])

# Define the target labels (0: setosa, 1: versicolor, 2: virginica)
targets = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Define the target names
target_names = np.array(['setosa'])

# Display the dataset information using print statements
print("Iris Dataset")
print("------------")
print("This is a simplified version of the Iris dataset.")
print("Features:")
print(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
print("Sample data:")
print(features)
print("Target labels:")
print(targets)
print("Target names:")
print(target_names)
