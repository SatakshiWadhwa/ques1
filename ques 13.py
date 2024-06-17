
from datetime import datetime


current_year = datetime.now().year


birth_year = int(input("Please enter your birth year: "))


age = current_year - birth_year

print(f"You are {age} years old")