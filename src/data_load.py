import pandas as pd


def load_data(employee_file, attendance_file):
    employees_df = pd.read_excel(employee_file)
    attendance_df = pd.read_excel(attendance_file)

    return employees_df, attendance_df