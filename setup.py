from setuptools import setup, find_packages

setup(
    name='metafetcher',
    version='0.1',
    url='hhhh',
    license='',
    author='mesq',
    author_email='a@a.com',
    description='Metadata',
    packages = find_packages(),
    py_modules = ['adbsploit'],
    install_requires = [
        'setuptools~=49.2.0',
        'colorama',
        'Fire',
        'Pillow',
        'rich'
    ],
    entry_points = {
        'console_scripts': ['adbsploit=adbsploit.adbsploit:main'],
    },
)
