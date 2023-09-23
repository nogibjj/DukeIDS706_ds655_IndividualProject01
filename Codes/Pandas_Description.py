#  IDS 706 Individual Project assignment
#  Code for generating summary statistics using pandas
# import pandas as pd
import os
import datetime
import tabulatehelper as th


def PandasDesc(df):
    """Code to return a summary of a dataframe and save it to a file"""
    if os.path.isfile("./Outputs/Summary.md"):
        os.remove("./Outputs/Summary.md")
    f = open("./Outputs/Summary.md", "w", encoding="utf-8")
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
