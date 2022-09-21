import numpy
import pandas as pd
data=open("/Users/sofisch/Downloads/data.pgxseg", "r")
data=data.readlines()

data=data[1006:]
df=pd.DataFrame(data)

print(df
      )
