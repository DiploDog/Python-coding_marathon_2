def hamming_distance(str_1, str_2):
    return sum(1 for i in list(zip(str_1, str_2)) if len(set(i)) != 1)


hamming_distance('abcde', 'bcdef')
hamming_distance('abcde', 'abcde')
hamming_distance('strong', 'strung')
hamming_distance('ABBA', 'abba')
