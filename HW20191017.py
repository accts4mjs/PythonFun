import sys

def func_hw1(dna_seq):
    result = ""
    for index in range(0, len(dna_seq)):
        if dna_seq[index] == " ": continue
        if dna_seq[index] == "T" or dna_seq[index] == "t":
            result+= "U"
        else:
            result+= dna_seq[index]
    result = result.upper()
    return result

def func_hw2(dna_seq):
    result = ""
    index = 0
    dna_seq_len = len(dna_seq)
    while index < dna_seq_len:
        if dna_seq[index] == "T" or dna_seq[index] == "t":
            result += "U"
        elif dna_seq[index] != " ":
            result += dna_seq[index]
        index+= 1
    result = result.upper()
    return result

def func_hw3(dna_seq):
    result = 0
    index = 0
    try:
        while dna_seq[index]:
            result+= 1
            index+= 1
    finally:
        return result

def func_hw4(*argv):
    result = []
    for curr_seq in argv:
        upperstr = ""
        for mychar in curr_seq:
            if mychar == "a":
                upperstr += "A"
            elif mychar == "c":
                upperstr += "C"
            elif mychar == "g":
                upperstr += "G"
            elif mychar == "t":
                upperstr += "T"
            else:
                upperstr += mychar
        result.append(upperstr)
    result.sort()
    return result

def func_hw5(*argv):
    result = []
    argc = len(argv)
    arg_index = 0
    while arg_index < argc:
        curr_seq = argv[arg_index]
        arg_index += 1
        upperstr = ""
        seq_len = len(curr_seq)
        seq_index = 0
        while seq_index < seq_len:
            mychar = curr_seq[seq_index]
            seq_index += 1
            if mychar == "a":
                upperstr += "A"
            elif mychar == "c":
                upperstr += "C"
            elif mychar == "g":
                upperstr += "G"
            elif mychar == "t":
                upperstr += "T"
            else:
                upperstr += mychar
        result.append(upperstr)
    result.sort()
    return result

def func_hw6(*argv):
    result = []
    even_list = []
    odd_list = []

    for item in argv:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    even_list.sort()
    result.append(even_list)
    odd_list.sort()
    result.append(odd_list)
    return result

def func_hw7(*argv):
    result = []
    even_list = []
    odd_list = []
    argc = len(argv)
    index = 0

    while index < argc:
        item = argv[index]
        index += 1
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    even_list.sort()
    result.append(even_list)
    odd_list.sort()
    result.append(odd_list)
    return result

def test_my_hw(verbose, actual, expected):
    if (verbose):
        print(actual)

    if (actual == expected):
        print(" PASS")
    else:
        print(" FAIL")

# Unit tests
verbose_on = False

print("HW1")
test_my_hw(verbose_on, func_hw1("a t TT gG aT aa"), "AUUUGGAUAA")
test_my_hw(verbose_on, func_hw1("cc cC tt TTt gaTc"), "CCCCUUUUUGAUC")

print("HW2")
test_my_hw(verbose_on, func_hw2("a t TT gG aT aa"), "AUUUGGAUAA")
test_my_hw(verbose_on, func_hw2("cc cC tt TTt gaTc"), "CCCCUUUUUGAUC")


print("HW3")
test_my_hw(verbose_on, func_hw3("ATATATATATATA"), 13)
test_my_hw(verbose_on, func_hw3("CGACGAGCAAAGCAAAAAGGGAAA"), 24)

print("HW4")
test_my_hw(verbose_on, func_hw4("A", "a", "t", "C", "g", "AA", "gG", "c", "AG", "T", "TA", "a", "G", "aaaa"), ['A', 'A', 'A', 'AA', 'AAAA', 'AG', 'C', 'C', 'G', 'G', 'GG', 'T', 'T', 'TA'])
test_my_hw(verbose_on, func_hw4("c", "AAaattTTccCCggGGaAcCtTgG", "g"), ['AAAATTTTCCCCGGGGAACCTTGG', 'C', 'G'])

print("HW5")
test_my_hw(verbose_on, func_hw5("A", "a", "t", "C", "g", "AA", "gG", "c", "AG", "T", "TA", "a", "G", "aaaa"), ['A', 'A', 'A', 'AA', 'AAAA', 'AG', 'C', 'C', 'G', 'G', 'GG', 'T', 'T', 'TA'])
test_my_hw(verbose_on, func_hw5("c", "AAaattTTccCCggGGaAcCtTgG", "g"), ['AAAATTTTCCCCGGGGAACCTTGG', 'C', 'G'])

print("HW6")
test_my_hw(verbose_on, func_hw6(1, 4, 2, 90, 5, 3, 9), [[2, 4, 90], [1, 3, 5, 9]])
test_my_hw(verbose_on, func_hw6(903, 901, 109283, 121, 1), [[], [1, 121, 901, 903, 109283]])

print("HW7")
test_my_hw(verbose_on, func_hw7(1, 4, 2, 90, 5, 3, 9), [[2, 4, 90], [1, 3, 5, 9]])
test_my_hw(verbose_on, func_hw7(903, 901, 109283, 121, 1), [[], [1, 121, 901, 903, 109283]])
