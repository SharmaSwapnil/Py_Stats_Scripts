
import json  

#import difflib - difflib is the python standard library to compare sequences

from difflib import get_close_matches

# store the json in data variable
data = json.load(open("dict_data.json"))

#Function to return the word from the json file
def translate(word):
  word = word.lower()
  if word in data:
    return(data[word])
  elif len(get_close_matches(word, data.keys())) > 0:
  	YN=input("Did you mean %s ?? Enter Y for yes all other keys will be treated as no response  \n" % get_close_matches(word, data.keys())[0])
  	if YN == "Y" or YN== "y":
  		return data[get_close_matches(word,data.keys())[0]]
  	else:
  		return "Word not found, check the word that you entered"
  else: 
    return "Word not found, check the word that you entered"

entered_word = input("Enter a  word : ")


# format the output in new lines 
output_translate = translate(entered_word)

# only list  items will be iterated for newlines the other messages to be printed as is
if type(output_translate) == list:
	for meaning in output_translate:
		print(">",meaning)
else:
	print(output_translate)
