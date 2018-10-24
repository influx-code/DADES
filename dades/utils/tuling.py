# --------------------------------
# Author : Garvey Ding
# Created: 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

import json
import requests

from config import ConfigTuling
from utils.logger import Logger


class Tuling(object):
    def __init__(self, user_id):
        self.logger = Logger(self.__class__.__name__)

        self.config_cls = ConfigTuling
        self.apikey = self.config_cls.apikey
        self.secret = self.config_cls.secret
        self.host = self.config_cls.host

        self.user_id = user_id

    def format_body(self, msg):
        return {
            'key': self.apikey,
            'info': msg,
            'userid': self.user_id
        }

    def get_response(self, msg):
        text = None

        try:
            res = requests.post(url=self.host, json=self.format_body(msg))
            data = res.json()
            text = data.get('text')
        except Exception as e:
            self.logger.errlog('Tuling error: %e' % res.content)

        return text

    def chat(self, msg):
        return self.get_response(msg)
