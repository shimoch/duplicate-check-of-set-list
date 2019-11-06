・title_check ディレクトリ直下に dj.txt を作成し、英小文字でDJ名を記入
例 : dj.txt
fujimura
shimoda
suzuki
...
...

・title_check ディレクトリで以下を実行
python3 title_check.py > result/overlapping.txt

・result ディレクトリ内に、曲の重複結果 overlapping.txt が生成されているので、内容を確認