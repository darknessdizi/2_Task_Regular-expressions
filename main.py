from pprint import pprint
import csv
import re


def load_file():
    with open("phonebook_raw.csv", encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def save_file(new_list):
    with open("phonebook.csv", "w", encoding='utf-8', newline='') as file:
        datawriter = csv.writer(file, delimiter=',')
        datawriter.writerows(new_list)

def list_union(my_list):
    new_list = []
    for index, element in enumerate(my_list):
        append = True
        if index == 0:
            new_list.append(element)
            continue
        for y, line in enumerate(new_list):
            if element[0] == line[0] and element[1] == line[1]:
                union_line = [line for line in map(set, zip(element, line))]
                for i, my_set in enumerate(union_line):
                    if len(my_set)>1:
                        my_set.discard('')
                    union_line[i] = ''.join(list(my_set))
                new_list.pop(y)
                new_list.insert(y, union_line)
                append = False
        if append:
            new_list.append(element)
    return new_list   

def search_for_templates():
    pass             


if __name__ == '__main__':

    file_list = load_file()

    new_list = []
    for element in file_list:
        line = ','.join(element[:3])
        client_list = re.findall(r'\w+', line)
        while True:
            if len(client_list) < 3:
                client_list.append('')
            else:
                break
        client_list.extend(element[3:5])
        patern = r'(\+7|8)\s*\(*(\d+)\)*[\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})'
        if re.search(patern, element[5]):
            phone = re.sub(patern, r'+7(\2)\3-\4-\5', element[5])
            patern = r'\(*(\w+)\.\s*(\d+)\)*'
            phone = re.sub(patern, r'\1.\2', phone)
            client_list.append(phone)
        else:
            client_list.append(element[5])
        client_list.append(element[6])
        new_list.append(client_list)

    new_list = list_union(new_list)

    save_file(new_list)