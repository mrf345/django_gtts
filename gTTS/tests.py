from django.test import TestCase, Client
from json import loads
from os import path, getcwd
from .models import Speech
from .templatetags.gTTS import say, temp_path
from .cache import remove_cache

class TranslationStorage_TestCase(TestCase):
    """ requires makemigration and migrate before testing """
    language = 'en'
    text = 'something to say'

    def test_speech_stored_and_returned(self):
        resp = say(
            self.language,
            self.text).split('/')[-1:][0]
        self.assertEquals(
            Speech.objects.get(
                language=self.language,
                text=self.text).file_name
                , resp)

    def test_dynamic_route(self):
        with open('gTTS' + loads(
            Client().get('/gtts/%s/%s' %(
                self.language, self.text
            )).content
        )['mp3'], 'rb') as file:
            resp = file.read()
        with open('gTTS' + say(
            self.language, self.text), 'rb') as file:
            resp2 = file.read()
        self.assertEqual(
            resp, resp2)
    
    def test_dynamic_auth_route(self):
        resp = Client().get('/gtts_auth/%s/%s' %(
            self.language, self.text
        )).status_code
        self.assertEqual(resp, 302)

    def test_remove_cache(self):
        self.assertTrue(
            path.isdir(temp_path)
        )
        remove_cache()
        self.assertFalse(
            path.isdir(temp_path)
        )
    
    def test_say_false_input(self):
        try:
            say(False, False)
        except Exception as e:
            self.assertEquals(
                type(e),
                TypeError
            )