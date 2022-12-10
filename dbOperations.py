import sqlite3
import logging as log
import sys
import traceback


def sqliteConn():
        sqlite3Con = sqlite3.connect('ifw-db.db')
        return sqlite3Con


def sqliteInitialize(sqlite3Con: sqlite3):
        log.info("Check tables")
        executor = sqlite3Con.cursor()
        # Create monitor Table
        executor.execute(
            "CREATE TABLE IF NOT EXISTS previous (ID INTEGER PRIMARY KEY DEFAULT auto_increment,filename varchar)")
        executor.execute(
            "CREATE TABLE IF NOT EXISTS current (ID INTEGER PRIMARY KEY DEFAULT auto_increment,filename varchar)")


def insertRow(sqlite3Con: sqlite3, filename):
        executor = sqlite3Con.cursor()
        print('filename'+filename)
        executor.execute("insert into current (filename) values (?)", [filename])
        sqlite3Con.commit()

def store_current(sqlite3Con: sqlite3):
        executor = sqlite3Con.cursor()
        executor.execute("delete from previous")
        sqlite3Con.commit()
        executor.execute("insert into previous select * from current")
        sqlite3Con.commit()
        executor.execute("delete from current")
        sqlite3Con.commit()

def checkIfRunning(sqlite3Con: sqlite3):
        executor = sqlite3Con.cursor()
        executor.execute("select * from previous EXCEPT select * from current")
        results = executor.fetchall()
        i = 0
        for r in results:
                i = i+1
        return i

