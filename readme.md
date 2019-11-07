# このプログラムについて

#### 
準備するデータ ： DJ名簿(テキストファイル)、各DJのセットリスト(テキストファイル)
得られる結果 ： 各DJのセットリストの重複の有無(標準出力)、各DJの重複している曲目(テキストファイル)

# 使用手順

#### 1.  title_check ディレクトリ直下に `dj.txt` を作成し、DJ名を英小文字で中身に記入
例 : dj.txt
```
fujimura
shimoda
suzuki
...
...
```

#### 2.  set_list ディレクトリ下に、各人から受け取ったセットリストを、`DJ名.txt`として配置
```
fujimura.txt
shimoda.txt
suzuki.txt
...
...
```


#### 3.  title_check ディレクトリで以下を実行
```
python3 title_check.py
```
#### 4.  ターミナル上に、曲被りの有無が標準出力される
```
fujimura は OK
shimoda は OK
suzuki は 【重複あり】
...
...
```

#### 5.  result ディレクトリ内に、曲の重複結果 `DJ名_overlapping.txt` が生成されるので、詳細が確認出来る
