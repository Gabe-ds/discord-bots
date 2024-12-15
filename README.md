# discord-bots

## 開発環境構築

本環境はpyenvとpoetryを使用する．

1. コード取得

```shell
git clone https://github.com/Gabe-ds/discord-bots.git
```

1. Pythonダウンロード

```shell
cd discord-bots
```

```shell
pyenv install $(cat .python-version)
```

1. ライブラリインストール

```shell
poetry add
```

1. 仮想環境起動

```shell
poetry shell
```

## 環境変数定義

BotのTOKENを定義する．

```shell
cp .env.template .env
```

コピーして作成された`.env`ファイルにTOKENを記述する．
