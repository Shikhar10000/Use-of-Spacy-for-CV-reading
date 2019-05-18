import csv
import re
import spacy
import sys
import pandas as pd
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import numpy as np
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def extract_name(string):
    r1 = string
    nlp = spacy.load('my_model')
    doc = nlp(r1)
    for ent in doc.ents:
        if(ent.label_ == 'Email Address'):
            print(ent.text)
            break

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

resume_string = convert("resume.pdf")
resume_string1 = resume_string

resume_string = resume_string.replace(',',' ')

resume_string = resume_string.lower()

def extract_information(string):
    string.replace (" ", "+")
    query = string
    soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/" + query), "html.parser")
    for item in soup.find_all('div', attrs={'id' : "mw-content-text"}):
        print(item.find('p').get_text())
        print('\n ')
with open('techatt.csv', 'r+') as f:
    reader = csv.reader(f)
    your_listatt = list(reader)
with open('techskill.csv', 'r+') as f:
    reader = csv.reader(f)
    your_list = list(reader)
with open('nontechnicalskills.csv', 'r+') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)

s = set(your_list[0])
s1 = your_list
s2 = your_listatt
skillindex = []
skills = []
skillsatt = []
print('\n')
extract_name(resume_string1)
print('\n')
print('Phone Number is')
y = extract_phone_numbers(resume_string)
y1 = []
for i in range(len(y)):
    if(len(y[i])>9):
        y1.append(y[i])
print(y1)
print('\n')
print('Email id is')
print(extract_email_addresses(resume_string))
for word in resume_string.split(" "):
    if word in s:
        skills.append(word)
skills1 = list(set(skills))
print('\n')
print("Following are his/her Technical Skills")
print('\n')
np_a1 = np.array(your_list)
for i in range(len(skills1)):
    item_index = np.where(np_a1==skills1[i])
    skillindex.append(item_index[1][0])

nlen = len(skillindex)
for i in range(nlen):
    print(skills1[i])
    print(s2[0][skillindex[i]])
    print('\n')

s1 = set(your_list1[0])
nontechskills = []
for word in resume_string.split(" "):
    if word in s1:
        nontechskills.append(word)
nontechskills = set(nontechskills)
print('\n')

print("Following are his/her Non Technical Skills")
list5 = list(nontechskills)
print('\n')
for i in range(len(list5)):
    print(list5[i])
print('\n \n')
