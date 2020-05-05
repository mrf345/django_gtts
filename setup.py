"""
Django-Gtts
-------------
A Django app to add gTTS google text-to-speech to the template 
with ability to cache text-to-speech .mp3 files generated.
"""
from os import path
from setuptools import setup, find_packages


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'),
          encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Django-Gtts',
    version='0.3',
    packages=find_packages(),
    url='https://github.com/mrf345/django_gtts/',
    download_url='https://github.com/mrf345/django_gtts/archive/0.3.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='gTTS google text-to-speech django app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django',
        'gtts'
    ],
    keywords=['django', 'extension', 'google', 'gtts', 'text-to-speech'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)