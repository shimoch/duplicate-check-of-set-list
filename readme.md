# 使用方法

#### 1.  title_check ディレクトリ直下に `dj.txt` を作成し、DJ名を英小文字で中身に記入
例 : dj.txt
```
fujimura
shimoda
suzuki
...
...
```

#### 2.  set_list ディレクトリ内に、各人から受け取ったセットリストを、`DJ名.txt`として配置
```
fujimura.txt
shimoda.txt
suzuki.txt
...
...
```


#### 3.  title_check ディレクトリで以下を実行
```
python3 title_check.py > result/overlapping.txt
```

#### 4.  result ディレクトリ内に、曲の重複結果 `overlapping.txt` が生成されるので内容を確認
