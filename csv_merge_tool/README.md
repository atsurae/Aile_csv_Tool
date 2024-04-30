## csv_splitting_tool
### 説明
対象ディレクトリに入っている元データをファイル名に含まれている日付の新しい順に結合して一つのcsvにするツール

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
  * csv_files.sort関数のsplitの数を日付が含まれる箇所に修正
* ツールを実行  
`python3 main.py`  