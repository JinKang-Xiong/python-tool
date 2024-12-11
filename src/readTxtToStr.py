def extract_second_elements(file_path):
    result = []

    # 打开文件并逐行读取
    with open(file_path, "r") as file:
        for line in file:
            # 去掉行末的换行符并分割
            elements = line.strip().split(",")

            # 检查是否有足够的元素（至少 2 个）
            if len(elements) > 1:
                result.append(f'"{elements[1]}"')  # 提取第二个元素

    # 使用逗号连接所有的第二个元素，形成一个字符串

    return ",".join(result)


# 使用示例
file_path = "/Users/xjk/Desktop/back-code-project/python-tool/src/store/out/target1211-2.txt"  # 替换为你的文件路径
output_string = extract_second_elements(file_path)
print(output_string)
