
def read_file(file_name, as_file = False):
    file = open(file_name, "r", encoding="utf-8")
    if as_file:
        return file
    text = file.read()
    file.close()
    return text

