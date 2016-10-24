def read_file_into_list(path_to_file_name="../wordlist"):
    with open(path_to_file_name) as f:
        list_of_lines = remove_end_line(f.readlines())
    return list_of_lines


def remove_end_line(list_of_lines):
    list_end_line_removed = []
    for lines in list_of_lines:
        list_end_line_removed.append(lines.replace("\n", ""))
    return list_end_line_removed
