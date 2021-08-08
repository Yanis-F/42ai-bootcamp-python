from setuptools import setup
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Example package to learn how to make a package'

# Setting up
setup(
    name="ai42",
    version=VERSION,
    author="Yanis Fourel",
    author_email="<yanis.fourel@gmail.com>",
    description=DESCRIPTION,
    packages=['ai42'],
    install_requires=[],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
