import pandas as pd
import re
import os

# 正则表达式用于提取数字
def extract_number(text):
    # 使用正则表达式查找数字
    match = re.search(r'\d+', text)
    if match:
        return match.group()  # 返回第一个匹配的数字
    return ''

# 读取文件并保存数据到txt文件
def read_and_save_to_txt(file_path, columns, output_txt_file):
    # 检查文件扩展名，决定读取Excel还是CSV
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.xlsx' or file_extension == '.xls':
        # 读取Excel文件
        df = pd.read_excel(file_path)
    elif file_extension == '.csv':
        # 读取CSV文件
        df = pd.read_csv(file_path)
    else:
        print("不支持的文件格式！")
        return

    # 打开txt文件准备写入
    with open(output_txt_file, 'w', encoding='utf-8') as f:
        # 遍历指定列的每一行
        for index, row in df[columns].iterrows():
            # 提取数字并保存到txt文件，以逗号分隔
            extracted_values = [extract_number(str(row[column])) for column in columns]
            print(extracted_values)
            # 将提取的数字连接成一行，并以逗号分隔
            
            
            if any(value == '' for value in extracted_values):
                continue
            line = ','.join(extracted_values) + '\n'
            f.write(line)

    print(f"数据已经保存到 {output_txt_file}")

# 示例：读取'example.xlsx'或'example.csv'文件的'C'和'D'列，并保存到'target.txt'
read_and_save_to_txt('/Users/xjk/Desktop/back-code-project/python-tool/store/red.xlsx', ['订单号', '包裹备注信息'], 'target2.txt')
# 或者
# read_and_save_to_txt('example.csv', ['C', 'D'], 'target.txt')
