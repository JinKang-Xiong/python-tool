import pandas as pd
import re
import os


# 正则表达式用于提取数字
def extract_number(text):
    # 使用正则表达式查找数字
    match = re.search(r"\d+", text)
    if match:
        return (
            match.group()
        )  # 返回第一个匹配的数字，r表示该字符串是原始字符串，不会进行转义
    return ""


def extract_code(text):
    # 使用正则表达式提取兑换码，假设兑换码由字母和数字组成
    match = re.search(r"兑换码：([A-Za-z0-9]+)", text)
    if match:
        return match.group(1)  # 提取到的兑换码
    return ""  # 如果没有匹配到，返回 None


# 读取文件并保存数据到txt文件
def read_and_save_to_txt(file_path, columns, output_txt_file):
    # 检查文件扩展名，决定读取Excel还是CSV
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".xlsx" or file_extension == ".xls":
        # 读取Excel文件
        df = pd.read_excel(file_path)
    elif file_extension == ".csv":
        # 读取CSV文件
        df = pd.read_csv(file_path)
    else:
        print("不支持的文件格式！")
        return

    # 打开txt文件准备写入
    with open(output_txt_file, "w", encoding="utf-8") as f:
        # 遍历指定列的每一行
        for index, row in df[columns].iterrows():
            # 提取数字并保存到txt文件，以逗号分隔
            # extracted_values = [extract_number(str(row[column])) for column in columns]
            extracted_values = []
            for column in columns:
                if column == "主订单编号":
                    extracted_values.append(extract_number(str(row[column])))

                elif column == "商家备注":
                    extracted_values.append(extract_code(str(row[column])))
            print(extracted_values)
            # 将提取的数字连接成一行，并以逗号分隔

            if any(value == "" for value in extracted_values):
                continue
            line = ",".join(extracted_values) + "\n"
            f.write(line)

    print(f"数据已经保存到 {output_txt_file}")  # f表示格式化字符串


read_and_save_to_txt(
    "/Users/xjk/Desktop/back-code-project/python-tool/src/store/12-11.csv",
    ["主订单编号", "商家备注"],
    "src/store/out/target1211-2.txt",
)
