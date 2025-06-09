import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rnk'] = employee['salary'].rank(method='dense', ascending=False)
    ans = employee[employee.rnk == N]['salary'].unique()
    print(ans)
    if not len(ans):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': ans})