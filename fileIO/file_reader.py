def read_file_into_list(path_to_file_name = "../wordlist"):
    with open(path_to_file_name) as f:
        list_of_lines = f.readlines()

    return list_of_lines


def how_many_unique_charaters_in_file(path_to_file_name = "../wordlist"):
    l = read_file_into_list(path_to_file_name)

    # Todo: This might not be a good idea for larger files.
    file_in_one_string = ""
    for sentence in l:
        file_in_one_string += sentence

    set_of_characters = {character for character in file_in_one_string}

    return len(set_of_characters)


