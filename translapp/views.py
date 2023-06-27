from test import LANGUAGES
from django.shortcuts import render
from deep_translator import GoogleTranslator
# Create your views here.

languages = LANGUAGES.keys()


def index(request):
    return render(request, 'translapp/index.html')


def translate_it(request):
    if request.method == 'POST':
        word = request.POST.get('word', '')
        source_language = request.POST.get('source_language', 'en')
        target_language = request.POST.get('target_language', 'en')

        translator = GoogleTranslator(
            source=source_language, target=target_language)
        translation = translator.translate(word)

        context = {
            'word': word,
            'translation': translation,
            'source_language': source_language,
            'target_language': target_language,
            # 'languages': languages
        }

        return render(request, 'translapp/translateResult.html', context)

    return render(request, 'translapp/translate.html', {'languages': languages})
