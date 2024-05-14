
class BudgetCategory:
  def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expense = 0

  def name(self):
        return self.__name

  def name(self, name):
        self.__name = name

  def budget(self):
        return self.__budget

  def budget(self, budget):
        if budget >= 0:
            self.__budget = budget
        else:
            print("Error: Budget should be a positive number.")

  def add_expense(self, amount):
        if amount >= 0:
            self.__expense += amount
        else:
            print("Error: Expense amount should be a positive number.")

  def display_category_summary(self):
        remaining_budget = self.__budget - self.__expense
        print(f"Category Name: {self.__name}")
        print(f"Allocated Budget: {self.__budget}")
        print(f"Expenses: {self.__expense}")
        print(f"Remaining Budget: {remaining_budget}")


    
    
food_category = BudgetCategory("Food", 1000)
food_category.add_expense(1000)
food_category.display_category_summary()
