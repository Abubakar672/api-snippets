# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import json

# Find your credentials at twilio.com/console
api_key_sid = 'SKXXXX'
api_key_secret = 'your_api_key_secret'
client = Client(api_key_sid, api_key_secret)

composition = client.video.compositions.create(
    room_sid = 'RMXXXX',
    audio_sources = '*',
    audio_sources_excluded = 'advisor-audio',
    video_layout = {
                        'interviewed' : {
                            'z_pos': 2,
                            'x_pos': 400,
                            'y_pos': 180,
                            'width': 480,
                            'height': 360,
                            'video_sources': ['interviewed-video']
                        },
                        'interviewers': {
                            'z_pos': 1,
                            'x_pos': 10,
                            'y_pos': 0,
                            'width': 1260,
                            'height': 720,
                            'max_rows': 3,
                            'max_columns': 3,
                            'reuse': 'show_newest',
                            'cells_excluded': [4],
                            'video_sources': ['interviewer-*']
                        }
                    },
    status_callback = 'http://my.server.org/callbacks',
    resolution = '1280x720',
    format='mp4')

print('Created composition with SID=%s' % (composition.sid))
