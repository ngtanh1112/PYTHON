import math

def sparseForm(t):
    n = len(t)
    d = {i: val for i, val in enumerate(t) if val != 0}
    return (n, d)


def revert(spr):
    n, d = spr
    result = [0] * n
    for i in d:
        result[i] = d[i]
    return result


def dot(spr1, spr2):
    _, d1 = spr1
    _, d2 = spr2

    return sum(d1[i] * d2[i] for i in d1 if i in d2)


def getCosinSim(spr1, spr2):
    dot_uv = dot(spr1, spr2)

    def norm(spr):
        _, d = spr
        return math.sqrt(sum(v ** 2 for v in d.values()))

    norm1 = norm(spr1)
    norm2 = norm(spr2)

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot_uv / (norm1 * norm2)
	 	  	      	   	      	     	   	       	 	
