import sqlite3

conn = sqlite3.connect("rasp.db")
cursor = conn.cursor()


def TableExist():
    tableCheck = "parsData"
    showTable = cursor.execute('select * from sqlite_master where type = "table"')
    temp = []
    for showTable in cursor:
        temp.append(showTable)
    try:
        if tableCheck not in temp:
            createTable = """CREATE TABLE parsData (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              groupName TEXT OT NULL,
                              day TEXT OT NULL,
                              numLesson INTEGER NOT NULL,
                              dataLesson TEXT OT NULL,
                              NumberClass TEXT OT NULL,
                              );"""
            cursor.execute(createTable)
            conn.close()
    except sqlite3.OperationalError:
        print('Таблица уже существует')
        conn.close()


def NonOutExecuteSQL(command):
    cursor.execute(command)


def ValuesExecuteSQL(command, values):
    cursor.execute(command, values)


def OutPExecuteSQL(command):
    cursor.execute(command)
    resultExecute = cursor.fetchall()

    return print(resultExecute)


def ReturnExecuteSQL(command):
    cursor.execute(command)
    ResultExecute = cursor.fetchall()
    return ResultExecute


def OutputSQL(command, values):
    cursor.execute(command, [values])
    ResultExecute = cursor.fetchall()
    return ResultExecute


def Commit():
    conn.commit()
