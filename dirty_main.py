from datetime import datetime
from Приложения.salary import *
from Приложения.база_данных.people import *

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(f"Текущая дата: {current_date}")
    print("-" * 40)

    calculate_salary()
    get_employees()