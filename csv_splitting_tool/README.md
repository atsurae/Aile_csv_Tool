## csv_splitting_tool
### 説明
csvの指定したカラム単位で分割するツール
例)ユーザーIDごとにcsvを分割する

### 使い方
Pythonとpipは入っている前提です。

* ターミナルで「library」ディレクトリに移動  
* Pythonパッケージの仮想環境を作成  
`python3 -m venv myenv`  
* 仮想環境をアクティベート  
`source myenv/bin/activate`  
* csv解析ライブラリの「pandas」をインストール  
`pip install pandas`  
* ツールを実行する「main.py」の中身を編集する  
  * 入出力を指定する「dict_data」を編集
  * ユニークにするカラムを指定する「unique_column」を編集
* ターミナルで「csv_splitting_tool」ディレクトリに移動  
* ツールを実行  
`python3 main.py`  