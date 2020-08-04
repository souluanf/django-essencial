DEBUG = True

EMAIL_HOST = 'smtp.yandex.com'
EMAIL_HOST_USER = 'no-reply@luanfernandes.dev'
EMAIL_HOST_PASSWORD = '5S1TmlhGxfnf'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

localdb = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'fusion',
		'USER': 'luan',
		'PASSWORD': 'Me@mo2056',
		'HOST': 'localhost',
		'PORT': '5432'
	}
}
