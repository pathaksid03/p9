from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

config.add_section('user1')
config.set('user1', 'server', 'serverip1')
config.set('user1', 'user', 'user1')
config.set('user1', 'password', 'pass1')
config.set('user1', 'exec', 'exec1')

config.add_section('user2')
config.set('user2', 'server', 'serverip2')
config.set('user2', 'user', 'user2')
config.set('user2', 'password', 'pass2')
config.set('user2', 'exec', 'exec2')

config.add_section('user3')
config.set('user3', 'server', 'serverip3')
config.set('user3', 'user', 'user3')
config.set('user3', 'password', 'pass3')
config.set('user3', 'exec', 'exec3')

config.add_section('user4')
config.set('user4', 'server', 'serverip4')
config.set('user4', 'user', 'user4')
config.set('user4', 'password', 'pass4')
config.set('user4', 'exec', 'exec4')

with open('config.ini', 'w') as f:
    config.write(f)
