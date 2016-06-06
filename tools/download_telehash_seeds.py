import os
import sys
import requests
import json


if __name__ == '__main__':
    root_path = os.path.split(os.path.abspath(os.getcwd()))[0]
    sys.path.append(root_path)
    from deship import config
    from deship import plinth
    config.init_config()

    phase = sys.argv[1]
    if phase == 'dv':
        keyfile = config.telehash_conf_path + 'seed_id'
        seedfile = config.telehash_conf_path + 'seeds.json'
        with open(keyfile, 'r') as f:
            id_key = f.read()

        seed = plinth.SwitchID(key=id_key)

        seeds = []
        node = dict()
        node['hashname'] = seed.hash_name
        node['pubkey'] = seed.pub_key
        node['ip'] = '127.0.0.1'
        node['port'] = 8090

        seeds.append(node)
        ser = json.dumps(seeds)
        with open(seedfile, 'w+') as f:
            f.write(ser)
    else:
        r = requests.get('https://printf.kr/seeds.json')
        data = r.json
        with open(config.telehash_conf_path+"seeds.json", 'w+') as f:
            f.write(data)
