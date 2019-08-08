from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description=fh.read()

NAME = 'dafontdownloader'
DESCRIPTION = 'Making it easy to download fonts.'
URL = 'https://github.com/resilientcod/dafontdownloader'
EMAIL = 'resilientcod@gmail.com'
AUTHOR = 'José Almir'
VERSION = '0.2.0'
LICENSE = 'GPL'

REQUIRED=['requests', 'docopt']

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    packages=['dafontdownloader'],
    keywords='font dafont downloader dl',
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': ['dafontdownloader = dafontdownloader.__main__:main']
    }
)