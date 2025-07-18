import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_file = "finance_data.csv"
    date_format = "%d-%m-%Y"
    COLUMNS = ["date","category","amount","description"]

    @classmethod
    def initialize_csv(cls):
        try:
            with open(cls.CSV_file,"r"):
                print("CSV file already exists")
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_file, index= False)
    @classmethod
    def get_transactions(cls, start_date, end_date):

    

    



def main():
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


if __name__ == "__main__":
    main()