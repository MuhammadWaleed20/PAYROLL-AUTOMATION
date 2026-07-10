import pandas as pd


def merge_data(employees_df, attendance_df):
    """
    Merge employee and attendance data
    using Employee ID.
    """

    merged_df = pd.merge(
        employees_df,
        attendance_df,
        on="Employee ID",
        how="inner"
    )

    return merged_df