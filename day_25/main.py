
import csv

# with open(r"C:\Users\Suhail.DESKTOP-0CIIIA7\OneDrive\Desktop\python_prgms\Course\100 days python\day_25\wheather.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if row[1] != "temp":
#             temperatures.append(int(temp))

#     print(temperatures)

import pandas
data = pandas.read_csv("day_25\wheather.csv")
print(data)
print(data["temp"])

# pandas has two type of data type: series and dataframe
# every single column is series
# whole table is dataframe

data_dict = data.to_dict()
print(data_dict)


# convert the series into list
all_temp = data["temp"].to_list()

# print(sum(all_temp)/len(all_temp))
# print(data["temp"].mean())
# print(data["temp"].max())

# use pandas documentation for the methods
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print(type(data))
# print(type(data["temp"]))

print(data.condition)
# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_faren = ((monday_temp*(9/5))+32)
print(monday_faren)


# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}


data = pandas.DataFrame(data_dict)
print(data)

# output
#   students  scores
# 0      Amy      76
# 1    James      56
# 2   Angela      65

# to save the data into csv format
data.to_csv("new_data.csv")
