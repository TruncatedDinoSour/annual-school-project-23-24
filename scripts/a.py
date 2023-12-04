import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the CSV file
df = pd.read_csv("a.csv")

# Set the color palette
colors = sns.color_palette('pastel')[0:len(df.columns)]

# For each column, create a pie chart
for i, column in enumerate(df.columns):
    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)  # Set larger size and dpi
    df[column].value_counts().plot(
        kind="pie",
        ax=ax,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
    )
    ax.set_ylabel("")
    plt.title(column)
    plt.savefig(
        f"out/{column}_pie_chart.png", dpi=100, transparent=True
    )
    plt.close(fig)
