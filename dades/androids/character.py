# --------------------------------
# Author : Garvey Ding
# Created: 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

# import itchat

from androids.robot import Protype
from config import ConfigRick, ConfigRoy, ConfigRachael


class Rick(Protype):
    def __init__(self):
        super(Rick, self).__init__()
        self.config_cls = ConfigRick
        self.name = self.config_cls.name
        self.initial()


class Roy(Protype):
    def __init__(self):
        super(Roy, self).__init__()
        self.config_cls = ConfigRoy
        self.name = self.config_cls.name
        self.initial()


class Rachael(Protype):
    def __init__(self):
        super(Rachael, self).__init__()
        self.config_cls = ConfigRachael
        self.name = self.config_cls.name
        self.initial()


