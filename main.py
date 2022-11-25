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

def list_union(my_list):
    line_list = []
    for index, element in enumerate(my_list[:-1]):
        # print(index, element)
        union_line = False
        for i in my_list[index+1:]:
            if element[0] == i[0] and element[1] == i[1]:
                union_line = [i for i in map(set, zip(element, i))]
                # print(union_line)
                for i, my_set in enumerate(union_line):
                    if len(my_set)>1:
                        my_set.discard('')
                    union_line[i] = ''.join(list(my_set))
                # print('zip', union_line)
        else:
            if union_line:
                line_list.append(union_line)
            else:
                line_list.append(element)
                # print(i[0], 'no')
    pprint(line_list)
                



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

    # pprint(new_list)
    list_union(new_list)

    # save_file(new_list)