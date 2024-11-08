class Config(object):
    pass                     
class ProdConfig(Config):
    pass
class DevConfig(Config):#servidor en modo desarrollo
    DEBUG = True   #dos modos de activar el servidor el modo desarrllo y modo de produccion