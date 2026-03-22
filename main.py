import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# --- Renderのスリープ防止用 ---
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- Bot本体 ---
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    async def setup_hook(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")

bot = MyBot()

@bot.tree.command(name="test", description="起動テスト")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("✅ 正常に動いています！")

if __name__ == "__main__":
    Thread(target=run).start()
    token = os.getenv('TOKEN')
    bot.run(token)
