import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_file = "finance_data.csv"
    date_format = "%d-%m-%Y"
    COLUMNS = ["date","amount","category","description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_file, index= False)

    @classmethod
    def add_entry(cls,date,category,amount,description):
        new_entry={
            "date": date,
            "amount" : amount,
            "category" : category,
            "description" : description
        }
        with open(cls.CSV_file, "a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= cls.COLUMNS)
            writer.writerow(new_entry)



def get_transactions(start_date, end_date):
    df = pd.read_csv(CSV.CSV_file)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], format = CSV.date_format)
    start_date = datetime.strptime(start_date , CSV.date_format)
    end_date = datetime.strptime(end_date , CSV.date_format)

    mask = (df["date"] >= start_date) & (df["date"] <= end_date) 
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        print("No transactions found in this date range!")
    else:
        print(f"The transactions from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}")
        filtered_df.to_string(
            index = False, formatters={"date": lambda x: x.strftime(CSV.date_format) }
        )

        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
        
        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Savings: ${ total_income - total_expense:.2f}")
    return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Added successfully!...")


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choices('1->add', '2-> view transactions' and '3->exit): ")
        if choice == '1':
            add()
        elif choice == '2':
            print("Give the start date and end date for transactions: ")
            start_date = get_date("Enter the start date of transactions: ", allow_default = True)
            end_date = get_date("Enter the end date of transactions: ", allow_default = True)
            get_transactions(start_date, end_date)

        elif choice == '3':
            print("Exiting the program!")
            break
        else:
            print("Please enter valid choice(1,2 or 3): ")


if __name__ == "__main__":
    main()