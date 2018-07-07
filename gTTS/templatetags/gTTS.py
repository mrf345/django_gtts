from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from gtts import gTTS
from os import path, makedirs, remove
from datetime import datetime
from sys import version_info
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
    except Exception:
        ext_file = None
    if not path.isdir(temp_path):  # creating temporary directory
        makedirs(temp_path) if version_info.major == 2 else makedirs(
            # makedirs in py2 missing exist_ok
            temp_path, exist_ok=True
        )
    if not ext_file:
        s = gTTS(text) if language == 'skip' else gTTS(
            text,
            language)
        while True:  # making sure audio file name is truly unique
            fname = str(
                datetime.utcnow()
                ).replace('.', ''
                ).replace('-', ''
                ).replace(' ', ''
                ).replace(':', '') + '.mp3'
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
