from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
from pyromod.listen import Listen
# Initialize Bot Client
bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

if STRING_SESSION:
    # Run Multiple Clients (bot and Client2)
    apps = [Client2, bot]
    for app in apps:
        app.start()  # Start all clients
    print("All clients started successfully.")

    idle()  # Keep the bot running

    for app in apps:
        app.stop()  # Stop all clients when exiting
    print("All clients stopped.")

else:
    # Run only the bot if STRING_SESSION is not provided
    bot.run()
