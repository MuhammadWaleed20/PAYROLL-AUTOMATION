from data_load import load_data
from validator import validate_data
from merge import merge_data
from payroll import calculate_payroll
from report import generate_payroll_report
from salary_slip import generate_salary_slips



EMPLOYEE_FILE = "Input/employees.xlsx"
ATTENDANCE_FILE = "Input/attendance.xlsx"

PAYROLL_REPORT = "Output/payroll_report.xlsx"
SALARY_SLIP_FOLDER = "Output/Salary_Slips"


def main():

    print("=" * 60)
    print("EMPLOYEE PAYROLL AUTOMATION SYSTEM")
    print("=" * 60)



    employees_df, attendance_df = load_data(
        EMPLOYEE_FILE,
        ATTENDANCE_FILE
    )

    if employees_df is None or attendance_df is None:
        print("\nProgram stopped.")
        return


    if not validate_data(employees_df, attendance_df):
        print("\nValidation Failed.")
        return

    merged_df = merge_data(
        employees_df,
        attendance_df
    )

    print("\nData merged successfully.")
    print(f"Total Employees: {len(merged_df)}")

    payroll_df = calculate_payroll(merged_df)

    print("Payroll calculated successfully.")


    generate_payroll_report(
        payroll_df,
        PAYROLL_REPORT
    )


    generate_salary_slips(
        payroll_df,
        SALARY_SLIP_FOLDER
    )

    print("\nPayroll Preview\n")

    print(
        payroll_df[
            [
                "Employee ID",
                "Name",
                "Department",
                "Basic Salary",
                "Overtime Pay",
                "Bonus",
                "Leave Deduction",
                "Tax Amount",
                "Net Salary"
            ]
        ].head(10)
    )

    print("\n" + "=" * 60)
    print("PAYROLL AUTOMATION COMPLETED SUCCESSFULLY")
    print("=" * 60)



if __name__ == "__main__":
    main()