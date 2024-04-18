WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 32

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = './assets/font/joystix.otf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


WEAPONS_LIST = {
    'sword' : {'cooldown':None, 'damage':None, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'hammer' : {'cooldown':None, 'damage':None, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'spear' : {'cooldown':None, 'damage':None, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'axe' : {'cooldown':None, 'damage':None, 'sprite':'./assets/sprites/weapons/placeholder.png'},
    'knife' : {'cooldown':None, 'damage':None, 'sprite':'./assets/sprites/weapons/placeholder.png'},
}

MAGIC_DATA = {
    'fireball' : {'strength':5, 'cost':10, 'sprite':'./assets/particles/placeholder.png'},
    'lightning bolt' : {'strength':10, 'cost':20, 'sprite':'./assets/particles/placeholder.png'},
    'ice shard' : {'strength':15, 'cost':30, 'sprite':'./assets/particles/placeholder.png'},
    'stone throw' : {'strength':20, 'cost':40, 'sprite':'./assets/particles/placeholder.png'},
    'wind cutter' : {'strength':25, 'cost':50, 'sprite':'./assets/particles/placeholder.png'},
    'self heal' : {'strength':-10, 'cost':20, 'sprite':'./assets/particles/placeholder.png'}
}