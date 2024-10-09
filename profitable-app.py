#Identifying Profitable App Profiles for the App Store and Google Play Markets

#Introduction:
#In this project, we are conducting data analysis for a company that develops mobile apps. Our apps are available on both the App Store and Google Play, and our main source of revenue comes from in-app advertisements. Our goal is to identify which types of apps attract more users, helping us reach a larger audience and increase our revenue.

#In this project, we will use our Python programming knowledge to analyze app data and provide guidance to developers so they can create successful apps that attract more users.

from csv import reader



#The Google Play reading Data Set
with open ("googleplaystore.csv", encoding="utf-8") as open_file:
    read_file = reader(open_file)
    android = list(read_file)
    android_header = android[0]
    android = android[1:]
    
#The App Storereading Data Set
with open ("AppleStore.csv", encoding="utf-8") as open_file:
    read_file = reader(open_file)
    ios = list(read_file)
    ios_header = ios[0]
    ios = ios[1:]
    

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print("\n")
explore_data(android, 0, 3, True)

#The Google Play data set has a dedicated discussion section, and we can see that one of 
#the discussions outlines an error for row 10472. Let's print this row and compare it against 
#the header and another row that is correct.

print(android[10472], "\n") #incorrect row
print(android_header, "\n") #header
print(android[0]) #correct row

print(len(android)) 
del(android[10472])
print(len(android))

#Removing Duplicate Entries
#Part One
#If we explore the Google Play data set long enough, we'll find that some apps have more than one entry. 
#For instance, the application Instagram has four entries:

for app in android:
    name = app[0]
    app_names = ["Instagram", "Facebook",]
    if name == app_names:
        print(app)

duplicated_app = []
uniq_app = set()
for app in android:
    name = app[0]
    if name in uniq_app:
        duplicated_app.append(name)
    else:
        uniq_app.add(name)

print('Number of duplicate apps:', len(duplicated_app))
print('\n')
print('Examples of duplicate apps:', duplicated_app[:15])