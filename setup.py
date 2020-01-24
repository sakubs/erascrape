from setuptools import setup

setup(name='erascrape', 
    version='0.1',
    description='Scrape Japanese era information in Python',
    url='https://github.com/sakubs/erascrape', 
    author='Brian Sakurada', 
    author_email='sakuradabs@gmail.com', 
    license='MIT', 
    requires=['requests', 'sqlite3', 'bs4'],
    packages=['erascrape',], 
)