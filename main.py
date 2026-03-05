expenses = ["1.Breakfast - 70rup",
            "2.transport - 350rup",
            "3.recharges - 500rup",
            "4.grocery - 1000rup",
            "5.snakes - 200rup"    
]

money_spent = [70,350,500,1000,200]

menu = '''
       1. show all expense
       2. add expenes
       3. delete expenses
       4. total spent
       5. save expenses
       6. Exit

       '''

def save_expense():
        with open("zexpenses" , "w") as f:
                for e in expenses:
                        f.write(e + "\n")

def add_expenses():
        new_expenses = input("Enter the new expense = ")
        expenses.append(new_expenses)
        amount_spent = int(input("Enter the amount spent :"))
        money_spent.append(amount_spent)
        

def delete_expenses():
        index = 0
        for e in expenses:
                print(f"{index+1}.{e}")
                index += 1
        s = int(input("Enter the number that the expense had to be deleted : ")) - 1
        del expenses[s]
        del money_spent[s]

def total_spent():
        print(sum(money_spent))

def Exit():
        print("hope our app is useful to you")
        print("See you later")
        print("Thankyou !!!!")


def menu_show():
        while True:
                print(menu)
                choice = int(input("Enter the choice to be opened : "))

                if choice == 1:
                        for e in expenses:
                                print(e)

                elif choice == 2:
                        add_expenses()

                elif choice == 3:
                        delete_expenses()

                elif choice == 4:
                        total_spent()

                elif choice == 5:
                        save_expense()
                
                elif choice == 6:
                        Exit()

                else:
                        print("Invalid choice")
                        print("TRY AGAIN LATER")

menu_show()

                