import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']

    total_times = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()

    total_times.columns = ['emp_id', 'day', 'total_time']

    total_times = total_times[['day', 'emp_id', 'total_time']]

    return total_times