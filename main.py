def create_note_log (file):
    with open(file, 'w', encoding ='utf-8') as f:
        note_log = []
        json.dump(note_log, f, indent=2, ensure_ascii=False)   
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
