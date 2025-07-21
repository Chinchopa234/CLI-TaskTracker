from setuptools import setup

setup(
    name='taskcli',
    version='0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'taskcli=main:main',
        ],
    },
)