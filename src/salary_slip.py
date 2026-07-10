import os
from openpyxl import Workbook


def generate_salary_slips(payroll_df, output_folder):
    """
    Generate one salary slip for each employee.
    """

    os.makedirs(output_folder, exist_ok=True)

    for _, employee in payroll_df.iterrows():

        wb = Workbook()
        ws = wb.active
        ws.title = "Salary Slip"

        ws["A1"] = "Employee ID"
        ws["B1"] = employee["Employee ID"]

        ws["A2"] = "Name"
        ws["B2"] = employee["Name"]

        ws["A3"] = "Department"
        ws["B3"] = employee["Department"]

        # Payroll Information
        ws["A5"] = "Basic Salary"
        ws["B5"] = employee["Basic Salary"]

        ws["A6"] = "Overtime Pay"
        ws["B6"] = employee["Overtime Pay"]

        ws["A7"] = "Bonus"
        ws["B7"] = employee["Bonus"]

        ws["A8"] = "Leave Deduction"
        ws["B8"] = employee["Leave Deduction"]

        ws["A9"] = "Tax Amount"
        ws["B9"] = employee["Tax Amount"]

        ws["A10"] = "Net Salary"
        ws["B10"] = employee["Net Salary"]

        filename = (
            f"{employee['Employee ID']}_"
            f"{employee['Name']}.xlsx"
        )

        filepath = os.path.join(output_folder, filename)

        wb.save(filepath)

    print("\n✅ Salary slips generated successfully.")