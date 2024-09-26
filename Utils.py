def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data