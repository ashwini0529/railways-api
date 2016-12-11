
'''
Preset controller by torn for / route
'''
from modules import *


class homeHandler(tornado.web.RequestHandler):

    def get(self):
        ob = {
                'status': 'OK',
                'reponse': 'Application running'
        }
        self.write(tornado.escape.json_encode(ob))
