import os
import ari
import time
from variaveisAmbientes import *

def on_channel_event(channel_obj, event_name):
    if event_name == 'StasisStart':
        playback = channel_obj.play(media='sound:custom/ura-menu')
        time.sleep(8)  # Wait 8 seconds for user input
        if playback.state != 'done':
            playback.stop()

        if channel_obj.dtmf_received:
            dtmf_digit = channel_obj.dtmf_received.get('digit')
            if dtmf_digit == '1':
                channel_obj.continue_in_dialplan(context='default', extension='200')
            elif dtmf_digit == '2':
                channel_obj.continue_in_dialplan(context='default', extension='201')
            else:
                channel_obj.play(media='sound:custom/invalid-option')
    elif event_name == 'StasisEnd':
        channel_obj.play(media='sound:custom/goodbye')
        channel_obj.hangup()

client = ari.connect(os.getenv('ASTERISK_URL'), os.getenv('ASTERISK_USER'), os.getenv('ASTERISK_PASS'))
client.on_channel_event('StasisStart', on_channel_event)
client.run(apps='ura')
