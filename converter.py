def convert_id(filename):
    """Convert id in the id.txt to Python list."""
    file = open(filename)  # open file with id
    id_list = [int(word.rstrip("\n")) for word in file]
    return id_list