# mac-mommand
- このファイルをディレクトリ直下に置くこと。cloneするときもできればユーザー直下で ex) /Users/<username>/commands
- .zshrcを作成する。すでにある場合は省略。
  ```
  touch ~/.zshrc
  ```
 - .zshrcを編集する。
  ```
  sudo nano .zshrc
  ```
 - 下記を.zshrcに書く
  ```
  export PATH=$HOME/mac-command:$PATH
  ```
 - 変更した内容を反映させる
  ```
  source ~/.zshrc
  ```
  
  
 - コマンドを使うには権限が必要 ex)sudo chmod 777 chpdf
  ```
  sudo chmod 777 コマンドファイル
  ```

