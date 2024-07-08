import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low_salary_count = 0
    average_salary_count = 0
    high_salary_count = 0

    # Iterate through each income and categorize into respective bins
    for income in accounts['income']:
        if income < 20000:
            low_salary_count += 1
        elif income >= 20000 and income <= 50000:
            average_salary_count += 1
        elif income > 50000:
            high_salary_count += 1

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary_count, average_salary_count, high_salary_count]
    })

    return result