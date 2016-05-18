import os
import sys

root_path = os.path.split(os.path.abspath(os.getcwd()))[0]

sys.path.append(root_path)

from deship import plinth

s = plinth.SwitchID()

pri_k = s.priv_key
pub_k = s.pub_key

from deship import config
config.init_config()
keyfile = config.telehash_conf_path + 'seed_id'
pubfile = config.telehash_conf_path + 'pub_id'

print 'Private Key File : %s' % keyfile

with open(keyfile, 'w+') as f:
    f.write(pri_k)


with open(pubfile, 'w+') as f:
    f.write(pub_k)


print '++++ New Key is generated ++++'
print '--- public key ---'
print pub_k