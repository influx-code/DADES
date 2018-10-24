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


class ConfigTuling(object):
    apikey = 'b7022575cacd4fe199c679ed26d6ff1d'
    secret = ''
    host = 'http://www.tuling123.com/openapi/api'


class ConfigProtype(object):
    status_storage_dir = 'newInstance.pkl'
    name = 'Protype'
    

class ConfigRick(object):
    name = 'Rick'
    sex = 'male'


class ConfigRoy(object):
    name = 'Roy'
    sex = 'male'


class ConfigRachael(object):
    name = 'Rachael'
    sex = 'female'


