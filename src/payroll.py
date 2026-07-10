
def calculate_payroll(df):
    """
    Calculate payroll for all employees.
    """

    df["Daily Salary"] = df["Basic Salary"] / 26

    df["Overtime Pay"] = (
        df["Overtime Hours"] *
        df["Overtime Rate"]
    )

    df["Leave Deduction"] = (
        df["Leave Days"] *
        df["Daily Salary"]
    )

    df["Gross Salary"] = (
        df["Basic Salary"]
        + df["Overtime Pay"]
        + df["Bonus"]
    )

    df["Tax Amount"] = (
        df["Gross Salary"] *
        (df["Tax %"] / 100)
    )

    
    df["Net Salary"] = (
        df["Gross Salary"]
        - df["Leave Deduction"]
        - df["Tax Amount"]
    )

    return df