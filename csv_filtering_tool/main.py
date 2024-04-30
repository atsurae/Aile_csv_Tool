import os
import glob
import shutil

# 元データを格納しているディレクトリ
original_csv = 'csv/original'
# 結果データを保存するディレクトリ
result_csv = 'csv/result'

# 検索する文字列
search_string = 'flights_climbed'
search_string2 = 'heart_rate'

# ディレクトリ内のすべてのCSVファイルを再帰的に検索
for filename in glob.glob(os.path.join(original_csv, '**', '*.csv'), recursive=True):
    # ファイル名に検索する文字列が含まれているかどうかを確認
    if search_string in os.path.basename(filename):
        print(f'Found "{search_string}" in {filename}')
        # ファイルをresult_csvディレクトリにコピー
        os.makedirs(result_csv + "/" + search_string, exist_ok=True)
        destination = os.path.join(result_csv, search_string, os.path.basename(filename))
        shutil.copy(filename, destination)
        print(f'Copied {filename} to {destination}')
    if search_string2 in os.path.basename(filename):
        print(f'Found "{search_string2}" in {filename}')
        # ファイルをresult_csvディレクトリにコピー
        os.makedirs(result_csv + "/" + search_string2, exist_ok=True)
        destination = os.path.join(result_csv, search_string2, os.path.basename(filename))
        shutil.copy(filename, destination)
        print(f'Copied {filename} to {destination}')
