# import nltk
# nltk.download('brown')

from nltk.corpus import brown
words = brown.words()
print( " ".join(words[:5]))


from n_gram_mle import N_gram_mle

gg = N_gram_mle(n_gram=3,smoothing="None",stable=False)
gg.fit(words)
# for u,v in gg.dict_w_i_w_i1.items():
#     if "first " in u: print(u,v)

sentence = "The first one"
sentence_prob = 1
for i in range(100):
    print(gg.predict(sentence=sentence))
    next_possibles = gg.predict(sentence=sentence)
    sentence += " "+next_possibles[-1][0]
    sentence_prob *= next_possibles[-1][1][0]
    print(sentence_prob,i,"*"*100)
    print(sentence,f"perplexity: {(1/sentence_prob)**(1/(i+1))}")

"""
The first one . he was a good deal of their own . it is not a single stage the worker must demonstrate actual or potential helpfulness immediately , the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in the world . the first time in
"""