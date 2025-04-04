import pandas as pd

squirrel = pd.read_csv(
    r"day_25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count = squirrel["Primary Fur Color"].value_counts()
print(squirrel_count)

data = pd.DataFrame(squirrel_count)
print(data)
data.to_csv("squirrel_count.csv")
