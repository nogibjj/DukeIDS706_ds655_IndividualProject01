#  IDS 706 Individual Project assignment
#  Code for plotting the data using pandas
#   Importing Packages
import matplotlib.pyplot as plt
import os
import datetime


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
        "Distribution of Sepal Length and Sepal Width\n generated on - "
        + str(datetime.datetime.now())
    )
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    if os.path.isfile("./Outputs/PlotImage.png.png"):
        os.remove("./Outputs/PlotImage.png")
    plt.savefig("./Outputs/PlotImage.png")
    print("Pasted Plot")
    plt.show()
