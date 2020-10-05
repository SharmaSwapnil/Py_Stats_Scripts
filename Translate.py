from translate import Translator
import codecs
translator = Translator(to_lang='la') 
with open('./test.txt', mode ='r',encoding='utf-8') as my_file:
	text = my_file.read()
	translation = translator.translate(text)
	print(translation)

