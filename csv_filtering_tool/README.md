## csv_splitting_tool
### 説明
指定した文字列を含むcsvをフォルダごとに格納するツール
特定のポータルデータcsvを抜き出したい特に使います。

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
  * 検索する文字列を指定する「search_string」を編集
* ターミナルで「csv_filtering_tool」ディレクトリに移動  
* ツールを実行  
`python3 main.py`  