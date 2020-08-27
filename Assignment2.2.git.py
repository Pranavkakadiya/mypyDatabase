

import sqlite3
import subprocess as sp
import time
from pygame import mixer
mixer.init()
mixer.music.load('MeekMillGoingBadfeatDrakeOfficialVideo-arabsongtop.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")



#import datetime

print(os.name)
print(os.getcwd)


def create_table():
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()
    print(cursor)

    query = '''
	    CREATE TABLE IF NOT EXISTS student(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        phone TEXT,
	        time TEXT,
	        photo BLOB NOT NULL
	    )
	'''
    query1 = '''
    	    CREATE TABLE IF NOT EXISTS student1(
    	    	id INTEGER PRIMARY KEY, 
    	    	roll INTEGER, 
    	    	name TEXT,
    	        phone TEXT
    	    )
    	'''

    cursor.execute(query)
    cursor.execute(query1)

    conn.commit()

    conn.close()


def add_student(roll, name, phone, time, photo):
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	    INSERT INTO student( roll, name, phone,time,photo)
	    	        VALUES ( ?,?,?,?,?)
	'''
    # "insert into student values('{},{},{}')".format('RKU','SOE',5000))
    # "insert into student values(?,?,?)",('rku','sos',6000)
    # "insert into student values(:name,:lname,:pay)",{'name':'RKU','lname':'kakadiya','pay':5000}
    cursor.execute(query, (roll, name, phone, time, photo))

    conn.commit()
    conn.close()


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def get_students():
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	    SELECT roll, name, phone,time,photo
	    FROM student
	'''

    cursor.execute(query)
    all_rows = cursor.fetchall()

    for row in all_rows:
        roll = row[0]
        name=row[1]
        phone = row[2]
        time = row[3]
        photo=row[4]
        print("roll = ",roll, "Name = ",name)
        print("phone= ",phone,"time= ",time)
        print("Storing employee image and resume on disk \n")
        photoPath = "D:\\" + name + ".jpg"
        writeTofile(photo, photoPath)


    conn.commit()
    conn.close()

    return 0


def get_list_of_table():
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	 SELECT name FROM sqlite_master WHERE type='table'
	'''

    cursor.execute(query)
    all_names = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_names


def get_student_by_roll(roll):
    conn = sqlite3.connect('testdb2.db')
    cursor = conn.cursor()

    query = '''
	    SELECT roll, name, phone
	    FROM student
	    WHERE roll = {}
	'''.format(roll)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def update_student(roll, name, phone):
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	    UPDATE student
	    SET name = ?, phone = ?
	    WHERE roll = ?
	'''
    # 'update emp set pay=? where lname=?',(pay,lname)
    cursor.execute(query, (name, phone, roll))

    conn.commit()
    conn.close()


def delete_student(roll):
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	    DELETE
	    FROM student
	    WHERE roll = {}
	'''.format(roll)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def drop_table(name):
    conn = sqlite3.connect('testdb2.db')

    cursor = conn.cursor()

    query = '''
	    DROP TABLE {}
	'''.format(name)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


create_table()

"""
main code
"""


def add_data(id_, name, phone, time, photo):
    add_student(id_, name, phone, time, photo)


def get_data():
    return get_students()


def get_table():
    return get_list_of_table()


def show_data():
    get_data()
    # for student in students:
    #     print(student)


def show_table():
    table = get_table()
    for all_table in table:
        print(all_table)


def show_data_by_id(id_):
    students = get_student_by_roll(id_)
    if not students:
        print("No data found at roll", id_)
    else:
        print(students)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def select():


    sp.call('cls', shell=True)  #ifu are using window if u are use linux go for clear instead of cls
    sel = input("1. Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Show table\n7.Drop table\n8.Exit\n\n")

    if sel == '1':
        speak.Speak("you are going to add data")
        sp.call('cls', shell=True)

        localtime = time.asctime(time.localtime(time.time()))
        # time_now= str(datetime.datetime.now())
        id_ = int(input('id: '))
        name = input('Name: ')
        phone = input('phone: ')
        photo = input('enter full path with file name and extensuon: ')
        empPhoto = convertToBinaryData(photo)
        add_data(id_, name, phone, localtime, empPhoto)
    elif sel == '2':
        speak.Speak("your data is here")
        sp.call('cls', shell=True)
        show_data()
        input("\n\npress enter to back:")
    elif sel == '3':
        speak.Speak("you are going to search data for this enter id")
        sp.call('cls', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        input("\n\npress enter to back:")
    elif sel == '4':
        speak.Speak("you are going to update data for this enter id which u want to update")
        sp.call('cls', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        print()
        name = input('Name: ')
        phone = input('phone: ')
        update_student(id__, name, phone)
        input("\n\nYour data has been updated \npress enter to back:")
    elif sel == '5':
        speak.Speak("you are going to delete data for this enter id which u want to delete")
        sp.call('cls', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        delete_student(id__)
        input("\n\nYour data has been deleted \npress enter to back:")
    elif sel == '6':
        speak.Speak("your all tables are below")
        sp.call('cls', shell=True)
        show_table()
        input("\n\npress enter to back:")
    elif sel == '7':
        speak.Speak("your are going to delete table for this enter table name which u want to delete")
        sp.call('cls', shell=True)
        tname = input('Enter name: ')
        show_table()
        drop_table(tname)
        input("\n\nYour table has been deleted \npress enter to back:")
    else:
        speak.Speak("Have a goood day")
        mixer.music.stop()
        return 0
    return 1


while (select()):
    pass
