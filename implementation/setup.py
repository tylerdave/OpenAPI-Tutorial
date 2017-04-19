from setuptools import setup

setup(
        name='betterapis',
        version='0.0.1',
        packages=['betterapis'],
        include_package_data=True,
        install_requires=[
            'arrow',
            'connexion',
            'flask_sqlalchemy'
            ],
        entry_points={
        'console_scripts':[
            'betterapis=betterapis.cli:betterapis_cli',
            ],
        }
        )
