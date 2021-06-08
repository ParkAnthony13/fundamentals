# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1. 
x[1][0] = 15
# 2.
students[0]["last_name"] = "Bryant"
# 3.
sports_directory["soccer"][0] = "Andres"
# 4.
z[0]['y']=30
print(z)


# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for dicts in some_list:
        print(dicts.values())
        value_list = list(dicts.values())
        print(value_list)
        print(f"first_name - {value_list[0]}, last_name - {value_list[1]}")
iterateDictionary(students)





# 3. Get Values From a List of Dictionaries
students = [
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# Michael
# John
# Mark
# KB

# Jordan
# Rosales
# Guillen
# Tonel
for item in students:
    print(f"first name - {item['first_name']}, last name - {item['last_name']}")

# for i in range(0,len(students)):
#     print(students[i]['first_name'])
# for i in range(0,len(students)):
#     print(students[i]['last_name'])



# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
def printInfo(data):
    for key in data:
        print(f"{len(data[key])} {key}")
    for city in data[key]:
        print(city)
printInfo(dojo)
