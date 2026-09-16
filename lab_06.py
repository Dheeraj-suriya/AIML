import pandas as pd
import matplotlib.pyplot as plt
import math

# ---------------------------------------------------------
# 1. Create the dataset
# ---------------------------------------------------------

data = {
    'Outlook': [
        'Sunny', 'Sunny', 'Overcast', 'Rain',
        'Rain', 'Rain', 'Overcast', 'Sunny',
        'Sunny', 'Rain', 'Sunny', 'Overcast',
        'Overcast', 'Rain'
    ],

    'Temperature': [
        'Hot', 'Hot', 'Hot', 'Mild',
        'Cool', 'Cool', 'Cool', 'Mild',
        'Cool', 'Mild', 'Mild', 'Mild',
        'Hot', 'Mild'
    ],

    'Humidity': [
        'High', 'High', 'High', 'High',
        'Normal', 'Normal', 'Normal', 'High',
        'Normal', 'Normal', 'Normal', 'High',
        'Normal', 'High'
    ],

    'Wind': [
        'Weak', 'Strong', 'Weak', 'Weak',
        'Weak', 'Strong', 'Strong', 'Weak',
        'Weak', 'Weak', 'Strong', 'Strong',
        'Weak', 'Strong'
    ],

    'Play Tennis': [
        'No', 'No', 'Yes', 'Yes',
        'Yes', 'No', 'Yes', 'No',
        'Yes', 'Yes', 'Yes', 'Yes',
        'Yes', 'No'
    ]
}

df = pd.DataFrame(data)

print("========== DATASET ==========")
print(df)


# ---------------------------------------------------------
# 2. Entropy Function
# ---------------------------------------------------------

def entropy(data):
    target = data['Play Tennis']
    counts = target.value_counts()

    total = len(target)
    result = 0

    for count in counts:
        probability = count / total

        if probability > 0:
            result -= probability * math.log2(probability)

    return result


# ---------------------------------------------------------
# 3. Information Gain Function
# ---------------------------------------------------------

def information_gain(data, attribute):

    total_entropy = entropy(data)

    values = data[attribute].unique()

    weighted_entropy = 0

    for value in values:

        subset = data[data[attribute] == value]

        weight = len(subset) / len(data)

        weighted_entropy += weight * entropy(subset)

    gain = total_entropy - weighted_entropy

    return gain


# ---------------------------------------------------------
# 4. Calculate Information Gain
# ---------------------------------------------------------

attributes = [
    'Outlook',
    'Temperature',
    'Humidity',
    'Wind'
]

print("\n========== ENTROPY ==========")

print(f"Total Entropy: {entropy(df):.3f}")


print("\n========== INFORMATION GAIN ==========")

for attribute in attributes:

    gain = information_gain(df, attribute)

    print(f"{attribute}: {gain:.3f}")


# ---------------------------------------------------------
# 5. ID3 Algorithm
# ---------------------------------------------------------

def id3(data, attributes):

    # If all examples belong to the same class
    if len(data['Play Tennis'].unique()) == 1:

        return data['Play Tennis'].iloc[0]

    # If no attributes remain
    if len(attributes) == 0:

        return data['Play Tennis'].mode()[0]

    # Find attribute with highest information gain
    gains = {}

    for attribute in attributes:

        gains[attribute] = information_gain(data, attribute)

    best_attribute = max(gains, key=gains.get)

    tree = {
        best_attribute: {}
    }

    # Create branches
    for value in data[best_attribute].unique():

        subset = data[data[best_attribute] == value]

        remaining_attributes = [
            attr for attr in attributes
            if attr != best_attribute
        ]

        subtree = id3(subset, remaining_attributes)

        tree[best_attribute][value] = subtree

    return tree


# ---------------------------------------------------------
# 6. Build the Decision Tree
# ---------------------------------------------------------

tree = id3(df, attributes)

print("\n========== ID3 DECISION TREE ==========")

print(tree)


# ---------------------------------------------------------
# 7. Display Tree in Text Format
# ---------------------------------------------------------

def print_tree(tree, indent=""):

    if not isinstance(tree, dict):

        print(indent + "→ " + tree)

        return

    attribute = list(tree.keys())[0]

    for value, subtree in tree[attribute].items():

        print(indent + attribute + " = " + value)

        print_tree(subtree, indent + "    ")


print("\n========== TREE STRUCTURE ==========")

print_tree(tree)


# ---------------------------------------------------------
# 8. Draw a Clean Decision Tree
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 8))

ax.axis("off")

# Node positions
positions = {
    "root": (0.50, 0.88),

    "sunny": (0.20, 0.65),
    "overcast": (0.50, 0.65),
    "rain": (0.80, 0.65),

    "sunny_high": (0.10, 0.38),
    "sunny_normal": (0.30, 0.38),

    "rain_weak": (0.70, 0.38),
    "rain_strong": (0.90, 0.38),

    "no1": (0.10, 0.12),
    "yes1": (0.30, 0.12),

    "yes2": (0.70, 0.12),
    "no2": (0.90, 0.12)
}


# ---------------------------------------------------------
# Function to draw nodes
# ---------------------------------------------------------

def draw_node(x, y, text, node_type="decision"):

    if node_type == "decision":

        bbox = dict(
            boxstyle="round,pad=0.5",
            edgecolor="black",
            facecolor="lightblue"
        )

    elif node_type == "yes":

        bbox = dict(
            boxstyle="round,pad=0.5",
            edgecolor="black",
            facecolor="lightgreen"
        )

    else:

        bbox = dict(
            boxstyle="round,pad=0.5",
            edgecolor="black",
            facecolor="lightcoral"
        )

    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=12,
        bbox=bbox
    )


# ---------------------------------------------------------
# Function to draw arrows
# ---------------------------------------------------------

def draw_arrow(start, end, label):

    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle="->",
            lw=1.5
        )
    )

    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2

    ax.text(
        mid_x,
        mid_y + 0.025,
        label,
        fontsize=11,
        ha="center"
    )


# ---------------------------------------------------------
# Draw nodes
# ---------------------------------------------------------

draw_node(
    *positions["root"],
    "Outlook",
    "decision"
)

draw_node(
    *positions["sunny"],
    "Humidity",
    "decision"
)

draw_node(
    *positions["overcast"],
    "Yes",
    "yes"
)

draw_node(
    *positions["rain"],
    "Wind",
    "decision"
)

draw_node(
    *positions["sunny_high"],
    "No",
    "no"
)

draw_node(
    *positions["sunny_normal"],
    "Yes",
    "yes"
)

draw_node(
    *positions["rain_weak"],
    "Yes",
    "yes"
)

draw_node(
    *positions["rain_strong"],
    "No",
    "no"
)


# ---------------------------------------------------------
# Draw arrows
# ---------------------------------------------------------

draw_arrow(
    positions["root"],
    positions["sunny"],
    "Sunny"
)

draw_arrow(
    positions["root"],
    positions["overcast"],
    "Overcast"
)

draw_arrow(
    positions["root"],
    positions["rain"],
    "Rain"
)

draw_arrow(
    positions["sunny"],
    positions["sunny_high"],
    "High"
)

draw_arrow(
    positions["sunny"],
    positions["sunny_normal"],
    "Normal"
)

draw_arrow(
    positions["rain"],
    positions["rain_weak"],
    "Weak"
)

draw_arrow(
    positions["rain"],
    positions["rain_strong"],
    "Strong"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

plt.title(
    "ID3 Decision Tree - Play Tennis",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.show()
