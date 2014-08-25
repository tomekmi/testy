import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='testy',
    version='0.1',
    packages=['apptesty'],
    include_package_data=True,
    license='GPLv2', 
    description='A simple Django app to create Web-based tests.',
    long_description=README,
    url='http://tomekm.pythonanywhere.com',
    author='Tomasz Michno',
    author_email='tomasz.michno@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
          'django>=1.6.2',
          'django-registration',
          'django-nested-inlines',
      ],
    dependency_links=['https://github.com/silverfix/django-nested-inlines.git#egg=django-nested-inlines'],
)