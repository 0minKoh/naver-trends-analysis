import pandas as pd

def get_202409_relative_volumn(csv_file_path: str, brand_name: str) -> float:
  df = pd.read_csv(csv_file_path)
  df.set_index('date', inplace=True)
  df_202409 = df.loc['2024-09-01':'2024-09-30']
  sum = 0
  for el in df_202409[brand_name].values:
    sum += el
  return sum

def update_relative_to_absolute_value(montly_relative_volume: int, monthly_absolute_volume: int) -> float:
  search_volume_per_relative = monthly_absolute_volume / montly_relative_volume
  return search_volume_per_relative

def update_csvs(csv_file_path: str, abs_per_relative: int):
  df = pd.read_csv(csv_file_path)
  for idx, column in enumerate(df.columns):
    if idx == 0:
      continue
    df[f"{column}_absolute"] = df[column].apply(lambda x: x * abs_per_relative)
  df.to_csv(csv_file_path, index=True)
  print(f"{csv_file_path} updated")
  return df