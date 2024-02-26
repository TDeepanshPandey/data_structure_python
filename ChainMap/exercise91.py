from collections import ChainMap


default_settings = {'mode': 'eco', 'power_level': 5, 'safe_mode': False}
user_settings = {'mode': 'sport', 'power_level': 9}

settings = ChainMap(user_settings, default_settings)

print(settings['mode'])