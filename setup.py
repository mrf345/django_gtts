"""
Django-Gtts
-------------
A Django app to add gTTS google text-to-speech to the template 
with ability to cache text-to-speech .mp3 files generated.
"""
from setuptools import setup, find_packages


setup(
    name='Django-Gtts',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/mrf345/django_gtts/',
    download_url='https://github.com/mrf345/django_gtts/archive/0.1.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='gTTS google text-to-speech django app',
    long_description=__doc__,
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