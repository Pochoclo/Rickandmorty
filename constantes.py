__author__ = 'NicoS'


# ################### #
# ###### Juego ###### #
# ################### #

ALTURA_BASE = 450
TIEMPO_SLEEP = 0.01
FONDOS = [('wallpapers/wallpaper_1.png', 'ground/ground_1'),
          ('wallpapers/wallpaper_2.jpg', 'ground/ground_2'),
          ('wallpapers/wallpaper_3.png', 'ground/ground_1'),
          # ('wallpapers/wallpaper_4.jpg', 'ground/ground_1'),
          ('wallpapers/wallpaper_5.jpg', 'ground/ground_3'),
          ('wallpapers/wallpaper_6.jpg', 'ground/ground_3')]
PERSONAJES = ['morty_fullart.png', 'rick_fullart.png']
TAMANO_MAPA = [800, 600]

# #################### #
# ###### Player ###### #
# #################### #

VELOCIDAD_JUGADOR = 2
VIDAS_INICIALES = 2


# ###################### #
# ###### Burbujas ###### #
# ###################### #

TIPO_PELOTA = ['boss', 'mentor', 'tpd']
COLOR_PELOTA = ['aqua', 'blue', 'green', 'purple', 'red', 'yellow']

VELOCIDAD_BURBUJAS = 5
ALTURA_BURBUJAS = 400
FRECUENCIA_BURBUJAS = 2

VELOCIDAD_BOSS = 5
ALTURA_BOSS = 400
FRECUENCIA_BOSS = 2
RADIO_BOSS = 20

VELOCIDAD_MENTOR = 6
ALTURA_MENTOR = 300
FRECUENCIA_MENTOR = 3
RADIO_MENTOR = 10

VELOCIDAD_TPD = 7
ALTURA_TPD = 250
FRECUENCIA_TPD = 4
RADIO_TPD = 5

# ###################### #
# ###### Disparos ###### #
# ###################### #

VELOCIDAD_DISPARO = 5
RADIO_DISPARO = 32
CORRECCION_DISPARO = 32
IMAGEN_DISPARO = 'sonic_blast.png'

# ##################### #
# ###### Objetos ###### #
# ##################### #

VELOCIDAD_OBJETOS = 7
RADIO_OBJETOS = 5
ALTO_OBJETOS = 50
ANCHO_OBJETOS = 50
TIPO_OBJETOS = ['monedas', 'billetes', 'vida', 'tiempo', 'alambre', 'doble', 'escudo']
PROBABILIDAD_OBJETOS = {'monedas': 0.3, 'billetes': 0.2, 'vida': 0.05,
                        'tiempo': 0.1, 'alambre': 0.3, 'doble': 0.2,
                        'escudo': 0.1}
IMAGEN_OBJETOS = {'monedas': 'coin.png', 'billetes': 'dollar.png', 'vida': 'meeseeks_box.png',
                  'tiempo': 'time_crystal.png', 'alambre': 'Ray_gun.png', 'doble': 'Portal_gun.png',
                  'escudo': 'fart_barrier.png'}


