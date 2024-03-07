# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()
# total = sum(temp_list)
# average_temp = total / len(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
print(data[data.temp == data.temp.max()])
