from telethon.sync import TelegramClient
import asyncio

# Your Telegram API credentials
api_id = 21695379
api_hash = '2165722d6212b6894ca57739edbd50a9'
phone_number = '+2347064512708'
airdrop_bot_username = 'USDTMuskBot'  # ✅ This is the bot you're auto-claiming from

async def main():
    async with TelegramClient('autoclaim_session', api_id, api_hash) as client:
        await client.start(phone=phone_number)

        print("✅ Logged in successfully.")

        # Send /start to the airdrop bot
        await client.send_message(airdrop_bot_username, '/start')
        await asyncio.sleep(5)  # Wait for the bot to respond

        # Look for a "🎁" or "Claim" button in recent messages
        async for message in client.iter_messages(airdrop_bot_username, limit=10):
            if message.buttons:
                for row in message.buttons:
                    for button in row:
                        if '🎁' in button.text or 'Claim' in button.text or 'Receive' in button.text:
                            await button.click()
                            print("🎁 Gift claimed successfully!")
                            return
        print("❌ No claim button found. Try again later.")

# Run the bot
asyncio.run(main())
