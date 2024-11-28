import os

print(os.getcwd())  # 输出当前工作目录

output_dir = os.path.join(os.getcwd(), 'src/store/out/')

print(output_dir)

print(os.path.exists('src/store/out/'))