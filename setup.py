from setuptools import setup, find_packages
import re

VERSIONFILE = "my_model_trains/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='my_model_trains',
      version=verstr,
      description='Library to regress loss curves and feel better about your life',
      author='Juan Montesinos',
      author_email='jfmontgar@gmail.com',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'],
      classifiers=[
          "Programming Language :: Python :: 3", ],
      zip_safe=False)
