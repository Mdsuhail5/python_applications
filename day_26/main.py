
import pandas as pd
import random
numbers = [1, 2, 3]
new_list = []
for number in numbers:
    new_numb = number+1
    new_list.append(new_numb)

print(new_list)


# list comprehension
# syntax
# new_list=[new_item for item in numbers]

new_list = [n+1 for n in numbers]
print(new_list)

# sequences
# list,tuple,range,string

range_list = [num*2 for num in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_names = [name for name in names if len(name) < 5]
print(new_names)

second_list = [name.upper() for name in names if len(name) > 5]
print(second_list)

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [n*n for n in nums]

print(squared_nums)

result = [n for n in nums if n % 2 == 0]
print(result)

# dictionary comprehension
# syntax
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Angela", "Caroline", "Dave", "Elenor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {key: value for (
    key, value) in student_scores.items() if value >= 60}
print(passed_students)


# Looping through dictionaries:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)


for (key, value) in student_dict.items():
    print(key, value)

# iterating through pandas dataframe


student_df = pd.DataFrame(student_dict)
print(student_df)

# for (key, value) in student_df.items():
#     print(key)

# for (key, value) in student_df.items():
#     print(value)
print("-----"*10)
for (index, row) in student_df.iterrows():
    print(index)
print("------"*10)
for (index, row) in student_df.iterrows():
    print(row)
print("------"*10)
for (index, row) in student_df.iterrows():
    print(row.student)
print("------"*10)
for (index, row) in student_df.iterrows():
    print(row.score)
