import datetime
import tabulate

import expense_utils as EU


def monthly_report(expenses, current_date=None):
    
    if current_date is None:
        current_date =datetime.date.today()
        
    monthly_expenses = []
    
    for expense in expenses:
        
        expense_date = expense["Date"]
        
        if(expense_date.year==current_date.year and expense_date.month==current_date.month):
            
            monthly_expenses.append(expense)
            
    print("\n"+"="*55)
    print("\n          Monthly Expense Report")
    print("\n"+"="*55)
    
    if len(monthly_expenses)==0:
        print("No expense record for this month.")
        
        return
    
    #Prepare Table
    table_data =[]
    
    for expense in monthly_expenses:
        
        row = [expense["Reference Id"],
               expense["Date"].strftime("%Y-%m-%d"),
               expense["Description"],
               expense["Category"],
               expense["Amount"]
               ]
               
        table_data.append(row)
        
        header = ["Reference ID",
                  "Date",
                  "Description",
                  "Category",
                  "Amount"
                  ]
        
        print(tabulate.tabulate(table_data, headers=header, tablefmt="grid"))
       
       #Total month expenditure      
        totals = EU.calculate_totals(monthly_expenses)       
        
        print("\nTotal spending: Rs.", format(totals, ".2f"))

        #category wise Expenditure
        category_totals = EU.category_summary(monthly_expenses)
        
        print("\n====Category-Wise Expenses====")
        
        for category,amount in category_totals.items():
            print(f"{category} :Rs {format(amount, ".2f")}")
