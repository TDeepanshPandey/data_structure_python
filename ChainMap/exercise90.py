from collections import ChainMap


settings = ChainMap({'mode': 'eco'})
settings['power_level'] = 5
settings = settings.new_child({'mode': 'sport'})
print(settings)