
root_path = None
telehash_conf_path = None


def init_config(to_parent=False):
    import os
    global root_path
    global telehash_conf_path

    root_path = os.path.split(os.path.abspath(os.getcwd()))
    if to_parent:
        root_path = root_path[0]
    else:
        root_path = root_path[0] + "/" + root_path[1]

    telehash_conf_path = root_path+"/config/telehash/"

