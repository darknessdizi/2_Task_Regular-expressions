from pprint import pprint
import csv
import re


def load_file():
    with open("phonebook_raw.csv", encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def save_file(new_list):
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        datawriter = csv.writer(file, delimiter=',')
        datawriter.writerows(new_list)


if __name__ == '__main__':

    my_list = load_file()
    # pprint(my_list)

    new_list = []
    for index, element in enumerate(my_list):
        if index != 0: 
            client_list = []
            for i in element:
                client_list += re.findall(r'\w+', i)
                print(client_list) 
        else:
            new_list.append(element)

    save_file(new_list)