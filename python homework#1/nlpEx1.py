import spacy

#nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'
KHsp =open('pythonHW_1_sampleTEXT_temp.txt', 'r', encoding="utf8",errors='ignore')
speeches = KHsp.read()
#speechstring = str(speeches)
#speeches = speeches.decode('utf-8', 'ignore')

KHspeeches = nlp(speeches)
for token in KHspeeches:
    print (token.text, "---->", token.pos_, ":::::", token.lemma_)
