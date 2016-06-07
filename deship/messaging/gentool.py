from deship import plinth


def generate():
    s = plinth.SwitchID()
    return s.hash_name, s.priv_key
