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
