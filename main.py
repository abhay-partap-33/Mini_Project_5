import datetime as dt
import random
import os

import expense_utils as EU

from report_utils import monthly_report

def main():
    expenses = []
    
    print("\n"+"="*70)
    print("\n               PERSONAL EXPENSE TRACKER")
    print("\n"+"="*70)
    
    while True:
        print("\nEnter Expenses Details")
        
        description = input("Enter description about expense: ")
        
        category = input("Enter category of expense: ")
        
        while True:
            
            amount = float(input("Enter expense amount: "))
            
            if amount<=0:
                print("Amount must be greater than 0.")
                continue
            break
        
        while True:
            
            date = input("Enter date of expenditure(YYYY-MM-DD): ")
            
            if date =="":
                expense_date = dt.date.today()
                break
            
            expense_date = dt.datetime.strptime(
                    date, "%Y-%m-%d"
                ).date()
            break
        
        #validation Check
        valid = EU.validate_expenses(description,category,amount,expense_date)
        
        if valid:
            refernce_id = "EXP-"+ str(random.randint(1000,9999))
            
            expense = {
            "Reference Id":refernce_id, "Date":expense_date, "Description":description, "Category":category, "Amount":amount}
        
            expenses.append(expense)
            print("\nExpense recorded successfully!")
            print("\nReference ID: ",refernce_id)
            
        else:
            print("\nInvalid Expense Details.")

        choice = input("Do you want to add another expenses?(y/n)")
        
        if choice.lower()!='y':
            break
        
    #MONTHLY EXPENDITURE REPORT
    monthly_report(expenses,dt.date.today())
    


    report_path = os.path.join(os.path.dirname(__file__),"requirements.txt")

    if os.path.exists(report_path):
        print("Report file exists.")
    else:
        print("Report file does not exist.")
        
if __name__ == "__main__":
    main()