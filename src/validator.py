import re


def validate_data(employees_df, attendance_df):
    """
    Validate employee and attendance data.

    Returns:
        True if validation passes.
        False otherwise.
    """

    print("\n========== VALIDATING DATA ==========\n")

    # ==========================================
    # Check if DataFrames are empty
    # ==========================================
    if employees_df.empty:
        print("❌ Employee data is empty.")
        return False

    if attendance_df.empty:
        print("❌ Attendance data is empty.")
        return False

    print("✅ Data is not empty.")

    # ==========================================
    # Required Columns
    # ==========================================
    employee_columns = [
        "Employee ID",
        "Name",
        "Department",
        "Email",
        "Basic Salary",
        "Overtime Rate",
        "Tax %",
        "Bonus"
    ]

    attendance_columns = [
        "Employee ID",
        "Working Days",
        "Overtime Hours",
        "Leave Days"
    ]

    # Check employee columns
    for column in employee_columns:
        if column not in employees_df.columns:
            print(f"❌ Missing Employee Column: {column}")
            return False

    # Check attendance columns
    for column in attendance_columns:
        if column not in attendance_df.columns:
            print(f"❌ Missing Attendance Column: {column}")
            return False

    print("✅ Required columns found.")

    # ==========================================
    # Duplicate Employee IDs
    # ==========================================
    duplicate_ids = employees_df["Employee ID"].duplicated()

    if duplicate_ids.any():
        print("\n❌ Duplicate Employee IDs Found:")
        print(employees_df.loc[duplicate_ids, ["Employee ID", "Name"]])
        return False

    print("✅ No duplicate Employee IDs.")

    # ==========================================
    # Missing Employee IDs
    # ==========================================
    if employees_df["Employee ID"].isnull().any():
        print("❌ Missing Employee ID found.")
        return False

    print("✅ Employee IDs are complete.")

    # ==========================================
    # Missing Employee Names
    # ==========================================
    if employees_df["Name"].isnull().any():
        print("❌ Missing Employee Name found.")
        return False

    print("✅ Employee names are complete.")

    # ==========================================
    # Missing Emails
    # ==========================================
    if employees_df["Email"].isnull().any():
        print("❌ Missing Email found.")
        return False

    print("✅ Email addresses are complete.")

    # ==========================================
    # Email Validation
    # ==========================================
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    invalid_email = employees_df[
        ~employees_df["Email"].astype(str).str.match(email_pattern)
    ]

    if not invalid_email.empty:
        print("❌ Invalid Email Format:")
        print(invalid_email[["Employee ID", "Email"]])
        return False

    print("✅ Email format is valid.")

    # ==========================================
    # Missing Salary
    # ==========================================
    if employees_df["Basic Salary"].isnull().any():
        print("❌ Missing Salary found.")
        return False

    print("✅ Salary values are complete.")

    # ==========================================
    # Negative Salary
    # ==========================================
    if (employees_df["Basic Salary"] < 0).any():
        print("❌ Negative Salary Found.")
        return False

    print("✅ Salary values are valid.")

    # ==========================================
    # Tax Validation
    # ==========================================
    invalid_tax = (
        (employees_df["Tax %"] < 0) |
        (employees_df["Tax %"] > 100)
    )

    if invalid_tax.any():
        print("❌ Invalid Tax Percentage.")
        return False

    print("✅ Tax values are valid.")

    # ==========================================
    # Overtime Validation
    # ==========================================
    if (attendance_df["Overtime Hours"] < 0).any():
        print("❌ Negative Overtime Hours found.")
        return False

    print("✅ Overtime values are valid.")

    # ==========================================
    # Leave Validation
    # ==========================================
    if (attendance_df["Leave Days"] < 0).any():
        print("❌ Negative Leave Days found.")
        return False

    print("✅ Leave values are valid.")

    # ==========================================
    # Working Days Validation
    # ==========================================
    if (attendance_df["Working Days"] < 0).any():
        print("❌ Negative Working Days found.")
        return False

    print("✅ Working days are valid.")

    # ==========================================
    # Final Success Message
    # ==========================================
    print("\n" + "=" * 50)
    print("✅ ALL VALIDATION CHECKS PASSED")
    print("=" * 50)

    return True