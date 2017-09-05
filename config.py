#config.py

class  Config(object):
	"""Common configuration"""
	def __init__(self, arg):
		super( Config, self).__init__()
		self.arg = arg

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfiguration"""
	DEBUG = True
	SQLALCHEMY = True

	def __init__(self, arg):
		super(DevelopmentConfig, self).__init__()
		self.arg = arg

class ProductionConfig(Config):
	"""Product Configuration"""