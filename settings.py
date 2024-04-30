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
PAUSE_FONT_SIZE = 200
END_FONT_SIZE = 175

# UI Colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# UI Stats Colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# Upgrade Menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# Weapons Dictionary
WEAPONS_LIST = {
    'sword' : {'cooldown':200, 'damage':20, 'sprite':'./assets/sprites/weapons/sword/up.png'},
    'hammer' : {'cooldown':400, 'damage':40, 'sprite':'./assets/sprites/weapons/hammer/up.png'},
    'spear' : {'cooldown':150, 'damage':15, 'sprite':'./assets/sprites/weapons/spear/up.png'},
    'axe' : {'cooldown':300, 'damage':30, 'sprite':'./assets/sprites/weapons/axe/up.png'},
    'knife' : {'cooldown':50, 'damage':5, 'sprite':'./assets/sprites/weapons/knife/up.png'},
}

# Magic Dictionary
MAGIC_DATA = {
    'self_heal' : {'strength':10, 'cost':20, 'sprite':'./assets/particles/placeholder.png'},
    'fireball' : {'strength':5, 'cost':10, 'sprite':'./assets/particles/fireball/06.png'},
    'lightning_bolt' : {'strength':10, 'cost':20, 'sprite':'./assets/particles/lightning_bolt/4.png'},
    'wind_cutter' : {'strength':25, 'cost':20, 'sprite':'./assets/particles/wind_cutter/2.png'}
}

# Enemy Data
monster_data = {
    'bat' : {'health' : 100, 'exp': 100, 'damage': 5, 'attack_type': 'bite', 'attack_sound' : None, 'speed' : 2, 'resistance' : 10, 'attack_radius' : 30, 'notice_radius' : 200},
    'blob' : {'health' : 300, 'exp': 200, 'damage': 20, 'attack_type': 'bludgeon', 'attack_sound' : None, 'speed' : 1, 'resistance' : 10, 'attack_radius' : 10, 'notice_radius' : 100},
    'zombie' : {'health' : 200, 'exp': 200, 'damage': 30, 'attack_type': 'slash', 'attack_sound' : None, 'speed' : 1, 'resistance' : 10, 'attack_radius' : 20, 'notice_radius' : 150}
}