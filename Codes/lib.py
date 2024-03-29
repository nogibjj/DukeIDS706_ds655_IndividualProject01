#  IDS 706 Individual Project assignment
#   Importing Packages
import matplotlib.pyplot as plt
import os
import datetime
import tabulatehelper as th


def PandasPlot(df):
    #  Code for plotting the data using pandas
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
    if os.path.isfile("./Outputs/PlotImage.png"):
        os.remove("./Outputs/PlotImage.png")
    print(os.getcwd())
    plt.savefig("./Outputs/PlotImage.png")
    print("Pasted Plot")
    plt.show()


def PandasDescription(df):
    return df.describe()


def PandasDesc(df):
    #   Code to return a summary of a dataframe and save it to a file
    if os.path.isfile("./Outputs/Summary.md"):
        os.remove("./Outputs/Summary.md")
    f = open(
        "./Outputs/Summary.md",
        "w",
        encoding="utf-8",
    )
    f.flush()
    d = df.describe()
    s = d.transpose()
    s["index"] = s.index
    column_to_move = s.pop("index")
    s.insert(0, "column name", column_to_move)
    f.write(th.md_table(s, formats={-1: "c"}))
    f.write("\n\n\n")
    f.write("Generated at: " + str(datetime.datetime.now()))
    f.write("\n\n\n")
    f.write(f"""![Graph]({"PlotImage.png"})""")
    f.write("\n\n\n")
    f.close()
    print("Summary of the dataframe has been saved to Summary.md")
    return df.describe()
