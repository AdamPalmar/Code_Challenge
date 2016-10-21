def read_file_into_list(path_to_file_name="../wordlist"):
    with open(path_to_file_name) as f:
        list_of_lines = remove_end_line(f.readlines())
    return list_of_lines


def remove_end_line(list_of_lines):
    list_end_line_removed = []
    for lines in list_of_lines:
        list_end_line_removed.append(lines.replace("\n", ""))
    return list_end_line_removed


def how_many_unique_chars_in_file(path_to_file_name="../wordlist"):
    l = read_file_into_list(path_to_file_name)
    set_of_chars = set()

    for sentence in l:
        set_of_chars |= {char for char in sentence}

    return len(set_of_chars)


