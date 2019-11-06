# 使用方法

#### title_check ディレクトリ直下に `dj.txt` を作成し、英小文字でDJ名を記入
例 : dj.txt
```
fujimura
shimoda
suzuki
...
...
```

#### set_list ディレクトリ内に、各人のセットリストを、`DJ名.txt`として配置
```
fujimura.txt
shimoda.txt
suzuki.txt
...
...
```


#### title_check ディレクトリで以下を実行
```
python3 title_check.py > result/overlapping.txt
```

#### result ディレクトリ内に、曲の重複結果 `overlapping.txt` が生成されるので内容を確認
