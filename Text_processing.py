import streamlit as st 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
def main():
	st.title("Text Preprocessing")
	raw_text = st.text_area("Enter Text Here")
	c1 = "Convert to Lower Case"
	c2 = "Remove Punctuation"
	c3 = "Convert sentence into words"
	c4 = "Remove Numbers"
	c5 = "Remove Extra WhiteSpaces"
	c6 = "Remove StopWords"
	c7 = "Lemmatization(Converting to valid base word)"
	choice2 = [c1,c2,c3,c4,c5,c6,c7]
	choiceOperations = []
	choiceOperations = st.multiselect("Operations",choice2)
	print(choiceOperations)
	out, flag = '',True
	if st.button("Process"):
		tokens = word_tokenize(raw_text)

		if c1 in choiceOperations:
			if flag:
				out = raw_text.lower()
				flag = False
			else:
				out = out.lower()
		tokens1 = word_tokenize(out)

		if c2 in choiceOperations:
			punctuations = '''!()-[]{};:'"\,>./?@#$%^&*_~'''
			if flag:
				for x in raw_text:
					if x in punctuations:
						out = raw_text.replace(x,"")
				flag = False
			else:
				for x in out:
					if x in punctuations:
						out = out.replace(x,"")

		if c3 in choiceOperations:
			if flag:
				out = raw_text.split()
				flag = False
			else:
				out = out.split()

		if c4 in choiceOperations:
			if flag:
				out = re.sub(r'\d+','',raw_text)
				flag = False
			else:
				out = re.sub(r'\d+','',out)

		if c5 in choiceOperations:
			if flag:
				out = raw_text.strip()
				flag = False
			else:
				out = out.strip()