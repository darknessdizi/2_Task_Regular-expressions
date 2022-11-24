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

    new_list = []
    for index, element in enumerate(my_list):
        line = ','.join(element[:3])
        full_name = re.findall(r'\w+', line)
        while True:
            if len(full_name) < 3:
                full_name.append('')
            else:
                break
        full_name.extend(element[3:5])
        patern = r'(\+7|8)\s*\(*(\d+)\)*[\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})'
        if re.search(patern, element[5]):
            phone = re.sub(patern, r'+7(\2)\3-\4-\5', element[5])
            patern = r'\(*(\w+)\.\s*(\d+)\)*'
            phone = re.sub(patern, r'\1.\2', phone)
            full_name.append(phone)
        else:
            full_name.append(element[5])
        full_name.append(element[6])
        new_list.append(full_name)
        print(full_name)

    save_file(new_list)