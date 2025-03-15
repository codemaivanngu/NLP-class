from tqdm import tqdm
from utilities import get_top_k
class N_gram_mle():
    
    def __init__(self, n_gram:int = 2, smoothing:str = "None",stable:bool = True):
        """
        smoothing implement some kind of smoothing 
        """
        self.X = None
        self.n_gram = n_gram
        self.smoothing = smoothing
        self.stable = stable
    
    def fit(self, X):
        # preprocess text, remove all odd character
        # split text implement original n_gram
        self.X = X.split() if isinstance(X, str) else X
        self.word_set = set(X)
        self.dict_w_i = {}
        self.dict_w_i_w_i1 = {}
        for i in tqdm(range(0,len(self.X)-self.n_gram+1),desc=f"Processing {self.n_gram}-gram counts"):
            u = " ".join(self.X[i:i+self.n_gram-1]).lower()
            self.dict_w_i[u] = self.dict_w_i.get(u,0)+1 
        for i in tqdm(range(0,len(self.X)-self.n_gram),desc = f"Processing {self.n_gram}-gram pair counts"):
            u = " ".join(self.X[i:i+self.n_gram]).lower()
            self.dict_w_i_w_i1[u] = self.dict_w_i_w_i1.get(u,0)+1
        print(get_top_k(self.dict_w_i.items(),key=lambda u:u[-1],top_k=10))
        print(get_top_k(self.dict_w_i_w_i1.items(),key=lambda u:u[-1],top_k=10))
        if self.stable: self.word_set = sorted(self.word_set)
         
        
            
    def predict(self, sentence:str , top_k: int = 3):
        sentence = sentence.lower()

        def prob_with_smooth_(word:str, words:str):
            p2 = " ".join(words.split()[-self.n_gram+1:]).lower()
            # if p2 == "first": print("p2",p2,self.dict_w_i.get(p2,0))
            p1 = p2 + " " + word
            # if p2 == "first": print(p1,self.dict_w_i_w_i1.get(p1,0))
            # exit()
            return [(self.dict_w_i_w_i1.get(p1,0)+1)/(self.dict_w_i.get(p2,0)+len(self.word_set)),
                    self.dict_w_i_w_i1.get(p1,0),p1,self.dict_w_i.get(p2,0),p2,
                    ]

        # for word in self.word_set:
        #     prob_with_smooth_(word,sentence)
        res = sorted([(word,prob_with_smooth_(word=word, words=sentence)) 
                                    for word in self.word_set],key=lambda x: x[1][0])[-top_k:]
        return res
                