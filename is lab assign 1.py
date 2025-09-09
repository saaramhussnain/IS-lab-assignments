# Task 1
print("\nTask 1: Merge and Sort Lists")

print("Enter numbers")
list1 = input().split()
list2 = input().split()

print("List 1:", list1)
print("List 2:", list2)

merged_list = list1 + list2
print("Merged list:", merged_list)

merged_list.sort()
print("Sorted merged list:", merged_list)

# Task 2
print("\n\nTask 2: Find Smallest and Largest")

print("Using the merged list:", merged_list)

smallest = min(merged_list)
largest = max(merged_list)

print("Smallest element:", smallest)
print("Largest element:", largest)

# Task 3
print("\n\nTask 3: Birthday Dictionary")

birthdays = {
    "Tiamour": "03/14/1879",
    "kashif": "01/17/1706",
    "nouman": "12/10/1815"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
print("Tiamour")
print("kashif")
print("nouman")

name = input("\nWho's birthday do you want to look up? ")

if name in birthdays:
    print(name + "'s birthday is " + birthdays[name] + ".")
else:
    print("Sorry, I don't know that person's birthday.")

# Task 4
print("\n\nTask 4: Extract Dictionary Keys")

sample_dict = {
    "name": "abdullah",
    "age": 20,
    "salary": 10000,
    "city": "attock"
}

print("Given dictionary:")
print(sample_dict)

keys_to_extract = ["name", "salary"]
print("Keys to extract:", keys_to_extract)

new_dict = {}
new_dict["name"] = sample_dict["name"]
new_dict["salary"] = sample_dict["salary"]

print("New dictionary with extracted keys:")
print(new_dict)