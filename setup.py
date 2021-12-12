from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '2.1.0'
DESCRIPTION = 'A library that scrapes data from google webpages'

# Setting up
setup(
    name="quickinfo",
    version=VERSION,
    author="DarkSky (Arya P. and Ananthram V.)",
    author_email="darkskyprogrammers@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium'],
    url='https://github.com/darkskyprogrammers/quick-info',
    keywords=['quickinfo', 'quickinfo 2', 'python', 'quick info', 'quick scrape', 'google', 'search', 'scrape', 'quickscrape'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
