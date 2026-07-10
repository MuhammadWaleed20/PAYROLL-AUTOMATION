from data_load import load_data
from validator import validate_data
from merge import merge_data


EMPLOYEE_FILE = "Input/employees.xlsx"
ATTENDANCE_FILE = "Input/attendance.xlsx"


def main():

    employees_df, attendance_df = load_data(
        EMPLOYEE_FILE,
        ATTENDANCE_FILE
    )

    if employees_df is None or attendance_df is None:
        return

    if not validate_data(employees_df, attendance_df):
        return

    merged_df = merge_data(
        employees_df,
        attendance_df
    )

    print("\nMerged Data\n")
    print(merged_df.head())

    print("\nTotal Employees:", len(merged_df))


if __name__ == "__main__":
    main()