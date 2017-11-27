# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import MySQLdb

# Create your views here.

def getform(request):
    return render(request, 'message_form.html')

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('select name from books ORDER by name')
    names = [ row[0] for row in cursor.fetchall()]
    db.close()
