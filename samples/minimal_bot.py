import logging
import os

import discord
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
# discord.pyのログ出力フォーマットを再現
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    """起動時自動実行"""
    msg = f"We have logged in as {client.user}"
    logger.info(msg)


@client.event
async def on_message(message: discord.Message) -> None:
    """`$hello`で始まる`メッセージ`が送られた時Helloを返す

    Parameters
    ----------
    message : discord.Message
        チャットメッセージ
    """
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


TOKEN = os.environ["TOKEN"]
# discord.py標準のロガーを無効化
client.run(token=TOKEN, log_handler=None)
