import os
import glob
import pandas as pd

# 元データを格納しているディレクトリ
original_csv = 'csv/original'
# 結果データを保存するディレクトリ
result_csv = 'csv/result'

# 全てのCSVファイルを読み込む
csv_files = glob.glob(os.path.join(original_csv, '*.csv'))

# ファイル名から日付を抽出し、それに基づいてソート
# TODO:ここはファイル名の形式に合わせて変更する必要がある
csv_files.sort(key=lambda x: os.path.basename(x).split('_')[3], reverse=True)

# 全てのCSVファイルを結合
df = pd.concat((pd.read_csv(f) for f in csv_files))

# 結果を新しいCSVファイルに保存
df.to_csv(result_csv + "/result.csv", index=False)