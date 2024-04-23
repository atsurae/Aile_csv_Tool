import os
import pandas as pd

# 元データを格納しているディレクトリ
original_csv = 'csv/original'
# 分割したデータを保存するディレクトリ
result_csv = 'csv/result'

# ユニークにするカラム
unique_column = 'email'

# 分割するデータのファイル名と保存先のファイル名を定義する
# 例)'「original」直下のファイル名':出力先のファイル名（userは動的に定義）
dict_data = {
    'activity_ring_20240101-20240331.csv': 'activity_ring/{user}_activity_ring_202401-202403.csv'
}

# CSVファイルを読み込む
for original_file, result_file in dict_data.items():
    df = pd.read_csv(f'{original_csv}/{original_file}')
    # 指定されたカラムのユニークな値を取得する
    users = df[unique_column].unique()
    # 各ユーザーについてデータを分割し、新しいCSVファイルとして保存する
    for user in users:
        df_user = df[df[unique_column] == user]
        output_path = f'{result_csv}/{result_file.format(user=user)}'
        # ディレクトリが存在しない場合は作成する
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_user.to_csv(output_path, index=False)