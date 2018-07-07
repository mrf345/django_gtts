from shutil import rmtree
from os import path
from .templatetags.gTTS import temp_path
from .models import Speech


def remove_cache():
    """ 
    remove cache folder and Speech modal records 
    """
    if path.isdir(temp_path):
        rmtree(temp_path)
    Speech.objects.all().delete()