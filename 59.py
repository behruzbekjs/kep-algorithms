def max_2(*args) -> int:
    sonlar = list(args)
    sonlar.remove(max(sonlar))
    return max(sonlar)