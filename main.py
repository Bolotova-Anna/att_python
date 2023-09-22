def create_note_log (file):
    with open(file, 'w', encoding ='utf-8') as f:
        note_log = []
        json.dump(note_log, f, indent=2, ensure_ascii=False)  
def add_note (file):
    id = input("введите идентификатор заметки: ")
    title = input("введите заголовок заметки: ")
    core = input("введите тело заметки: ")
    from datetime import datetime
    date_of_creation = datetime.now().date()
    new_date_of_creation = str(date_of_creation)
    note= {
        'id' : id, 
        'title' : title,
        'core' : core,
        'date_of_creation' : new_date_of_creation
        }
    data = json.load(open(file))
    data.append(note)
    with open(file, "w", encoding='utf8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
def show_all_notes(file):
    with open(file, 'r', encoding='utf-8') as rf:
        data = json.load(open(file))
        for t in data:
            print('id : ' + t['id'])
            print('title: '  + t['title'])
            print('core : '  + t['core'])
            print('date_of_creation: '  + t['date_of_creation'])
            print('')
def search_note_by_date(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(open(file))
        st = input("введите через тире, без пробелов дату(год, месяц, число) для поиска заметки: ")
        array =[]
        for line in data:
            array.append(line["date_of_creation"])
        flag = st in array
        if flag ==True:
            for line in data:
                    if st in line["date_of_creation"]:
                        print('id : ' + line['id'])
                        print('title: '  + line['title'])
                        print('core : '  + line['core'])
                        print('date_of_creation: '  + line['date_of_creation'])
                        print('')
        else:
            print("в этот день заметок не было")


 
work_file = 'notes.json'
import json
print("Для работы с программой введите пожлуйста одну из следующих цифр:\n"
"1 - если хотите создать журнал заметок\n"
"2 - если хотите создать и добавить новую заметку в журнал заметок\n"
"3 - если хотите вывести на экран все созданные заметки\n"
"4 - если хотите найти конкретную заметку в журнале по дате ее создания\n"
"5 - если хотите удалить заметку\n" 
"6 - если хотите внести изменение в заметку")
comand = int(input("цифра: "))
if(comand==1):
    create_note_log(work_file)
if(comand==2):
    add_note(work_file)
if(comand==3):
    show_all_notes(work_file)
if(comand==4):
    search_note_by_date(work_file)



