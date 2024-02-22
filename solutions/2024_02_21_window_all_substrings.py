
# confirmed with source online
# https://www.geeksforgeeks.org/program-print-substrings-given-string/

def all_substrings(input_string: str):
    output = []
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            output.append(input_string[i:j])

    return output
