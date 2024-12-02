import pandas as pd

def read_xlsx(file_path):
    df=pd.read_excel(file_path,['地理兑换码','历史兑换码'])
    df1=df['地理兑换码']
    df2=df['历史兑换码']
    
    str=''
    for item in df1['兑换码']:
        print(item)
        str+=f'"{item}",'
    for item in df2['兑换码']:
        print(item)
        str+=f'"{item}",'
    print(str)



def read_xlsx_wirte(file_path,origin_txt):
    """_summary_
    读取excel文件的数据tiket字段值，与txt文件中的值进行对比，然后写入excel文件中
    Args:
        file_path (_type_): _description_
        origin_txt (_type_): _description_
    """
    # 读取文件并按照换行符切割成数组
    with open(origin_txt, 'r') as file:
        lines = file.read().splitlines()  # 将每一行作为一个元素加入列表
    
    df=pd.read_excel(file_path,['地理兑换码','历史兑换码'])
    df1=df['地理兑换码']
    df2=df['历史兑换码']
    
    for index,row in df1.iterrows():
        ticket=row['兑换码']
        
        if ticket in lines:
            df1.at[index,'用户兑换状态']='未兑换'
        else:
            df1.at[index,'用户兑换状态']='已兑换'
    
    for index,row in df2.iterrows():
        ticket=row['兑换码']
        
        if ticket in lines:
            df2.at[index,'用户兑换状态']='未兑换'
        else:
            df2.at[index,'用户兑换状态']='已兑换'
    print(df1[['兑换码', '用户兑换状态']].head())  # 打印出兑换码和对应的用户兑换状态
    with pd.ExcelWriter(file_path,mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
        df1.to_excel(writer,sheet_name='地理兑换码',index=False)
        df2.to_excel(writer,sheet_name='历史兑换码',index=False)

read_xlsx_wirte("/Users/xjk/Desktop/back-code-project/python-tool/src/store/12-2.xlsx","/Users/xjk/Desktop/back-code-project/python-tool/src/12-2.txt")