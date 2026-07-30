import pandas as pd

# Load the dataset
data = pd.read_csv("workload_data.csv")

# Display the dataset
print("Dataset:\n")
print(data)

# Initialize the hypothesis
hypothesis = None

# Iterate through each training example
for i, row in data.iterrows():

    # Consider only positive examples
    if row["High-Performance Edge"] == "Yes":

        # Get only the attribute values (excluding target column)
        instance = row[:-1].tolist()

        # Initialize hypothesis with the first positive example
        if hypothesis is None:
            hypothesis = instance.copy()

        else:
            # Generalize the hypothesis
            for j in range(len(hypothesis)):
                if hypothesis[j] != instance[j]:
                    hypothesis[j] = "?"

        # Print hypothesis after processing each positive example
        print(f"\nAfter processing Positive Example {i+1}:")
        print(hypothesis)

# Display final hypothesis
print("\nFinal Specific Hypothesis:")
print(hypothesis)