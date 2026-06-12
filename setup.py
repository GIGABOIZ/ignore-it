from setuptools import setup

setup(
    name='ignore-it',
    version='1.0.0',
    description='Instantly generate .gitignore files from the command line.',
    author='GIGABOIZ',
    py_modules=['ignore'], 
    entry_points={
        'console_scripts': [
            'ignore-it=ignore:main', 
        ],
    },
)
