import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "antikozhi",
            api_id=int(os.environ.get("APP_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: "),
            device_model="AntiKozhi Ver 1.0.1"
    ) as antikozhi:
        print("\nprocessing...")
        await antikozhi.send_message(
            "me", f"#AntiKozhi User Session\n\n```{await antikozhi.export_session_string()}```\n\nKeep this Safe")
        print("Done !, Check your Saved Message!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
