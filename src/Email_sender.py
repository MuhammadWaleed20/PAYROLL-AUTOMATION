import os
import win32com.client


def send_salary_slips(payroll_df, salary_slip_folder):

    outlook = win32com.client.Dispatch("Outlook.Application")

    for _, employee in payroll_df.iterrows():

        email = employee["Email"]

        filename = f"{employee['Employee ID']}_{employee['Name']}.xlsx"

        attachment = os.path.join(
            salary_slip_folder,
            filename
        )

        mail = outlook.CreateItem(0)

        mail.To = email

        mail.Subject = "Monthly Salary Slip"

        mail.Body = f"""
Dear {employee['Name']},

Please find attached your monthly salary slip.

Regards,
HR Department
ABC Technologies
"""

        mail.Attachments.Add(attachment)

        mail.Display()


    print("All emails processed successfully.")