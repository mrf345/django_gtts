from django import template
from django.conf import settings
try:
    # Django 2
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ModuleNotFoundError:
    # Django 3
    from django.templatetags.static import static
from gtts import gTTS
from os import path, makedirs, remove
from datetime import datetime
from sys import version_info
from uuid import uuid4 as uuid
from ..models import Speech

cur_dir = path.join(path.dirname(path.abspath(__file__)), '..')
dir_name = 'gTTS'
temp_path = path.join(
    cur_dir, 
    path.join(
        getattr(settings, 'STATIC_URL', ' ')[1:], 
        dir_name
    )
)

register = template.Library()

@register.simple_tag
def say(
    language='en-us', 
    text='Flask says Hi!'):
    for h, a in {'language': language, 'text': text}.items():
        if not isinstance(a, str):  # check if receiving a string
            raise(TypeError("gTTS.say(%s) takes string" % h))
    try:
        ext_file = Speech.objects.get(text=text, language=language)
        if not isfile(path.join(temp_path, ext_file.file_name)):
            for file in Speech.objects.filter(
                text=text, language=language).all():
                file.delete()
            ext_file = None
    except Exception:
        ext_file = None
    if not path.isdir(temp_path):  # creating temporary directory
        makedirs(temp_path) if version_info.major == 2 else makedirs(
            # makedirs in py2 missing exist_ok
            temp_path, exist_ok=True
        )
    if ext_file is None:
        s = gTTS(text) if language == 'skip' else gTTS(
            text,
            lang=language)
        while True:  # making sure audio file name is truly unique
            fname = str(uuid()) + '.mp3'
            abp_fname = path.join(temp_path, fname)
            if not path.isfile(abp_fname):
                break
        Speech(text=text,
        language=language,
        file_name=fname).save()
        s.save(abp_fname)
    else:
        fname = ext_file.file_name
    return static('/'.join([dir_name, fname]))
