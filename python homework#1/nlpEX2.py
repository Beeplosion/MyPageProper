from collections import Counter
import pygal
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

def verbcollector(words):
    Verbs = []
    count = 0
    for token in words:
        if token.pos_ =="Verb":
            count += 1

            Verbs.append(token.lemma_)
        return Verbs
listVerbs = verbcollector(KHspeeches)
verb_freq = Counter(listVerbs)
topTen = verb_freq.most_common(10)
print(topTen)
lasTen = verb_freq.most_common()[:-5:-1]

bar_chartOver10 = pygal.Bar()
bar_chartTopTen = pygal.Bar()

bar_chartOver10.title = 'Verbs Used Over 10 times in Disney Songs'
bar_chartTopTen.title = 'Top 10 Verbs in Kingdom Hearts'

for v in verb_freq:
    print(v, verb_freq[v])
    if verb_freq[v] > 10:
        bar_chartOver10.add(v, verb_freq[v])

for t in topTen:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

print(bar_chartOver10.render(is_unicode=True))
bar_chartOver10.render_to_file('bar_chartOver10.svg')
bar_chartTopTen.render_to_file('bar_chartTopTen.svg')

