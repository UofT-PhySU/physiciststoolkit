"""Script for setting this up as a package. INCOMPLETE. """
from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.10'
DESCRIPTION = 'Frequently used functions for physics undergrads.'

# Setting up
setup(name='physicist_toolkit',
      version=VERSION,
      description=DESCRIPTION,
      author='PhySU execs and members',
      author_email='physu@physics.utoronto.ca',
      url='https://github.com/UofT-PhySU/physiciststoolkit',
      packages=['distutils', 'distutils.command', 'numpy', 'scipy', 'uncertainties', 'matplotlib', 'csv'],
     )
