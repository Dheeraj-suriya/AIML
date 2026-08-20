# Candidate Elimination Algorithm
# Bank Loan Dataset

# Training data
data = [
    ["MP", "NA", "Bachelor", "Employed", "Online", "Y"],
    ["MP", "Savings", "College", "Unemployed", "Offline", "N"],
    ["MP", "Savings", "Bachelor", "Employed", "Online", "Y"],
    ["MH", "Current", "Master", "Employed", "Online", "N"],
    ["MP", "NA", "College", "Employed", "Online", "Y"],
    ["MP", "Savings", "College", "Unemployed", "Online", "Y"],
    ["MP", "NA", "Master", "Unemployed", "Offline", "N"]
]

# Separate attributes and target
X = [row[:-1] for row in data]
Y = [row[-1] for row in data]

# Initial Specific and General hypotheses
S = ["Ø", "Ø", "Ø", "Ø", "Ø"]
G = [["?", "?", "?", "?", "?"]]


# Candidate Elimination
for i in range(len(X)):

    example = X[i]
    target = Y[i]

    print("\nExample:", example, "=>", target)

    if target == "Y":

        # Generalize S
        for j in range(len(S)):

            if S[j] == "Ø":
                S[j] = example[j]

            elif S[j] != example[j]:
                S[j] = "?"

        # Remove inconsistent hypotheses from G
        G = [
            g for g in G
            if all(g[j] == "?" or g[j] == example[j] for j in range(len(g)))
        ]

    else:

        # Specialize G for negative example
        new_G = []

        for g in G:

            if all(g[j] == "?" or g[j] == example[j]
                   for j in range(len(g))):

                for j in range(len(g)):

                    if S[j] != "?" and S[j] != "Ø":
                        if S[j] != example[j]:
                            new_hypothesis = g.copy()
                            new_hypothesis[j] = S[j]

                            if new_hypothesis not in new_G:
                                new_G.append(new_hypothesis)

            else:
                new_G.append(g)

        G = new_G

    print("Specific Hypothesis:", S)
    print("General Hypothesis:", G)


# Final hypothesis
print("\n-----------------------------")
print("Final Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
print(G)


# Unseen example
new_example = ["MP", "Current", "Bachelor", "Unemployed", "Online"]

# Classification
if all(S[i] == "?" or S[i] == new_example[i] for i in range(len(S))):
    print("\nUnseen Example:", new_example)
    print("Prediction: Y")
    print("Decision: Loan should be given.")
else:
    print("\nUnseen Example:", new_example)
    print("Prediction: N")
    print("Decision: Loan should NOT be given.")


#OUTPUT:
'''
Example: ['MP', 'NA', 'Bachelor', 'Employed', 'Online'] => Y
Specific Hypothesis: ['MP', 'NA', 'Bachelor', 'Employed', 'Online']
General Hypothesis: [['?', '?', '?', '?', '?']]

Example: ['MP', 'Savings', 'College', 'Unemployed', 'Offline'] => N
Specific Hypothesis: ['MP', 'NA', 'Bachelor', 'Employed', 'Online']
General Hypothesis: [['?', 'NA', '?', '?', '?'], ['?', '?', 'Bachelor', '?', '?'], ['?', '?', '?', 'Employed', '?'], ['?', '?', '?', '?', 'Online']]

Example: ['MP', 'Savings', 'Bachelor', 'Employed', 'Online'] => Y
Specific Hypothesis: ['MP', '?', 'Bachelor', 'Employed', 'Online']
General Hypothesis: [['?', '?', 'Bachelor', '?', '?'], ['?', '?', '?', 'Employed', '?'], ['?', '?', '?', '?', 'Online']]

Example: ['MH', 'Current', 'Master', 'Employed', 'Online'] => N
Specific Hypothesis: ['MP', '?', 'Bachelor', 'Employed', 'Online']
General Hypothesis: [['?', '?', 'Bachelor', '?', '?'], ['MP', '?', '?', 'Employed', '?'], ['?', '?', 'Bachelor', 'Employed', '?'], ['MP', '?', '?', '?', 'Online'], ['?', '?', 'Bachelor', '?', 'Online']]

Example: ['MP', 'NA', 'College', 'Employed', 'Online'] => Y
Specific Hypothesis: ['MP', '?', '?', 'Employed', 'Online']
General Hypothesis: [['MP', '?', '?', 'Employed', '?'], ['MP', '?', '?', '?', 'Online']]

Example: ['MP', 'Savings', 'College', 'Unemployed', 'Online'] => Y
Specific Hypothesis: ['MP', '?', '?', '?', 'Online']
General Hypothesis: [['MP', '?', '?', '?', 'Online']]

Example: ['MP', 'NA', 'Master', 'Unemployed', 'Offline'] => N
Specific Hypothesis: ['MP', '?', '?', '?', 'Online']
General Hypothesis: [['MP', '?', '?', '?', 'Online']]

-----------------------------
Final Specific Hypothesis:
['MP', '?', '?', '?', 'Online']

Final General Hypothesis:
[['MP', '?', '?', '?', 'Online']]

Unseen Example: ['MP', 'Current', 'Bachelor', 'Unemployed', 'Online']
Prediction: Y
Decision: Loan should be given.
'''