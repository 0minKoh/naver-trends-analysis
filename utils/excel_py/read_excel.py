import pandas as pd

def read_excel(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    return df

def extract_keywords(df: pd.DataFrame) -> list:
    keywords_list = []
    for idx, el in enumerate(df.iloc[5].values):
        if (idx % 2 != 0):
            keywords_list.append(el)
    return keywords_list

def create_relative_column_names(df: pd.DataFrame) -> list:
    keywords_list = []
    for idx, el in enumerate(df.iloc[5].values):
        if (idx % 2 != 0):
            keywords_list.append(f"{el}")
    return keywords_list

def create_relative_csv(excel_file_path: str) -> list:
    df = read_excel(excel_file_path)
    keywords_list = []
    for idx, el in enumerate(df.iloc[5].values):
        if (idx % 2 != 0):
            keywords_list.append(el)

    df_relative_search = df.iloc[6:]
    df_relative_search.reset_index(drop=True, inplace=True)
    # 필요없는 열 (1, 2번째 열) 삭제
    # df_relative_search.drop(df_relative_search.columns[[0, 1]], axis=1, inplace=True)

    # 1. 날짜 인덱스 생성
    date_index = pd.to_datetime(df.iloc[6:, 0])  # 날짜 형식으로 변환

    # 2. 필요한 칼럼 데이터 선택
    column_len = len(df.columns)
    columns_to_extract = [i for i in range(1, column_len, 2)]
    column_data = df.iloc[6:, columns_to_extract] # 1, 3, 5, 7, 9 index인 열 선택

    # 3. 열 이름 추출
    column_names = create_relative_column_names(df)

    # 4. 새 DataFrame 생성
    new_df = pd.DataFrame(column_data.values, index=date_index, columns=column_names)
    new_df.rename_axis('date', inplace=True)

    for column in new_df.columns:
        column_df = new_df[[column]]
        column_df.to_csv(f"res/{column}.csv", index=True)

    return keywords_list

def remove_excel(excel_file_path: str):
    import os
    os.remove(excel_file_path)
