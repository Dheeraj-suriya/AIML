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

OUTPUT:
Dataset:

  Latency Sensitivity Data Volume RAM Demand Network Bandwidth GPU Required High-Performance Edge
0                High       Large       High         Dedicated          Yes                   Yes
1                High       Small       High            Shared          Yes                    No
2                High       Large       High            Shared          Yes                   Yes
3                 Low       Large     Medium            Shared           No                    No
4                High       Large       High         Dedicated           No                   Yes

After processing Positive Example 1:
['High', 'Large', 'High', 'Dedicated', 'Yes']

After processing Positive Example 3:
['High', 'Large', 'High', '?', 'Yes']

After processing Positive Example 5:
['High', 'Large', 'High', '?', '?']

Final Specific Hypothesis:
