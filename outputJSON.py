import connector
import json
import os
from operator import itemgetter

if not os.path.exists('outFile'):
    os.mkdir('outFile')

pathName = 'outFile/'


def OutBASE():
    com = """SELECT * FROM parsData WHERE dataLesson LIKE ? 
    ORDER BY CASE 
    WHEN day LIKE 'понедельник'  THEN 1  
    WHEN day LIKE 'вторник'  THEN 2
    WHEN day LIKE 'среда'  THEN 3 
    WHEN day LIKE 'четверг'  THEN 4 
    WHEN day LIKE 'пятница'  THEN 5 
    WHEN day LIKE 'суббота'  THEN 6 
    ELSE 7
    END, 
    numLesson ASC;"""
    inp = input("Введите фамилию: ")
    val = '%' + inp + '%'
    DataTech = connector.OutputSQL(com, val)
    return DataTech, inp


def toJSON():
    temp = OutBASE()
    data = temp[0]
    teacher = temp[1]
    lesson = []
    for row in data:
        lesson.append({'GroupName': row[1], 'Day': row[2], 'NumberLesson': row[3], 'DataLesson': row[4], 'NumberClass': row[5]})

    name_file = pathName + teacher + '.json'
    json_data = {'Teacher': teacher, 'lesson': lesson}
    with open(name_file, 'w') as f:
        json.dump(json_data, f, ensure_ascii=False)

