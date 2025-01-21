from discord import Client, Intents, Message
from application.program import Application
from discord.ext import commands
from os import getenv

# Cria o cliente do bot
base: Client = commands.Bot(command_prefix="->", help_command=None, intents=Intents.all(), owner_id=1037376694450933821, description="Theriana do agoj 🤍")

@base.event
async def on_ready() -> None:
    await Application.on_started(base)
    pass

@base.event
async def on_message(message: Message) -> None:
    await Application.message_reviced(message, base)
    pass

if __name__ == "__main__":
    # Inicializa o boto em seu estado atual
    base.run(token=str(getenv("TOKEN")), reconnect=bool(True))
    pass

