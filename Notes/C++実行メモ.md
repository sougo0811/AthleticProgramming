# C++ 実行メモ

## コンパイル
```
g++ ファイル名.cpp -o ファイル名
(-o ファイル名 がない場合 a.exe にコンパイルされる)
```

## ディレクトリ指定
```
AtCoder/問題ID/問題アルファベット
```

## 実行
```
./ファイル名
./a.exe (ファイル名がない場合)
```

## デバッグ用コード
```
g++ -g -O0 <ソースファイル名>
```
-g	ファイルにデバッグ情報を付加する。これがないとデバッグ時に変数名や行番号が表示されない<br>
-O0	最適化を行わない。最適化を行うと、コードの入れ替えや削除が行われてしまい、デバッグしにくくなる<br>
