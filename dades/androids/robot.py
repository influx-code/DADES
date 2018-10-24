# --------------------------------
# Author : Garvey Ding
# Created: 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

import datetime
import random

import itchat
from itchat.content import *

from config import ConfigRobot
from utils.logger import Logger



class Robot(object):
    def __init__(self):
        self.logger = Logger(self.__class__.__name__)

        self.config_cls = ConfigRobot
        self.status_storage_dir = self.config_cls.status_storage_dir
        self.default_reply = self.config_cls.default_reply

        self.ins = self.auto_login()
        self.register_text()
        self.register_other()

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

    def register_text(self):

        def reply_base(msg):
            raw_text = msg.text
            self.logger.log("receive raw text: \n" + str(raw_text))

            sentences = raw_text.split('\n')
            reply_lst = []
            csv_data_lst = []

            for i,sentence in enumerate(sentences):
                lst = []

                if sentence.find('：') > 0:
                    lst = sentence.split('：')
                elif sentence.find(':') > 0:
                    lst = sentence.split(':')
                
                if not lst:
                    self.logger.errlog("no ':' found, raw sentence : %s" % sentence)
                    # msg.user.send(self.reply_default(msg.user['NickName']))
                    msg.user.send('rubbish')
                    continue

                head = lst[0][0]
                val = lst[1]

                if i == 0:
                    head = lst[0][0:2]
                
                new_s = head + ' ' + val
                reply_lst.append(new_s)

                csv_data_lst.append(val)

            if csv_data_lst:
                csv_data_lst.append(
                    datetime.datetime.strftime(
                        datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'
                    )
                )
                self.write_csv(csv_data_lst)

            reply_s = '\n'.join(reply_lst)
            msg.user.send(reply_s)
            # return reply_s

        @self.ins.msg_register(TEXT)
        def reply(msg):
            reply_base(msg)
    
        # @self.ins.msg_register(TEXT, isGroupChat=True)
        # def reply_group(msg):
        #     reply_base(msg)

    def register_other(self):
        others = [MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS]

        @self.ins.msg_register(others)
        def reply(msg):
            print(msg)
            if msg.user.get('NickName'):
                msg.user.send(self.reply_default(msg.user['NickName']))
            else:
                msg.user.send(self.reply_default('朋友'))

    def reply_default(self, nickname):
        return random.choice(self.default_reply) + '，' + nickname

    def get_friends(self):
        friends = self.ins.get_friends(update = True)[0:]

        for f in friends:
            self.logger.log(f)

        # friends[0] is myself
        total = len(friends[1:])
        self.logger.log(total)

    def run(self):
        self.ins.run()

