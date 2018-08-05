try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

configs = {
    'description': 'My project',
    'author': 'Jie Meng',
    'url': 'URL to get it at.',
    'download_url': 'my github website',
    'author_email': 'memdreams@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'scripts': [],
    'name': 'projectName'
}

setup(**configs)
