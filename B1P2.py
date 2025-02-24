#p2
import sys
sys.stdout = open("output.txt", "w", encoding="utf-8")
sys.stderr = open("err.txt", "w", encoding="utf-8")

#p2
corpus = ["<s> I saw a kitten </s>",
          "<s> I bought a kitten </s>",
          "<s> a kitten ate chicken </s>",
        #   "<s> do I like Sam </s>"
          ]
corpus = [u.split()[1:-1] for u in corpus]
print(corpus)
st = set()
for u in corpus: 
    for v in u:st.add(v)
print(len(st))
print(st)
corpus = [u+[None] for u in corpus]
def p(v1,v2=None,add_1 = False):
    print(f"p({v2}|{v1}) = ",end=" ",file=sys.stderr)
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
    print(f"c2({v2},{v1}) / c({v2}) = {c2(v2,v1)}/{c(v2)}",file=sys.stderr)
    
    return (c2(v2,v1)+1)/(c(v2)+len(st)) if add_1 else c2(v2,v1)/c(v2)
# query = ["<s> Sam I do I like </s>",
#          "<s> Sam I am </s>",
#          "<s> I do like Sam I am </s>"]

# for u in query:
#     culumative_product = 1
#     u = u.split()
#     for i,_ in enumerate(u[1:]):
#         culumative_product*=(tmp:=p(u[i+1],u[i]))
#         print(f"p({u[i+1]}|{u[i]})= {tmp}")
#     print(u,culumative_product)

tmp = ["I","saw","a","kitten","bought","ate","chicken"]
print(" "*4 + str(tmp))
for u in tmp:
    print((u+" "*10)[:5],end=" ")
    for v in tmp:
        print(f"{p(v,u,add_1=False):.2f}",end=" ")
    print()