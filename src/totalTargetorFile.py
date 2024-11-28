# 多个文件爱你内容合并成为一个文件
input_files=['target.txt','target2.txt','target3.txt']
output_file='totalTarget.txt'


rootDir='/Users/xjk/Desktop/back-code-project/python-tool/src/store/out/'

with open(f'{rootDir}{output_file}','w',encoding='utf-8') as f_out:
    for file_name in input_files:
        with open(f'{rootDir}{file_name}','r',encoding='utf-8') as f_in:
            f_out.write(f_in.read())
            
print('文件合并完成')
    