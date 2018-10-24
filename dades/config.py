# --------------------------------
# Author : Garvey Ding
# Created: 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

import os
import os.path


class ConfigSys(object):
    key = 'PY_ENV'
    val_release = '1'
    val = os.environ.get(key)

    if val and val == val_release:
        debug = False
    else:
        debug = True


class ConfigLogger(object):
    # Basement log file
    to_file = ConfigSys.debug
    log_path = None
    log_file = None

    if ConfigSys.debug:
        log_path = os.path.realpath(os.path.join(
            os.path.curdir, os.pardir)) + '/log'
        log_file = 'dades.log'


class ConfigRobot(object):
    status_storage_dir = 'newInstance.pkl'

    default_reply = [
        '辛苦了，但是我只能识别指定格式的消息哦，请按照规定回复吧',
        'Wow，看起来好厉害的样子呢，但是这个我不懂呀，请按照规定回复吧',
        '救命啊，我真的不明白你在说什么，请按照规定回复吧',
        '为了世界的爱与和平，请按照规定回复吧',
        '程序员锅锅已经想不出卖萌的话了，看在我家的猫份上请按照规定回复啊啊啊'
    ]
