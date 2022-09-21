import numpy
import pandas as pd
import matplotlib as plt

data="/Users/sofisch/Downloads/data.pgxseg"

with data as segfile:
      for line in segfile.readlines():
            if "#" not in line:
                  with data as f:
                        f.write(line)


df=pd.DataFrame(data.csv, sep="\t")

print(df)
