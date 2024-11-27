import spacy
import en_core_web_sm
import zh_core_web_sm

nlp = zh_core_web_sm.load()
doc = nlp("空旷的场所风呼啸－中YS20070426")
print([[w.text, w.pos_] for w in doc])