'''PERSONAL EXOPENSE TRACKER & MONTHLY REPORT GENERATOR'''

import math

def validate_expenses(description,category,amount, expense_date):
    
    if description.strip()=="":
            return False
        
    if category.strip()=="":
        return False

    if amount<=0:
        return False
    
    if expense_date is None:
        return False
    
    return True

def calculate_totals(expenses):
    
    amounts=[]
    
    for expense in expenses:
        amounts.append(expense["Amount"])
        
    total = math.fsum(amounts)
    
    return round(total,3)

def category_summary(expenses):
    
    category_total ={}
    
    for expense in expenses:
        
        category = expense["Category"]
        amount = expense["Amount"]
        
        if category in category_total:
            category_total[category] +=amount
            
        else:
            category_total[category]=amount
            
        for category in category_total:
            category_total[category] = round((category_total[category]),2)
            
    return category_total
        