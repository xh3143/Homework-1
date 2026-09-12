# import dataset
import csv
def load_csv(file_path):
    data = []
    
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            
    return data
food_data = load_csv("Good_Food_Purchasing_Data.csv")

# print(food_data)


## Required Tasks

# Task 1: Print the first 2 rows

print(food_data[:2])

# Task 2: Print the first row

print(food_data[0])

# Task 3: 3. Print rows 10–19

print(food_data[10:20])

# Task 4:Print column names

print(food_data[0].keys())

# Task 5:Print the first 10 values of one column

for row in food_data[:10]:
    print(row["Food Product Category"])
    
# Task 6: Print the first 10 rows of three columns

for row in food_data[:10]:
    print(
        row["Food Product Group"],
        row["Food Product Category"],
        row["Product Name"]
    )
#Three Data Questions Code

# Question 1: How many purchasing records are there in the Produce Food Product Group?

produce_count = 0

for row in food_data:
    if row["Food Product Group"] == "Produce":
        produce_count += 1
print("Produce:", produce_count)

# Question 2: How many Produce vs. Meat pruchasing record are there?

produce_count = 0
meat_count = 0

for row in food_data:
    if row["Food Product Group"] == "Produce":
        produce_count += 1
    elif row["Food Product Group"] == "Meat":
        meat_count += 1
print("Produce:", produce_count)
print("Meat:", meat_count)

# Question 3: How many Produce vs Meat purchasing records are from the Department of Education?

doe_produce_count = 0
doe_meat_count = 0

for row in food_data:
    if row["Agency"] == "Department of Education":
        if row["Food Product Group"] == "Produce":
            doe_produce_count += 1
        elif row["Food Product Group"] == "Meat":
            doe_meat_count += 1

print("Department of Education Produce:", doe_produce_count)
print("Department of Education Meat:", doe_meat_count)
