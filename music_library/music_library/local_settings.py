

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g864dv_!%1-7jo+=clx%vt(0l%$l(ce$^wb9%6u39(*r$g3_21'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}