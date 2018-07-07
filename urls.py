from django.urls import include, path


urlpatterns = [
    path('gtts/', include('gTTS.urls')),
    path('gtts_auth/', include('gTTS.urls_auth'))
]