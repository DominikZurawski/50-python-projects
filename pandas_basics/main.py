# Work with csv file

# COMPLICATED:

#Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


#Using csv library
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# SIMPLER:

# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

print("-----------------------------------------------------------------------------")
#Central Park Squirrel Data Analysis
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrels = data["Primary Fur Color"].unique()
#print(squirrels)
squirrels_count = data["Primary Fur Color"].value_counts()
print(squirrels_count)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
#df = pandas.DataFrame(squirrels_count)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

print("--------------------------------------------------------------------------")

#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)





