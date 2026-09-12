## Good Food Purchasing Data (2023) - Three Data Questions

## Why I chose this dataset
I chose this dataset because it comes from a real NYC Open Data report 
and includes information about food purchases made by different NYC agencies.
I personally think finding high-quality food can be very difficult in NYC,
especially because there are so many options available. 
This dataset provides general information regarding food product groups, food categories, 
agencies, vendors, and costs which allows me to explore patterns in NYC agency food purchasing
and compare at quantities, weights, and costs. 

## Three Data Questions

# Question 1: How many purchasing records are there in the Produce Food Product Group?

#produce_count = 0

#for row in food_data:
#    if row["Food Product Group"] == "Produce":
#       produce_count += 1
#print("Produce:", produce_count)
# output: Produce: 3821

Why the data structure supports this question:
This works because each row represents a food purchasing record,
and the Food Product Group column identifies the food group for each record.
By searching for the specific food product group, "Produce", 
we can count the number of records that match this category
and find the total number of purchasing records for Produce.

# Question 2: How many Produce vs. Meat pruchasing record are there?

#produce_count = 0
#meat_count = 0

#for row in food_data:
#    if row["Food Product Group"] == "Produce":
#        produce_count += 1
#    elif row["Food Product Group"] == "Meat":
#        meat_count += 1
#print("Produce:", produce_count)
#print("Meat:", meat_count)
#output: Produce: 3821, Meat: 1786


Why the data structure supports this question:
This works because we are iterating through each row in the dataset 
and counting only the records for "Produce" and "Meat"in the Food Product Group column. 
By doing this, we can compare the number of pruchasing records between these two food product groups.

# Question 3: How many Produce vs Meat purchasing records are from the Department of Education?

#doe_produce_count = 0
#doe_meat_count = 0

#for row in food_data:
#    if row["Agency"] == "Department of Education":
#        if row["Food Product Group"] == "Produce":
#            doe_produce_count += 1
#        elif row["Food Product Group"] == "Meat":
#            doe_meat_count += 1

#print("Department of Education Produce:", doe_produce_count)
#print("Department of Education Meat:", doe_meat_count)
#output: Department of Education Produce: 706, Department of Education Meat: 154

Why the data structure supports this question:
This works because the dataset contains both an "Agency" column 
and a "Food Product Group" column. 
We first search for an "Agency" column that's labeled as "Department of Education"
and then we count how many records are "Produce" or "Meat" from the "Food Product Groups" column.


What the Data Cannot Answer

One question that I might want to ask is "how often does agency purchase a specific food product group per month?
The dataset cannot answer this question because it only provides broad time periods, from 2019 to 2023, 
and does not provide the specific purchase dates, times, weeks, or months.
which can make it difficult to analyze the pruchasing frequency of a food product group in a short time of period.
It would be misleading to assume that certain types of food products are frequently purchased monthly
because multiple records for some food type can occurred within the same period. 
