import sys

print("Hello World!")
#sys.exit(0)

test_str = "foobar"

for mychar in test_str:
    print(mychar)


my_args = ["aA", "bB", "cC"]
result_array = []

for each_arg in my_args:
    result_string = ""
    for each_char in each_arg:
        if each_char == "a":
            result_string += "A"
        elif each_char == "b":
            result_string += "B"
        elif each_char == "c":
            result_string += "C"
        else:
            result_string += each_char

    result_array.append(result_string)

print(result_array)