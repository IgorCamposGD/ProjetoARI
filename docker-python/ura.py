import asyncari
from asyncari.state import ToplevelChannelState, DTMFHandler
import asyncio
import logging
import asks
import os
from variaveisAmbientes import *


class State(ToplevelChannelState, DTMFHandler):
    do_hang = False

    async def on_start(self):
        await self.channel.play(media='sound:welcome')

    async def on_dtmf_Star(self):
        self.do_hang = True
        await self.channel.play(media='sound:vm-goodbye')

    async def on_dtmf_Pound(self):
        await self.channel.play(media='sound:asterisk-friend')

    async def on_dtmf_one(self):
        await self.channel.play(media='sound:digits/1')
    
    async def on_dtmf_two(self):
        await self.channel.play(media='sound:digits/2')

    async def on_PlaybackFinished(self):
        if self.do_hang:
            try:
                await self.channel.continueInDialplan()
            except asks.errors.BadStatus:
                pass
        
async def on_start(client):
    
    async with client.on_channel_event('StasisStart') as listener:
        async for objs, event in listener:
            channel = objs['channel']
            await channel.answer()
            client.taskgroup.start_soon(State(channel).start_task)

async def main():
    async with asyncari.connect(os.getenv('URL'), os.getenv('ASTERISK_APP'), os.getenv('ASTERISK_USER'), os.getenv('ASTERISK_PASS')) as client:
        client.taskgroup.start_soon(on_start, client)
        # Run the WebSocket
        async for m in client:
            print("** EVENT **", m)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    logging.basicConfig(level=logging.DEBUG)

    # Executar a função para estabelecer a conexão e executar o aplicativo, aguardando eventos indefinidamente
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()





