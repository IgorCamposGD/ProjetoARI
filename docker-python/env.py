import os

os.environ['HOST'] = 'http://192.168.0.6'
os.environ['PORT'] = '8088'
os.environ['URL'] =  os.getenv("HOST")+':'+os.getenv("PORT")
os.environ['ASTERISK_USER'] = 'asterisk'
os.environ['ASTERISK_PASS'] = 'asterisk'
os.environ['ASTERISK_APP'] = 'ura'