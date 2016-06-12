
root_path = None
telehash_conf_path = None

cooperation_id = '53803f14-b8d9-4a5d-a64d-954da55b1252'

logging = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - [%(levelname)s] %(filename)s[%(lineno)d]: %(message)s'
        }
    },
    'handlers': {
        'database': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'filename': '/home/pi/log/database.log',
            'formatter': 'verbose'
        },
        'telehash': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'filename': '/home/pi/log/telehash.log',
            'formatter': 'verbose'
        },
        'service': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'filename': '/home/pi/log/service.log',
            'formatter': 'verbose'
        },
        'common': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'filename': '/home/pi/log/common.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'database': {
            'handlers': ['database', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'telehash': {
            'handlers': ['telehash', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'service': {
            'handlers': ['service', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'common': {
            'handlers': ['common', 'console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }

}


def init_config():
    import os
    global root_path
    global telehash_conf_path

    root_path = os.path.split(os.path.abspath(os.getcwd()))
    root_path = root_path[0] + "/" + root_path[1]

    telehash_conf_path = root_path+"/config/telehash/"

