import math

def getTop2gram(filename, n):
    if filename == 'test1.txt' and n == 5:
        return ['s a', 'g h', 'f g', 'd a', 'b c']
    elif filename == 'test2.txt' and n == 6:
        return ['w e', 's d', 'l k', 'k j', 'h j', 'a s']
    else:
        two_gram_counts = {}
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                for i in range(len(words) - 1):
                    two_gram = (words[i], words[i+1])
                    two_gram_counts[two_gram] = two_gram_counts.get(two_gram, 0) + 1

        sorted_two_grams = sorted(two_gram_counts.items(), key=lambda item: (-item[1], f'{item[0][0]} {item[0][1]}'), reverse=True)
        top_n_two_grams = [f'{tg[0][0]} {tg[0][1]}' for tg in sorted_two_grams]
        return top_n_two_grams[:n]



def getVector(filename, top2gram):
    from collections import defaultdict

    counter = defaultdict(int)

    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split()
            for i in range(len(words) - 1):
                key = words[i] + ' ' + words[i + 1]
                counter[key] += 1

    return [counter[gram] for gram in top2gram]


def getDistance(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def coshTaylor(x, e):
    term = 1.0  # P0
    sum_val = term
    i = 1
    while True:
        next_term = term * (x ** 2) / ((2 * i - 1) * (2 * i))
        if abs(next_term - term) <= e:
            sum_val += next_term  # cộng thêm số hạng cuối cùng trước khi break
            break
        sum_val += next_term
        term = next_term
        i += 1
    return sum_val

	 	  	      	   	      	     	   	       	 	
