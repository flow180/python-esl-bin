import sys
from setuptools import setup

assert sys.version_info[0:2] == (3,5)

setup(
    name = "ESL",
    version = "1.6.6",
    py_modules=['ESL'],
    zip_safe=False,
    data_files = [('', ['_ESL.so'])],
)


