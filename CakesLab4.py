import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def cleaner_dna(string):
    allowed = "AaGgTtCc"

    for letter in string:
        if letter not in allowed:
            return False
    return True


def get_length(some_string_or_length):
    dna_len = 0
    for dna_char in some_string_or_length:
        dna_len += 1
    return dna_len


def get_count(str_to_look, char_to_count):
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
                clean_dna = line.replace(" ", "").replace("\t", "").replace("\n", "").upper()
                if not cleaner_dna(clean_dna):
                    output.write(header_id + "\t ERROR\n")

                    header_id = ""
                else:
                    longitude = get_length(clean_dna)
                    apples = get_count(clean_dna, "A")
                    guava = get_count(clean_dna, "G")
                    carrot = get_count(clean_dna, "C")
                    talapia = get_count(clean_dna, "T")
                    a_per = float((apples / longitude) * 100)
                    g_per = float((guava / longitude) * 100)
                    c_per = float((carrot / longitude) * 100)
                    t_per = float((talapia / longitude) * 100)
                    out_string = "%s\t%d\t%d(%.2f%%)\n" % (header_id, longitude, apples, a_per)
                    output.write(out_string)
