#!/usr/bin/python
#coding: latin-1
from random import randint as ran
def encrypt(txt):
	file=open('dict.py').readlines()
	ls=[]
	for i in range(len(file)):
	    ls.append(file[i].strip('\n'))
	txt=list(txt)
	inpt=[]
	for i in txt:
		try:
			inpt.append(ls.index(i)+1)
		except Exception as e:
			pass
	txts=[]
	txtz=[]
	for i in range(10):
		txtz.append(ls[ran(0,len(ls)-1)])
	txtv=0
	for i in range(10):
		if i == 0:
			txtv=ls.index(txtz[i])
		else:
			txtv+=ls.index(txtz[i])
	n=txtv
	total=0
	for ii,i in enumerate(inpt):
		if ii == 0:
			total+=i
		else:
			iss=i
			if len(str(i)) == 1:
				iss='0'+str(iss)
			total=int(str(total)+str(iss))
	total*=n
	total*=n
	return [''.join(txtz), total]

def decrypt(txt, ns):
	file=open('/Users/Max/PY/MakepassFiles/dict.py').readlines()
	ls=[]
	for i in range(len(file)):
	    ls.append(file[i].strip('\n'))
	txtv=0
	for i in range(len(txt)):
		if i == 0:
			txtv=ls.index(txt[i])
		else:
			txtv+=ls.index(txt[i])
	n=txtv
	l=str(ns/n/n)
	lz=[]
	for i in range(len(l)):
		if i % 2 == 0:
			try:
				lz.append(ls[int(l[i]+l[i+1])-1])
			except Exception as e:
				pass
	return ''.join(lz)

