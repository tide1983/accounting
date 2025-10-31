from datetime import datetime
import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.dirname(__file__))

try:
    from Приложения.salary import calculate_salary
    from Приложения.база_данных.people import get_employees

    print("✅ Все модули успешно импортированы!")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Проверьте:")
    print("1. Существует ли папка 'Приложения'")
    print("2. Существует ли файл 'Приложения/salary.py'")
    print("3. Существует ли файл 'Приложения/база_данных/people.py'")
    exit(1)

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(f"📅 Текущая дата: {current_date}")
    print("-" * 40)

    calculate_salary()
    get_employees()