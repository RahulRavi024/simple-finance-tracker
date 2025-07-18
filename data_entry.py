from datetime import datetime
date_format = "%d-%m-%Y"
Categories = {"I":"Income" , "E":"Expenses"}

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    else:
        try:
            date = datetime.strptime(date_str,date_format)
            return date.strftime(date,date_format)
        except ValueError:
            print("Please enter valid date!")
            return get_date(prompt, allow_default = False)
        

def get_category():
    category = input("Enter the category('I' for Income and 'E' for Expenses): ").upper()
    if category in Categories:
        return Categories[category]
    else:
        print("Invalid input!...Give valid inputs('I' or 'E')")
        return get_category()

def get_amount():
    try:
        amount = float(input("Please enter the amount: "))
        if amount<=0:
            print("Please enter valid ones!")
            return get_amount()
        return amount
    except ValueError:
        print("please enter valid")
        return get_amount()

def get_description():
    return input("Enter the description")