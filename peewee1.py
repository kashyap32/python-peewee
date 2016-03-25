from peewee import *
from collections import OrderedDict
import datetime
import sys,os
db=SqliteDatabase('peewee.db')
class  Entry(Model):
    content=TextField()
    time=DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database=db
def init():
    db.connect()
    db.create_tables([Entry],safe=True)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def loop():
    choice=None
    while choice!='q':
        clear()
        print "enter 'q' to quit"
        for key,value in menu.items():
            print('{} {}'.format(key,value.__doc__))
        choice=raw_input('Action:').lower().strip()
        if choice in menu:
            clear()
            menu[choice]()
    #hello
def entry():
     """Enter the number"""
     print "enter your entry Press ctrl+d when finished"
     data=sys.stdin.read().strip()
     if data:
         if raw_input('Save entry?[yn]').lower()!='n':
             Entry.create(content=data)
             print "success"
             
def view(search=None):
     """Enter the number"""

     entries=Entry.select()
     if search:
         entries=entries.where(Entry.content.contains(search))

     for lists in entries:
         clear()
      
         print lists.content
         print 'n:Nexr'
         print 'q to main menu'
         print 'd to delete'
         next_action=raw_input('Action:[Nq]').lower().strip()
         if next_action=='q':
             break
         if next_action=='d':
             delete(lists)
def search():
     """search"""
     view(raw_input('search entry'))
     
def delete(lists):
    if raw_input('sure?[y/n]').lower()=='y':
        lists.delete_instance()
        print 'deleted'
        
         
menu=OrderedDict([('a',entry),('v',view),('s',search)])

if __name__=='__main__':
    init()
    loop()
    view()
    search()
