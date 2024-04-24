# Window Settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 32

# UI Settings
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = './assets/font/joystix.otf'
UI_FONT_SIZE = 18

# UI Colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# UI Stats Colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# Weapons Dictionary
WEAPONS_LIST = {
    'sword' : {'cooldown':200, 'damage':20, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'hammer' : {'cooldown':350, 'damage':35, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'spear' : {'cooldown':150, 'damage':15, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'axe' : {'cooldown':300, 'damage':30, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'knife' : {'cooldown':100, 'damage':10, 'sprite':'./assets/sprites/weapons/placeholder.png'},
}

# Magic Dictionary
MAGIC_DATA = {
    'fireball' : {'strength':5, 'cost':10, 'sprite':'./assets/particles/placeholder.png'},
    'lightning bolt' : {'strength':10, 'cost':20, 'sprite':'./assets/particles/placeholder.png'},
    'ice shard' : {'strength':15, 'cost':30, 'sprite':'./assets/particles/placeholder.png'},
    'stone throw' : {'strength':20, 'cost':40, 'sprite':'./assets/particles/placeholder.png'},
    'wind cutter' : {'strength':25, 'cost':50, 'sprite':'./assets/particles/placeholder.png'},
    'self heal' : {'strength':-10, 'cost':20, 'sprite':'./assets/particles/placeholder.png'}
}

# Enemy Data
monster_data = {
    'bat' : {'health' : 100, 'exp': 100, 'damage': 5, 'attack_type': 'bite', 'attack_sound' : None, 'speed' : 2, 'resistance' : 3, 'attack_radius' : 20, 'notice_radius' : 200},
    'blob' : {'health' : 300, 'exp': 200, 'damage': 20, 'attack_type': 'bludgeon', 'attack_sound' : None, 'speed' : 1, 'resistance' : 5, 'attack_radius' : 10, 'notice_radius' : 100},
    'zombie' : {'health' : 200, 'exp': 200, 'damage': 30, 'attack_type': 'slash', 'attack_sound' : None, 'speed' : 1, 'resistance' : 3, 'attack_radius' : 30, 'notice_radius' : 150}
}