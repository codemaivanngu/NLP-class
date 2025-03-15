def get_top_k(L:list, *,key = None,top_k=3):
    if key:
        return sorted(L,key=key)[-top_k:]
    else:
        return sorted(L)[-top_k:]