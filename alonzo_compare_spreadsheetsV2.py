import pandas as pd
import csv
file_path_one = ""
file_path_two = ""

index = 0
data = pd.read_csv(f"{file_path_one}/Gala Donations.xlsx - sf.csv")
names = data["Opportunity Name"]
amounts = data["Amount"]

my_csv = pd.read_csv(f"{file_path_two}/Spreadsheet2.xlsx - Sheet1.csv")
contacts = my_csv["Contacts"]
moneys = my_csv["Amount"]

with open("output.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow("Compare Spreadsheet2 Against Gala")

for name in names:
    num = 0
    found = False
    name = name.split()[:2]
    first_name = name[0].lower()
    last_name = name[1].lower()
    amount_one = amounts[index]
    for contact in contacts:
        if first_name in str(contact).lower() and last_name in str(contact).lower():
            mooney = moneys[num]
            mooney = mooney.replace(",", "")
            if float(mooney) == float(amount_one):
                found = True
                break
        num += 1
    if not found:
        with open("output.csv", "a", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(["The entry:", first_name + last_name, "with the amount of", amount_one, "was not found."])
        print(f"The entry: {first_name} {last_name} with the amount of {amount_one} was not found.")
    index += 1

with open("output.csv", "a", newline="") as output:
    writer = csv.writer(output)
    writer.writerow("Compare Gala to Spreadsheet2")
for contact in contacts:
    num = 0
    found = False
    contact = contact.split()[:2]
    first_name = contact[0].lower()
    last_name = contact[1].lower()
    amount_one = moneys[index]
    for name in names:
        if first_name in str(name).lower() and last_name in str(name).lower():
            amt = amounts[num]
            amt = amt.replace(",", "")
            if float(amt) == float(amount_one):
                found = True
                break
        num += 1
    if not found:
        with open("output.csv", "a", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(["The entry:", first_name+last_name, "with the amount of", amount_one, "was not found."])
        print("The entry:", first_name+last_name, "with the amount of", amount_one, "was not found.")
    index += 1





