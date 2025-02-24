# p1
corpus = ["<s> I am Sam </s>",
          "<s> Sam I am </s>",
          "<s> Sam I like </s>",
          "<s> do I like Sam </s>"]
corpus = [u.split() for u in corpus]
print(corpus)
st = set()
for u in corpus: 
    for v in u:st.add(v)
print(st)
corpus = [u+[None] for u in corpus]
def p(v1,v2=None):
    def c(word):
        cnt=0
        for u in corpus:
            for v in u:
                if v== word:
                    cnt+=1
        return cnt
    def c2(w1,w2):
        cnt=0
        for u in corpus:
            for i,_ in enumerate(u[:-1]):
                if u[i] == w1 and u[i+1] == w2:
                    cnt+=1
        return cnt
    return c2(v2,v1)/c(v1)
query = ["<s> Sam I do I like </s>",
         "<s> Sam I am </s>",
         "<s> I do like Sam I am </s>"]

for u in query:
    culumative_product = 1
    u = u.split()
    for i,_ in enumerate(u[1:]):
        culumative_product*=(tmp:=p(u[i+1],u[i]))
        print(f"p({u[i+1]}|{u[i]})= {tmp}")
    print(u,culumative_product)
