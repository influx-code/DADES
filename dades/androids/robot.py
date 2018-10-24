# --------------------------------
# Author : Garvey Ding
# Created: 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

import datetime
import time
import random

import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING, PICTURE, \
    RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM

from config import ConfigProtype
from utils.logger import Logger
from utils.tuling import Tuling


class Protype(object):
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

        self.config_protype = ConfigProtype
        self.status_storage_dir = self.config_protype.status_storage_dir
        self.name = self.config_protype.name
        self.combo_limit = 3

    def initial(self):
        self.tuling = Tuling(self.name)
        self.ins = self.auto_login()

        self.register_text()
        # self.register_picture()
        self.register_other()

    # Basic control
    def login(self):
        ins = itchat.new_instance()
        ins.login()
        return ins

    def auto_login(self):
        ins = itchat.new_instance()
        ins.auto_login(
            enableCmdQR = 2,
            hotReload = True, 
            statusStorageDir = self.status_storage_dir
        )
        return ins

    def run(self):
        self.ins.run()

    def send(self, msg_obj, content):
        msg_obj.user.send(content)

    def send_image(self, msg_obj, image_url):
        msg_obj.user.send_image(image_url)

    # Attributes
    def get_friends(self):
        friends = self.ins.get_friends(update=True)[0:]

        for f in friends:
            self.logger.log(f)

        # friends[0] is myself
        total = len(friends[1:])
        self.logger.log(total)

    def get_chatrooms(self):
        chatrooms = self.ins.get_chatrooms(update=True)

        for room in chatrooms:
            self.logger.log(room)

        total = len(chatrooms)
        self.logger.log(total)

    # Reply
    def reply_base(self, msg_obj, content):
        self.logger.log("receive raw text: \n" + str(content))
        
        res = self.tuling.chat(content)
        self.send(msg_obj, res)

        # combo = random.choice(range(1, self.combo_limit+1))
        # self.logger.log("combo : %d" % combo)

        # for i in range(combo):
        #     res = self.tuling.chat(content)
        #     self.send(msg_obj, res)
        #     content = res

        #     if combo > 1:
        #         time.sleep(round(random.random() * 2, 1))

    def register_text(self):

        @self.ins.msg_register(TEXT)
        def reply(msg):
            self.reply_base(msg, msg.text)

        @self.ins.msg_register(TEXT, isGroupChat=True)
        def reply_group(msg):
            self.reply_base(msg, msg.text)

    def register_picture(self):

        image_url = ""

        @self.ins.msg_register(PICTURE)
        def reply(msg):
            self.send_image(msg, image_url)

        @self.ins.msg_register(PICTURE, isGroupChat=True)
        def reply_group(msg):
            self.send_image(msg, image_url)

    def register_other(self):
        others = [MAP, CARD, NOTE, SHARING, PICTURE,
                  RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM]

        @self.ins.msg_register(others)
        def reply(msg):
            self.logger.log('!!!!!!!! : % s' % msg)
            # self.send(msg, "说话")
            self.reply_base(msg, "说")
            return

