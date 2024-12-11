import pandas as pd


def read_csv_with_pandas(file_path):
    df = pd.read_csv(file_path, sep=";")

    total = 0
    totalG = 0
    num_rows = len(df)
    for row in df["authority_group_id"]:
        if row == 1:
            total += 1
        if row == 4:
            totalG += 1

    print(f"退掉历史的总共有{total}条数据")
    print(f"退掉地理的总共有{totalG}条数据")
    print(f"总共有{num_rows}条数据")


read_csv_with_pandas(
    "/Users/xjk/Desktop/back-code-project/python-tool/src/store/12-11-mysql.csv"
)
