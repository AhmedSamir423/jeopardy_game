def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()     
    questions = []
    choices = []
    answer = []

    for i in range(0, len(data), 5):
        questions.append(data[i].strip())
        choices.append([data[i+1].strip(),data[i+2].strip(),data[i+3].strip()])
        answer.append(data[i+4].strip())
    return questions, choices, answer