import os
import pandas as pd

original_csv = 'csv/original'
result_csv = 'csv/result'

dict_data = {
    'activity_ring_20240101-20240331.csv': 'activity_ring/{user}_activity_ring_202401-202403.csv',
    'distance_20240101-20240331.csv': 'distance/{user}_distance_202401-202403.csv',
    'sleep_20240101-20240331.csv': 'sleep/{user}_sleep_202401-202403.csv',
    'step_count_20240101-20240331.csv': 'step_count/{user}_step_count_202401-202403.csv',
}

# CSVファイルを読み込む
for original_file, result_file in dict_data.items():
    df = pd.read_csv(f'{original_csv}/{original_file}')
    # 'email'列のユニークな値を取得する
    users = df['email'].unique()
    # 各ユーザーについてデータを分割し、新しいCSVファイルとして保存する
    for user in users:
        df_user = df[df['email'] == user]
        output_path = f'{result_csv}/{result_file.format(user=user)}'
        # ディレクトリが存在しない場合は作成する
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df_user.to_csv(output_path, index=False)