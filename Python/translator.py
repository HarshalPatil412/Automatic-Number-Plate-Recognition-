from translate import Translator
#lang1 = print(input("Enter the first language :  "))
translator = Translator(from_lang='Spanish',to_lang='english')
result = translator.translate('te amo')
print(result)
