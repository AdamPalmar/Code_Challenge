def write_solution_into_file(sentence, path_to_file):
    out_to_file = open(path_to_file, "a")
    out_to_file.write(sentence + "\n")
    out_to_file.close()
