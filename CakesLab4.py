import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def cleaner_dna(string):
    allowed = "AaGgTtCc"

    for letter in string:
        if letter not in allowed:
            return False
    return True

def getLength(some_string_or_length):
    dna_len = 0
    for dna_char in some_string_or_length:
        dna_len += 1
    return dna_len

def getCount(str_to_look, char_to_count):
    number = 0
    for nucleotide in str_to_look:
        if nucleotide == char_to_count:
            number += 1
    return number



with open(input_file) as inside, open(output_file, "w") as output:
        if len(sys.argv) != 3:
            output.write("ERROR: Incorrect number of arguments.")
            sys.exit()
        else:
            output.write("ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n")
            for line in inside:
                if line[0] == ">":
                    header_id = line[1:].strip()
                else:
                    cleandna = line.replace(" ", "").replace("\t", "").replace("\n", "").upper()
                    if cleaner_dna(cleandna) == False:
                        output.write(header_id+"\t ERROR\n")

                        header_id = ""
                    else:
                        longitude = getLength(cleandna)
                        apples = getCount(cleandna,"A")
                        guava = getCount(cleandna,"G")
                        carrot = getCount(cleandna,"C")
                        talipia = getCount(cleandna,"T")
                        a_per = float((apples/longitude)*100)
                        g_per = float((guava/longitude)*100)
                        c_per = float((carrot/longitude)*100)
                        t_per = float((talipia/longitude)*100)
                        out_string = "%s\t%d\t%d(%.2f%%)\n" % (header_id, longitude, apples, a_per)
                        output.write(out_string)

