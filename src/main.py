from data_load import load_data
from validator import validate_data
from merge import merge_data
from payroll import calculate_payroll
from report import generate_payroll_report

EMPLOYEE_FILE = "Input/employees.xlsx"
ATTENDANCE_FILE = "Input/attendance.xlsx"

OUTPUT_FILE = "Output/payroll_report.xlsx"


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

    payroll_df = calculate_payroll(merged_df)

    generate_payroll_report(
        payroll_df,
        OUTPUT_FILE
    )


if __name__ == "__main__":
    main()