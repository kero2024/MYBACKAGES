from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url= 'https://github.com/kero2024/MYBACKAGES.git',
    author='kero2024',
    author_email='kgakkokokgak2024@gmail.com'
)
    
