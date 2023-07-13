import pandas as pd

index = 0
data = pd.read_csv(f"{file_path}Gala Donations.xlsx - sf.csv")
names = data["Opportunity Name"]
amounts = data["Amount"]

my_csv = pd.read_csv(f"{file_path}Spreadsheet2.xlsx - Sheet1.csv")
contacts = my_csv["Contacts"]
moneys = my_csv["Amount"]
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
        print("The entry:", first_name+last_name, "with the amount of", amount_one, "was not found.")
    index += 1
