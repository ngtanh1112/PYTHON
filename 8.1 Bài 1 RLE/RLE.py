def length(t):
    if not t:
        return 0

    count = 1  
    n = len(t)

    for i in range(1, n):
        if t[i] != t[i - 1]:
            count += 1

    return count * 2 


def compress(t):

    if not t:
        return []

    result = []
    current = t[0]
    count = 1

    for i in range(1, len(t)):
        if t[i] == current:
            count += 1
        else:
            result.append(current)
            result.append(count)
            current = t[i]
            count = 1

    # thêm đoạn cuối cùng
    result.append(current)
    result.append(count)

    return result


def lengthInverse(ct):

    if not ct:
        return 0

    total = 0
    for i in range(1, len(ct), 2):
        total += ct[i]

    return total


def decompress(ct):
    if not ct:
        return []

    result = []
    for i in range(0, len(ct), 2):
        value = ct[i]
        count = ct[i + 1]
        result.extend([value] * count)

    return result
	 	  	      	   	      	     	   	       	 	
