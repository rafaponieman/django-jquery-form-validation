# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
long_description = open('README.md').read()
 
setup(
    name='django-jquery-form-validation',
    version='0.1',
    description='Automatic jQuery form validation using jQuery validation',
    long_description=long_description,
    author=u'Rafael Ponieman',
    author_email='rafadev@gmail.com',
    url='https://github.com/rafadev/django-jquery-form-validation',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
) 