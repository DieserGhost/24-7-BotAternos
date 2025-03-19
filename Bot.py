from javascript import require, On

# Importiere die Mineflayer-Bibliothek
mineflayer = require("mineflayer")

reconnect = True


def create_bot():
    bot = mineflayer.createBot(
        {
            #"username": "Name", # Only if u want to use Cracked
            "host": "TheGhost143.aternos.me",
            "port": 52785,
            "version": "1.19.2",
            "auth": "microsoft",
            "hideErrors": False,
        }
    )

    # Login-Event
    @On(bot, "login")
    def login(this):
        print("Bot logged in sucessfully!")

    @On(bot, "end")
    def end(this, reason):
        print(f"Disconnected: {reason}")
        if reconnect:
            print("RESTARTING THE BOT")
            create_bot()


create_bot()
