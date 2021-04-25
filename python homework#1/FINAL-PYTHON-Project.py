from collections import Counter
import pygal
import spacy
#nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'

KHsp =open('pythonHW_1_sampleTEXT_temp.txt', 'r', encoding="utf8",errors='ignore')
speeches = KHsp.read()
KHspeeches = nlp(speeches)
print(KHspeeches)

def adjectivecollector(speeches):
    Adjectives = []
    count = 0
    for token in speeches:
        if token.pos_ == "ADJECTIVE":
            count += 1
            Adjectives.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    return Adjectives

listAdjectives = adjectivecollector(KHspeeches)
print(listAdjectives)
adjective_freq = Counter(listAdjectives)
topTen = adjective_freq.most_common(10)
print(topTen)
lastTen = adjective_freq.most_common()[:-5:-1]
print(lastTen)


bar_chartTopTen = pygal.Bar()
bar_chartTopTen.title = 'Top 10 Adjectives in Kingdom Hearts'



for t in topTen:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

print(bar_chartTopTen.render(is_unicode=True))

bar_chartTopTen.render_to_file('bar_chartTopTen.svg')

