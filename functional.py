#def add_cont(file_name, str):

def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()    

def add_cont(file_name, fio):
    data = open(file_name, 'a')
    data.write(fio + '\n')
    data.close()

def show_all(file_name):
    data = open(file_name, 'r')
    for line in data:
        print(line[:-1])
    data.close()    
    
def search(file_name, stroka):
    vyhod = 0
    data = open(file_name, 'r')
    for line in data:
        if str in line:
            print(line)
            vyhod = 123
            break
    if vyhod != 123:    
        print('Такого контакта нет')    
    data.close()

 
