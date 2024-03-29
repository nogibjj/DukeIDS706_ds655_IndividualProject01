#   IDS 706 Individual Project assignment -
#   Code for testing our template using pandas
import pandas as pd
import sys

sys.path.insert(0, "./Codes/")
from lib import PandasDesc  # noqa: E402
from lib import PandasPlot  # noqa: E402


def test_Pandas_Lib():
    #   Reading Source Data from the Github Link
    # sys.path.remove("./Codes")
    DataSource_Link = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv"
    data_s = pd.read_csv(DataSource_Link)
    df_s = pd.DataFrame(data_s)
    PandasPlot(df_s)

    #   Reading the Reference Data from the Resources Folder
    DataReference_Link = "./Resources/Iris_Data.csv"
    data_r = pd.read_csv(DataReference_Link)
    df_r = pd.DataFrame(data_r)

    assert PandasDesc(df_r).equals(df_s.describe())


if __name__ == "__main__":
    test_Pandas_Lib()
