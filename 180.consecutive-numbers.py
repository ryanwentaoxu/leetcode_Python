import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs2 = pd.DataFrame(logs)
    logs3 = pd.DataFrame(logs)
    merged = pd.merge(logs, logs2, on='num', suffixes=('_1', '_2'))
    filtered = merged[merged['id_1'] == merged['id_2'] - 1]
    merged = pd.merge(filtered, logs3, on='num')
    filtered = merged[merged['id_1'] == merged['id'] - 2]
    print(filtered)
    ans = len(filtered)
    if ans == 0:
        return pd.DataFrame({"ConsecutiveNums" : []})
    return pd.DataFrame({"ConsecutiveNums" : filtered['num'].unique()})