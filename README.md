# 💼 Employee Payroll & Attendance Automation System

A Python-based automation project that streamlines employee payroll processing by reading attendance and employee data from Excel files, calculating salaries automatically, generating payroll reports and salary slips, automating Outlook emails, and exporting reports to PDF.

---

## 🚀 Features

- 📂 Read employee and attendance data from Excel files
- ✅ Validate employee and attendance records
- 🔗 Merge employee and attendance datasets
- 💰 Automatically calculate employee payroll
- 📊 Generate a consolidated payroll report in Excel
- 📄 Generate individual salary slips for every employee
- 📧 Send salary slips automatically using Microsoft Outlook
- 📑 Export payroll report to PDF using Microsoft Excel Automation
- 📝 Maintain execution logs for monitoring and debugging
- ⚠️ Handle errors gracefully with logging

---

## 🛠️ Technologies Used

- Python
- pandas
- openpyxl
- pywin32
- logging

---

## 📁 Project Structure

```text
PAYROLL-AUTOMATION
│
├── Input
│   ├── employees.xlsx
│   └── attendance.xlsx
│
├── Output
│   ├── payroll_report.xlsx
│   ├── payroll_report.pdf
│   └── Salary_Slips
│
├── Logs
│   └── payroll.log
│
├── src
│   ├── main.py
│   ├── data_loader.py
│   ├── validator.py
│   ├── merge_data.py
│   ├── payroll.py
│   ├── report.py
│   ├── salary_slip.py
│   ├── email_sender.py
│   ├── excel_automation.py
│   └── logger.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Workflow

1. Load employee data
2. Load attendance data
3. Validate input files
4. Merge employee and attendance records
5. Calculate payroll
6. Generate payroll report
7. Generate salary slips
8. Send salary slips through Outlook
9. Export payroll report to PDF
10. Save execution logs

---

## 💵 Payroll Calculation

The system calculates:

- Basic Salary
- Daily Salary
- Overtime Pay
- Bonus
- Leave Deduction
- Gross Salary
- Tax Amount
- Net Salary

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/MuhammadWaleed20/PAYROLL-AUTOMATION.git
```

Move into the project directory:

```bash
cd PAYROLL-AUTOMATION
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

---

## 📌 Requirements

- Python 3.11 or above
- Microsoft Outlook (for email automation)
- Microsoft Excel (required for PDF export using pywin32)

---

## 📂 Generated Output

The project automatically creates:

- 📊 Payroll Report (`payroll_report.xlsx`)
- 📑 Payroll Report PDF (`payroll_report.pdf`)
- 📄 Individual Salary Slips
- 📝 Execution Log (`payroll.log`)

---

## 🧠 Skills Demonstrated

- Python Programming
- Business Process Automation
- Data Processing with pandas
- Excel Automation with openpyxl
- Outlook Automation using pywin32
- Excel COM Automation
- Exception Handling
- Logging
- Modular Project Architecture
- Git & GitHub

---

## 🔮 Future Improvements

- PostgreSQL/MySQL database integration
- Employee management dashboard
- Automated email scheduling
- GUI using Tkinter or PyQt
- REST API integration
- Cloud deployment
- Power BI dashboard integration

---

## 👨‍💻 Author

**Muhammad Waleed**

- GitHub: https://github.com/MuhammadWaleed20
- Repository: https://github.com/MuhammadWaleed20/PAYROLL-AUTOMATION

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.