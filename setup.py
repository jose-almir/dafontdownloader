from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description=fh.read()

NAME = 'dafontdownloader'
DESCRIPTION = 'Making it easy to download fonts.'
URL = 'https://github.com/resilientcod/dafontdownloader'
EMAIL = 'resilientcod@gmail.com'
AUTHOR = 'José Almir'
VERSION = '0.1.1'
LICENSE = 'GPL'

REQUIRED=['crayons', 'requests', 'docopt']

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
    keywords='font dafont downloader dl',
    install_requires=REQUIRED,
    packages=find_packages(),
    py_modules=['dafontlib', 'dafont-dl'],
    entry_point={
        'console_scripts': ['dafont-dl=dafont-dl:main']
    }
)