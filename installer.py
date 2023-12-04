a=open('Equation_Graph_Analyser_Code.py','w')
b=open('ptf1.txt','r')
for i in b.read() :
    a.write(i)
a.close()
b.close()
a=open('interface.py','w')
b=open('ptf2.txt','r')
for i in b.read() :
    a.write(i)
a.close()
b.close()
