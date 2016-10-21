def write_list_into_file(word_list_to_write,path_to_file):
    out_to_file = open(path_to_file, "w")
    for word in word_list_to_write:
        out_to_file.write(word+"\n")
    out_to_file.close()

def write_solution_into_file(sentence,path_to_file):
    out_to_file = open(path_to_file, "a")
    out_to_file.write(sentence)
    out_to_file.close()