import pandas as pd


def load_data(employee_file, attendance_file):
    """
    Reads employee and attendance Excel files.

    Parameters:
        employee_file (str): Path to employee file
        attendance_file (str): Path to attendance file

    Returns:
        tuple:
            employees_df,
            attendance_df
    """

    try:
        employees_df = pd.read_excel(employee_file)
        attendance_df = pd.read_excel(attendance_file)

        print("✅ Excel files loaded successfully.\n")

        return employees_df, attendance_df

    except FileNotFoundError as e:
        print(f"❌ File not found: {e.filename}")
        return None, None

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return None, None