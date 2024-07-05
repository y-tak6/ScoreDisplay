# 得点表示アプリ
クイズ大会で使用される得点表示を行うアプリです。
但し、大会用よりはサークル等で企画に使えば少し華やかになるようなものかもしれません。
大会に使えるものを目指して更新したいと思っています。

## 使い方
### 起動
`main.py`を動かしてください。(ライブラリ fletが必要です)

また、問題文を`data/questions.csv`から、参加者を`data/members.csv`から読み込みます。ない場合エラーが発生するかもしれません。空白でも用意した方がいいかもしれません(Todo)。

### 今できること
- ○数と×数を数えることができる
- 問題文と答えを表示することができる
- 複数タブを切り替えられる
- 以下のルールで記録できる
- free
	- 連答(or 加速連答)付n○m×
		- 連答：連続で正解すると2点入る
		- 加速連答：n連続で正解するとn点入る
		- 設定で連誤答も付けられるように見えますが、未実装です

### タブ
右上のケバブメニュー(︙)を開けばタブを切り替えられます。ゴミ箱アイコンで消す事が出来ますが、一度メニューを閉じないと反映されません。
#### Add window
タブを増やせます。
入力内容は以下：
- name: タイトル
- member: 参加者、入力方法は以下：
  - `1, 3, 4, 5`とコンマ区切りで数字を入力すると、参加者のcsvのn行目にあたる人の名前を表示します。
  - `1:あああ, 2, 3`のように`:名前`とついているものがある場合は表示する名前をコロンの後の文字列にします。
  - `1/1{7 3 True True}, 2, 3/0{}`のように`/`の後にルールのIDと{}の中に必要なパラメータを空白区切りで入力した場合、その人物だけそのルールとなります。(注意：パラメータの数が合わない場合はエラーが出ます)
- ルール
  - ルールIDは上から0, 1, ...となります。
- 各パラメータ
- (Todo)開始問題番号


## 更新履歴
2024.07.05 最低限の基礎ができたので公開
