import pandas as pd

def read_excel(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    return df

# test code
df = read_excel('/Users/sohyunwoo/Desktop/developer/python_personal/naver-trends/assets/excel_naver_trends/datalab.xlsx')
print(df.info())