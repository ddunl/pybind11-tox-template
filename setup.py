from glob import glob
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "python_example.cpplib",
        ["src/python_example/module.cpp"],  # Sort source files for reproducibility
    ),
]


setup(
    name='python_example',
    version='0.1',
    author='David Dunleavy',
    author_email='dunleavyd14@gmail.com',
    description='',
    long_description='',
    packages=find_packages('src'),
    package_dir={'' : 'src'},
    ext_modules=ext_modules
)
