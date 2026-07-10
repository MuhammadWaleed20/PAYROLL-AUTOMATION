from data_load import load_data
from validator import validate_data
from merge import merge_data
from payroll import calculate_payroll
from report import generate_payroll_report
from salary_slip import generate_salary_slips
from Email_sender import send_salary_slips
from logger import setup_logger



logger = setup_logger()



EMPLOYEE_FILE = "Input/employees.xlsx"
ATTENDANCE_FILE = "Input/attendance.xlsx"

PAYROLL_REPORT = "Output/payroll_report.xlsx"
SALARY_SLIP_FOLDER = "Output/Salary_Slips"


def main():

    logger.info("Program Started")

    print("=" * 60)
    print("EMPLOYEE PAYROLL AUTOMATION SYSTEM")
    print("=" * 60)

    try:

        employees_df, attendance_df = load_data(
            EMPLOYEE_FILE,
            ATTENDANCE_FILE
        )

        if employees_df is None or attendance_df is None:
            logger.error("Failed to load Excel files.")
            print("Program stopped.")
            return

        logger.info("Employee and attendance files loaded successfully.")


        if not validate_data(employees_df, attendance_df):
            logger.error("Validation failed.")
            print("Validation Failed.")
            return

        logger.info("Validation completed successfully.")


        merged_df = merge_data(
            employees_df,
            attendance_df
        )

        logger.info("Employee and attendance data merged.")

        print(f"\nData merged successfully.")
        print(f"Total Employees : {len(merged_df)}")


        payroll_df = calculate_payroll(merged_df)

        logger.info("Payroll calculated successfully.")

        print("Payroll calculated successfully.")


        generate_payroll_report(
            payroll_df,
            PAYROLL_REPORT
        )

        logger.info("Payroll report generated.")


        generate_salary_slips(
            payroll_df,
            SALARY_SLIP_FOLDER
        )

        logger.info("Salary slips generated.")

        send_salary_slips(
            payroll_df,
            SALARY_SLIP_FOLDER
        )

        logger.info("Salary slip emails processed.")



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

        logger.info("Program Finished Successfully.")

    except Exception as e:

        logger.exception(f"Unexpected Error: {e}")

        print(f"\nUnexpected Error: {e}")



if __name__ == "__main__":
    main()