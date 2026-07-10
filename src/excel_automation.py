import os
import win32com.client


def automate_excel(excel_file, pdf_file):

    excel = win32com.client.Dispatch("Excel.Application")

    excel.Visible = False
    excel.DisplayAlerts = False

    workbook = excel.Workbooks.Open(
        os.path.abspath(excel_file)
    )

    worksheet = workbook.Worksheets("Payroll Report")

    worksheet.Columns.AutoFit()

    worksheet.Rows("2:2").Select()
    workbook.Application.ActiveWindow.FreezePanes = True

    workbook.ExportAsFixedFormat(
        0,
        os.path.abspath(pdf_file)
    )

    workbook.Save()

    workbook.Close(True)

    excel.Quit()

    print("✅ Excel automation completed successfully.")