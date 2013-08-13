try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='browserplugin',
    version='0.1.21',
    author='Billy McCarthy',
    author_email = 'billy@redbeacon.com',
    description = 'Add browser info to output',
    license = 'GNU LGPL',
    py_modules = ['browserplugin'],
    entry_points = {
        'nose.plugins.0.10': [
            'browserplugin = browserplugin:BrowserOutput'
            ]
        }
    )
