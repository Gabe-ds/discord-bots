import logging
import os

import discord
from discord import app_commands
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
tree = app_commands.CommandTree(client)


@client.event
async def on_ready() -> None:
    """起動時自動実行"""
    logger.info("起動完了")
    logger.info("スラッシュコマンド読み込み開始")
    await tree.sync()
    logger.info("スラッシュコマンド読み込み完了")


@tree.command(name="sample-1", description="This is sample commnad 1")
async def sample_command_1(interaction: discord.Interaction) -> None:
    """引数なしのサンプルコマンド

    Parameters
    ----------
    interaction : discord.Interaction
        スラッシュコマンド
    """
    await interaction.response.send_message("This is sample command!")


@tree.command(name="sample-2", description="This is sample command 2")
async def sample_command_2(interaction: discord.Interaction, name: str, age: int) -> None:
    """引数に含まれる名前と年齢の確認をする

    Parameters
    ----------
    interaction : discord.Interaction
        スラッシュコマンド
    name : str
        名前
    age : int
        年齢
    """
    if age == 1:
        await interaction.response.send_message(f"Is your name {name} and are you one year old?")

    await interaction.response.send_message(f"Is your name {name} and are you {age} years old?")


TOKEN = os.environ["TOKEN"]
# discord.py標準のロガーを無効化
client.run(token=TOKEN, log_handler=None)
