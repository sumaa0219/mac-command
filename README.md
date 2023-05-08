# mac-mommand
- このファイルをディレクトリ直下に置くこと。cloneするときもできればユーザー直下で ex) /Users/<username>/commands
- 一緒に入っている.zshrcをユーザー直下にコピー。すでにある場合は省略。
 - コピーした.zshrcを反映させる
  ```
  source ~/.zshrc
  ```
  
 - コマンドを使うには権限が必要 これで全てのコマンドが反映される
  ```
  find ./ -name . -exec sudo chmod 777 {} \;
  ```

