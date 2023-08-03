import os
import asyncio
import asyncari
from variaveisAmbientes import *

async def on_channel_event(channel_obj, event_name):
    if event_name == 'StasisStart':
        playback = await channel_obj.play(media='/var/lib/asterisk/sounds/en/one-moment-please.gsm')
        await asyncio.sleep(8)  # Wait 8 seconds for user input

        if playback.state != 'done':
            await playback.stop()

        if channel_obj.dtmf_received:
            dtmf_digit = channel_obj.dtmf_received.get('digit')
            if dtmf_digit == '1':
                await channel_obj.continue_in_dialplan(context='default', extension='200')
            elif dtmf_digit == '2':
                await channel_obj.continue_in_dialplan(context='default', extension='201')
            else:
                await channel_obj.play(media='sound:custom/invalid-option')

    elif event_name == 'StasisEnd':
        await channel_obj.play(media='sound:custom/goodbye')
        await channel_obj.hangup()

async def main():
    async with asyncari.connect(os.getenv('ASTERISK_URL'), os.getenv('ASTERISK_APP'), os.getenv('ASTERISK_USER'), os.getenv('ASTERISK_PASS')) as client:
        client.on_channel_event('StasisStart', on_channel_event)
        async for m in client:
            print("** EVENT **", m)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Executar a função para estabelecer a conexão e executar o aplicativo, aguardando eventos indefinidamente
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()