#   Importing Packages
import matplotlib.pyplot as plt


#  Creating a function to build a scatterplot for the Iris dataset
def PandasPlot(df):
    groups = df.groupby("species")
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(
            group.sepal_length,
            group.sepal_width,
            marker="o",
            linestyle="",
            ms=12,
            label=name,
        )
    ax.legend()
    fig.suptitle(
        "Distribution of Sepal Length and Sepal Width across different species"
    )
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.savefig("./Resources/plot image.png")
    plt.show()
