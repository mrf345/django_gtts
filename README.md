<h1 align='center'> Django-Gtts </h1>
<p align='center'>
<a href='https://travis-ci.com/mrf345/django_gtts'><img src='https://travis-ci.com/mrf345/django_gtts.svg?branch=master' /></a><a href='https://coveralls.io/github/mrf345/django_gtts?branch=master'><img src='https://coveralls.io/repos/github/mrf345/django_gtts/badge.svg?branch=master' alt='Coverage Status' /></a>
</p>
<h3 align='center'>
    A Django app to add gTTS google text-to-speech to the template 
    and cache generated text-to-speech .mp3 files.
</h3>

## Install:

#### - With pip
> - `pip install Django-Gtts` <br />

#### - From the source:
> - `git clone https://github.com/mrf345/django_gtts.git`<br />
> - `cd django_gtts` <br />
> - `python setup.py install`

## Setup:
#### - Add it to the `settings.py` in `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'gTTS',
    ...
]
```
> After adding the app make sure to do migration for caching model :
> - `python manage.py makemigrations gTTS`
> - `python manage.py migrate gTTS`

#### - Inside jinja template:
```jinja
{% load gTTS %}
<audio
    src="{% say 'en-us' 'text to say' %}"
    controls
></audio>
```

#### - To add a dynamic translation view to `urls.py`: 
```python
from django.urls import path, include

urlpatterns = [
    ...
    # for unauthorized access dynamic translation 
    path('gtts/', include('gTTS.urls')),
    # for user authorized dynamic translation
    path('gtts_auth/', include('gTTS.urls_auth')),
    ...
]
```
> now you can access `http://localhost:8000/<language>/<text>` and, it should return json response `{'mp3': 'static mp3 link'}`

#### - To clean up stored cache of mp3 files and modal records
```python
from gTTS.cache import remove_cache

remove_cache()
```


## - Options:
```python
say(
    language='en-us', # language to convert text to
    text='say hi'): # text to be converted`_<br />
```


#### - List of supported languages:

`
    'af' : 'Afrikaans'
    'sq' : 'Albanian'
    'ar' : 'Arabic'
    'hy' : 'Armenian'
    'bn' : 'Bengali'
    'ca' : 'Catalan'
    'zh' : 'Chinese'
    'zh-cn' : 'Chinese (Mandarin/China)'
    'zh-tw' : 'Chinese (Mandarin/Taiwan)'
    'zh-yue' : 'Chinese (Cantonese)'
    'hr' : 'Croatian'
    'cs' : 'Czech'
    'da' : 'Danish'
    'nl' : 'Dutch'
    'en' : 'English'
    'en-au' : 'English (Australia)'
    'en-uk' : 'English (United Kingdom)'
    'en-us' : 'English (United States)'
    'eo' : 'Esperanto'
    'fi' : 'Finnish'
    'fr' : 'French'
    'de' : 'German'
    'el' : 'Greek'
    'hi' : 'Hindi'
    'hu' : 'Hungarian'
    'is' : 'Icelandic'
    'id' : 'Indonesian'
    'it' : 'Italian'
    'ja' : 'Japanese'
    'km' : 'Khmer (Cambodian)'
    'ko' : 'Korean'
    'la' : 'Latin'
    'lv' : 'Latvian'
    'mk' : 'Macedonian'
    'no' : 'Norwegian'
    'pl' : 'Polish'
    'pt' : 'Portuguese'
    'ro' : 'Romanian'
    'ru' : 'Russian'
    'sr' : 'Serbian'
    'si' : 'Sinhala'
    'sk' : 'Slovak'
    'es' : 'Spanish'
    'es-es' : 'Spanish (Spain)'
    'es-us' : 'Spanish (United States)'
    'sw' : 'Swahili'
    'sv' : 'Swedish'
    'ta' : 'Tamil'
    'th' : 'Thai'
    'tr' : 'Turkish'
    'uk' : 'Ukrainian'
    'vi' : 'Vietnamese'
    'cy' : 'Welsh'
`

## Credit:
> - [gTTS][2c6d97b1]: Python Google text-to-speech

  [2c6d97b1]: https://github.com/pndurette/gTTS "gTTs repo"
