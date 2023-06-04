import math
print("Welcome in program for accountants!")

#Choosing one of options

print("Menu:")
print("1. Purchase Invoice")
print("2. Bank Statement")
print("3. Sales Invoice")
print("4. Posting Commands")
print("5. Salaries")
print("6. Depreciation")
print("7. Show all operations on accounts")
print("8. Create profit and loss account")
print("9. Create balance")
print("10. Leave program")

#dictionary of all accounts

Accounts = {
    "010":{"dt":[0.00], 
           "ct":[0.00]},
    "011":{"dt":[0.00], 
           "ct":[0.00]},
    "020":{"dt":[0.00], 
           "ct":[0.00]},
    "030":{"dt":[0.00], 
           "ct":[0.00]},
    "040":{"dt":[0.00], 
           "ct":[0.00]},
    "070":{"dt":[0.00], 
           "ct":[0.00]},
    "071":{"dt":[0.00], 
           "ct":[0.00]},
    "072":{"dt":[0.00], 
           "ct":[0.00]},
    "075":{"dt":[0.00], 
           "ct":[0.00]},
    "080":{"dt":[0.00], 
           "ct":[0.00]},
    "091":{"dt":[0.00], 
           "ct":[0.00]},
    "130":{"dt":[0.00], 
           "ct":[0.00]},
    "200":{"dt":[0.00], 
           "ct":[0.00]},
    "201":{"dt":[0.00], 
           "ct":[0.00]},
    "220-1":{"dt":[0.00], 
           "ct":[0.00]},
    "220-2":{"dt":[0.00], 
           "ct":[0.00]},
    "221":{"dt":[0.00], 
           "ct":[0.00]},
    "230":{"dt":[0.00], 
           "ct":[0.00]},
    "240":{"dt":[0.00], 
           "ct":[0.00]},
    "280":{"dt":[0.00], 
           "ct":[0.00]},
    "300":{"dt":[0.00], 
           "ct":[0.00]},
    "310":{"dt":[0.00], 
           "ct":[0.00]},
    "330":{"dt":[0.00], 
           "ct":[0.00]},
    "400":{"dt":[0.00], 
           "ct":[0.00]},
    "401":{"dt":[0.00], 
           "ct":[0.00]},
    "402":{"dt":[0.00], 
           "ct":[0.00]},
    "403":{"dt":[0.00], 
           "ct":[0.00]},
    "404":{"dt":[0.00], 
           "ct":[0.00]},
    "405":{"dt":[0.00], 
           "ct":[0.00]},
    "409":{"dt":[0.00], 
           "ct":[0.00]},
    "490":{"dt":[0.00], 
           "ct":[0.00]},
    "640 - 1":{"dt":[0.00], 
           "ct":[0.00]},
    "640 - 2":{"dt":[0.00], 
           "ct":[0.00]},
    "701":{"dt":[0.00], 
           "ct":[0.00]},
    "702":{"dt":[0.00], 
           "ct":[0.00]},
    "711":{"dt":[0.00], 
           "ct":[0.00]},
    "712":{"dt":[0.00], 
           "ct":[0.00]},
    "730":{"dt":[0.00], 
           "ct":[0.00]},
    "731":{"dt":[0.00], 
           "ct":[0.00]},
    "740":{"dt":[0.00], 
           "ct":[0.00]},
    "741":{"dt":[0.00], 
           "ct":[0.00],},
    "750":{"dt":[0.00],
           "ct":[0.00]},
    "751":{"dt":[0.00],
           "ct":[0.00]},
    "760":{"dt":[0.00], 
           "ct":[0.00]},
    "761":{"dt":[0.00], 
           "ct":[0.00]},
    "801":{"dt":[0.00], 
           "ct":[0.00]},
    "802":{"dt":[0.00], 
           "ct":[0.00]},
    "803":{"dt":[0.00], 
           "ct":[0.00]},
    "804":{"dt":[0.00], 
           "ct":[0.00]},
    "820":{"dt":[0.00], 
           "ct":[0.00]},
    "840":{"dt":[0.00], 
           "ct":[0.00]},
    "860":{"dt":[0.00], 
           "ct":[0.00]},
    "870":{"dt":[0.00], 
           "ct":[0.00]}
    }


def saldo_ct (account): #
    dt = sum(Accounts[account]["dt"])
    ct = sum(Accounts[account]["ct"])
    if dt > ct:
        credit_balance = dt - ct
        return credit_balance
    else:
        return 0

def saldo_dt (account):
    dt = sum(Accounts[account]["dt"])
    ct = sum(Accounts[account]["ct"])
    if dt < ct:
        debit_balance = ct - dt
        return debit_balance
    else:
        return 0

def economic_cost_operation(dt_ct):
    Accounts[choose_debit][debet].append(dt_ct)
    Accounts[choose_credit][credit].append(dt_ct)
    


#Using for to update accounts

"""for account in Accounts:
    Accounts[account].update({"balance dt" : saldo_dt(account), "balance ct" : saldo_ct(account)})"""

#print (Accounts)

"""def number_of_account (Accounts):
    Accounts_balance = {}
    for keys, values in Accounts.items():
        Accounts_balance[keys] = saldo(keys)
    return Accounts_balance"""

# Using a program
while True:
    Option = input("Choose which document do you want to book: ") 
    
    if Option == "1": # Purchase Invoice
        print("310 - Warehouse")
        print("401 - Usage of materials and energy")
        print("402 - Services")
        print("403 - Taxes and fees")
        print("409 - Other costs")
        print("711 - Cost of finished sold products")
        print("712 - Cost of sold services")
        print("731 - The value of the goods sold at the purchase/acquisition price")
        print("741 - The value of the materials sold at the purchase/acquisition price")
        choose_debit = input("choose kind of cost: ")
        if choose_debit not in ("310", "401", "402", "403", "409", "711", "712", "731", "741"):
            print("This is not cost")
            continue
        debet = "dt"
        choose_credit = input("choose credit account: ")
        if choose_credit not in (Accounts):
            print("This is not an account")
            continue
        credit = "ct"
        while True:
            try:
                sums = float(input("choose your sum: "))
            except ValueError:
                print("this must be float!")
                break
            break   
    
    
    elif Option == "2": # Bank Statement
        print("130 - Bank Account")
        PayOrSell = input("Pay or Sell?: ")
        if PayOrSell == "Pay":
            choose_debit = input("Choose debit account: ")
            if choose_debit not in Accounts:
                print("This is not an Account")
                continue
            debet = "dt"         
              
            choose_credit = "130"
            if choose_credit not in (Accounts):
                print("This is not an account")
            credit = "ct"
            while True:
                try:
                    sums = float(input("choose your sum: "))
                except ValueError:
                    print("this must be float!")
                    break
                break 
        
        elif PayOrSell == "Sell":
            choose_debit = "130"
            debet = "dt"         
    
            choose_credit = input("Choose credit account: ")
            if choose_credit not in Accounts:
                print("This is not an Account")
                continue
            credit = "ct"
            while True:
                try:
                    sums = float(input("choose your sum: "))
                except ValueError:
                    print("this must be float!")
                    break
                break
            
        else:
            print("Error! It Must be Pay or Sell!")
            continue
        
    
    elif Option == "3": # Sales Invoice
        print("701 - Net revenues from the sale of finished products")
        print("702 - Net revenues from the sale of services")
        print("730 - Net revenues from sold goods")
        print("740 - Net revenues from sold materials")
        choose_debit = input("choose debit account: ")
        if choose_debit not in Accounts:
            print("This is not an account")
            continue
        debet = "dt"
        choose_credit = input("choose credit account: ")
        if choose_credit not in ("701", "702", "730", "740"):
            print("This is not a sell account")
            continue
        credit = "ct"
        while True:
            try:
                sums = float(input("choose your sum: "))
            except ValueError:
                print("this must be float!")
                break
            break  
    
    
    elif Option == "4": # Posting Commands
        choose_debit = input("choose debit account: ")
        if choose_debit not in Accounts:
            print("This is not an account")
            continue
        debet = "dt"
        choose_credit = input("choose credit account: ")
        if choose_credit not in Accounts:
            print("This is not a sell account")
            continue
        credit = "ct"
        while True:
            try:
                sums = float(input("choose your sum: "))
            except ValueError:
                print("this must be float!")
                break
            break  
    
    
    elif Option == "5": # Salaries
        print("220-1 - Settlements with the social insurance institution")
        print("220-2 - Settlements with the tax office")
        print("230 - Salary settlements")
        print("404 - Salaries")
        print("405 - Social security and other benefits")
        choose_debit = input("choose debit account: ")
        if choose_debit not in ("220-1", "220-2", "230", "404", "405"):
            print("This is not an account related with salaries")
            continue
        debet = "dt"
        choose_credit = input("choose credit account: ")
        if choose_credit not in ("220-1", "220-2", "230", "404", "405"):
            print("This is not an account related with salaries!")
            continue
        credit = "ct"
        while True:
            try:
                sums = float(input("choose your sum: "))
            except ValueError:
                print("this must be float!")
                break
            break  
    
    
    elif Option == "6": # Depreciation
        print("010 - Fixed assets")
        print("020 - Intangible assets")
        print("030 - longterm financial assets")
        print("040 - Investment property and law")
        print("070 - Depreciation of fixed assets")
        print("075 - Umorzenie wartości niematerialnych i prawnych")
        print("080 - Fixed assets under construction")
        print("091 - Tangible fixed assets in liquidation")
        choose_debit = input("choose debit account: ")
        if choose_debit not in ("010", "020", "030", "040", "070", "075", "080", "091"):
            print("This is not an account related with depreciation!")
            continue
        debet = "dt"
        choose_credit = input("choose credit account: ")
        if choose_credit not in ("010", "020", "030", "040", "070", "075", "080", "091"):
            print("This is not an account related with depreciation!")
            continue
        credit = "ct"
        while True:
            try:
                sums = float(input("choose your sum: "))
            except ValueError:
                print("this must be float!")
                break
            break  
        

    elif Option == "7": # Show all operations on accounts
        for Account, value in Accounts.items():
            print(Account, ":", value)
        continue
    
    
    elif Option == "8": # Create profit and loss account
        while True:
            try:
                #All values to profit and loss account
                Net_revenues_from_sales_and_equated_to_them = Accounts["701"]["balance ct"] + Accounts["702"]["balance ct"] + Accounts["730"]["balance ct"] + Accounts["740"]["balance ct"] + Accounts["490"]["balance ct"]
                Revenues_of_Financial_Products = Accounts["701"]["balance ct"] + Accounts["702"]["balance ct"]
                Cost_Of_Goods_sold = Accounts["711"]["balance dt"] + Accounts["712"]["balance dt"]
                The_value_of_sold_goods_and_materials = Accounts["731"]["balance dt"] + Accounts["741"]["balance dt"]
                Gross_profit_loss_on_sales = Net_revenues_from_sales_and_equated_to_them + Revenues_of_Financial_Products - Cost_Of_Goods_sold - The_value_of_sold_goods_and_materials
                Other_operating_income = Accounts["760"]["balance ct"]
                Other_operating_cost =  Accounts["761"]["balance dt"]
                Profit_and_loss_from_operations = Gross_profit_loss_on_sales + Other_operating_income - Other_operating_cost
                Financial_income = Accounts["750"]["balance ct"]
                Financial_costs = Accounts["751"]["balance dt"]
                Gross_profit_loss = Profit_and_loss_from_operations + Financial_income - Financial_costs
                Income_Tax = Accounts["870"]["balance dt"]
                Net_Profit_Loss = Gross_profit_loss - Income_Tax
                
                
                #Dictionary of profit and loss account
                Profit_and_loss_account = {
                    "Net revenues from sales and equated to them" : Net_revenues_from_sales_and_equated_to_them,
                    "Revenues of Financial Products " : Revenues_of_Financial_Products,
                    "Total sales and revenues" : Revenues_of_Financial_Products + Net_revenues_from_sales_and_equated_to_them,
                    "Cost of goods sold" : Cost_Of_Goods_sold,
                    "The value of sold goods and materials" : The_value_of_sold_goods_and_materials,
                    "Gross profit (loss) on sales" : Gross_profit_loss_on_sales,
                    "Other operating income " : Other_operating_income,
                    "Other operating cost " : Other_operating_cost,
                    "Profit (loss) from operations": Profit_and_loss_from_operations,
                    "Financial income" : Financial_income,
                    "Financial costs" : Financial_costs,
                    "Gross profit (loss)" : Gross_profit_loss,
                    "Income Tax" : Income_Tax,
                    "Net profit (loss)" : Net_Profit_Loss
                }
                
                for position, value in Profit_and_loss_account.items():
                    print(position, ":", value)
            except KeyError:
                print("You need values on accounts to create profit and loss account")
            
            break
        continue
    
    
    elif Option == "9": # Create Balance
        while True:
            try:
                IntangibleAssets = Accounts["020"]["balance dt"] - Accounts["072"]["balance ct"]
                TangibleFixedAssets = Accounts["011"]["balance dt"] - Accounts["071"]["balance ct"]
                LongTermReceivables = Accounts["240"]["balance dt"] - Accounts["280"]["balance ct"]
                LongTermInvestments = Accounts["030"]["balance dt"] + Accounts["040"]["balance dt"]
                LongTermPrepayments = Accounts["640 - 1"]["balance ct"]
                NonCurrentAssets = IntangibleAssets + TangibleFixedAssets + LongTermReceivables + LongTermInvestments + LongTermPrepayments
                
                Stock = Accounts["310"]["balance dt"] + Accounts["330"]["balance dt"]
                ShortTermReceivables = Accounts["200"]["balance dt"] + Accounts["201"]["balance dt"] + Accounts["221"]["balance dt"]
                ShortTermInvestments = Accounts["130"]["balance dt"]
                ShortTermPrepayments = Accounts["640 - 1"]["balance ct"]
                Assets = Stock + ShortTermReceivables + ShortTermInvestments + ShortTermPrepayments
                
                
                Basic_capital_fund = Accounts["801"]["balance ct"]
                Supplementary_capital_fund = Accounts["802"]["balance ct"]
                Capital_fund_from_revaluation = Accounts["804"]["balance ct"]
                Other_Reserve_capitals_funds = Accounts["803"]["balance ct"]
                Profit_loss_from_previous_years = Accounts["820"]["balance ct"]
                Net_Profit_Loss = Profit_and_loss_account["Net profit (loss)"]
                Equity_Fund = Basic_capital_fund + Supplementary_capital_fund + Capital_fund_from_revaluation + Other_Reserve_capitals_funds + Profit_loss_from_previous_years + Net_Profit_Loss
                
                Provisions_for_liabilities = Accounts["640 - 2"]["balance ct"]
                Long_term_liabilities = Accounts["240"]["balance ct"]
                Short_term_liabilities = Accounts["201"]["balance dt"] + Accounts["200"]["balance ct"]
                Accruals = Accounts["840"]["balance ct"]
                Liabilities_and_provisions_for_liabilities = Accruals + Short_term_liabilities + Long_term_liabilities + Provisions_for_liabilities
                
                Balance = {
                    "Assets" : {            
                        ("A. Non-current assets: ", NonCurrentAssets) : 
                            {
                                "I. Intangible assets" : IntangibleAssets,
                                "II. Tangible fixed assets" : TangibleFixedAssets,
                                "III. Long-term receivables" : LongTermReceivables,
                                "IV. Long term investments" : LongTermInvestments,
                                "V. Long-term prepayments" : LongTermPrepayments
                            },
                        ("B. Assets: ", Assets) :
                            {
                                "I. Stock" : Stock,
                                "II. Short-term receivables" : ShortTermReceivables,
                                "III. Short-term investments" : ShortTermInvestments,
                                "IV. Short-term prepayments" : ShortTermPrepayments
                            },
                    
                                },
                    "Liabilities" : {
                        ("A. Equity (fund): ", Equity_Fund) : 
                            {                    
                                "I. Basic capital (fund)" : Basic_capital_fund,
                                "II. Supplementary capital (fund)" : Supplementary_capital_fund,
                                "III. Capital (fund) from revaluation" : Capital_fund_from_revaluation,
                                "IV. Other Reserve capitals (funds)" : Other_Reserve_capitals_funds,
                                "V. Profit (loss) from previous years" : Profit_loss_from_previous_years,
                                "VI. Net profit (loss)" : Net_Profit_Loss,
                            },
                        ("B. Liabilities and provisions for liabilities: ", Liabilities_and_provisions_for_liabilities) : 
                            {
                                "I. Provisions for liabilities" : Provisions_for_liabilities,
                                "II. Long-term liabilities" : Long_term_liabilities,
                                "III. short-term liabilities" : Short_term_liabilities,
                                "IV. Accruals" : Accruals
                            }
                                    }
                }
            except KeyError:
                print("You need values on accounts to create balance")
            except NameError:
                print("You need profit(loss) account to create balance")
            for y in Balance:
                print(y)
                for i in Balance[y]:
                    print(i)        
                    for value, integer in Balance[y][i].items():
                        print(value, ":", integer)
            break
        continue
        
        
    elif Option == "10":
        print("Thank you for using our services!")
        break
    
    
    else:
        print("wrong option!")
        continue
    
    economic_cost_operation(sums)
    
    for account in Accounts:
            Accounts[account].update({"balance dt" : saldo_ct(account), "balance ct" : saldo_dt(account)})
    
    
    
    continue

