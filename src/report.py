from openpyxl import Workbook


def generate_payroll_report(payroll_df, output_file):
    """
    Generate Payroll Excel Report
    """

    wb = Workbook()
    ws = wb.active
    ws.title = "Payroll Report"

    ws.append(list(payroll_df.columns))

    for row in payroll_df.itertuples(index=False):
        ws.append(row)

    wb.save(output_file)

    print(f"\n Payroll report saved successfully!")
    print(f"Location: {output_file}")