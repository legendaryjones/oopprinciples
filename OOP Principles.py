# #- Inheritance: Extending a parent class, and giving it additional 
# #functionality and characteristic

# #General -> Specific


# #- Polymorphism: Objects from differnt classes responding similarly to the same method 
# #in their unique way.





class BudgetCategory():
    # Constructor and private attributes
   def __init__(self,name,budget):
        self.__name= name
        self.__budget= budget
        self.expense = 0



    # Getters and setters for category name and budget
    # ... def set_holder(self, new_holder):
   def set_name(self, user_name):
     self.__name = user_name

   def get_name(self):
        return self.__name

   def set_budget(self, user_budget):
        self.__budget = user_budget

   def get_budget(self):
        return self.__budget
        # Method to display the budget category details
        # ...




   def minus_expense(self, minus_expense): 
       if 0 < minus_expense <= self.get_budget():
        self.set_budget(self.get_budget() - minus_expense)
        print(f"I just spent ${minus_expense} out of my budget")
        print(f'Here is how much I have after ths purchase: ${self.get_budget()}')
       elif minus_expense > self.get_budget():
        print('You dont have that amount to cover this expense')
       else:
         print('Invalid')

minus_expense = BudgetCategory('budget', 4000)
rent= BudgetCategory ('rent', 1800)
utilites= BudgetCategory ('utilites', 400 )
misc= BudgetCategory ('misc',200 )

print(minus_expense.get_budget())
print(minus_expense.get_name())


 #mike = BudgetCategory, ("mikes budget",1000)
# # print (.get_budget)

misc.minus_expense(100)

# Example usage
# food_category = BudgetCategory("Food", 500)
# food_category.add_expense(100)
# food_category.display_category_summary()