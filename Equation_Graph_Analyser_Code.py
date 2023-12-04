import os
def installer() :
      try :
          import time
          import matplotlib
          import math
          import random
          import mysql.connector 

      except :
          os.system('pip install matplotlib')
          os.system('pip install python-time')
          os.system('pip install mysql-connector-python')


def analyser(x,y) :
      print()
      print()
      print()
      m=[]
      print('GRAPH  ANALYSIS AND PROPERTIES     ----->        ')
      print()
      print("     X-CORDNIATE              Y-CORDINATE            CORDINATE POINT                   INSTANTANEOUS SLOPE  ")
      for i in range(len(x)) :
         if i!=len(x)-1 :
               m=(y[i+1]-y[i])/(x[i+1]-x[i])
               print("        "+str(x[i])+"                                "+str(y[i])+"                                    "+'('+str(x[i])+','+str(y[i])+')'+'                                         '+str(m))
         elif i==len(x)-1 :
              break
def distributor() :
      import interface
      print(interface.creator())
      print(' List Of Operations :\n'.upper()+'                                     1) Equation-Graph Analyser\n'+'                                     2)Graph-Equation Analyser\n'+'                                     3)To Exit\n')
      c=input('Choice -->  ')
      import time
      if c=='1' :
            print('Redirecting To Equation-Graph Analysing Portal !!')
            time.sleep(5)
            EqGr()
            distributor()
      elif c=='2' :
            print('Sorry This Feature Is Still Under Work And Might Be Ready To Use In Later Updates !!!!!')
            time.sleep(5)
            distributor()
      elif c=='3' :
            import interface
            interface.end()
      else :
            print('Seems Like Something Went Wrong. Try Again in 5 seconds !!!!!')
            time.sleep(5)
            distributor()

def power(s) :
      x=''
      j=0
      l=[]
      p=[]
      k=0
      for i in range(len(s)) :
                     if s[i]=='^' :
                         l.append(i)
                     elif s[i] in('+','-') :
                         p.append(i)
      while k!=len(l) :
           x=x+s[j:l[k]-1]+'math.pow('+s[l[k]-1]+','+s[l[k]+1:p[k]]+')'
           j=p[k]
           k+=1
      x=x+s[j : ]
      return x


def EqGr() :
      eq=''
      import interface
      print(interface.EqGrp())
      s=input('Enter Space Seperated Terms Y and X in The Equation refer to [ y  x ]-->  ').split()
      eq=input("Enter The Mathematical Equation In Terms Of X and Y Only --> ")
      if '^' in eq :
            eq=power(eq)      
      m=eq[2: ]
      import matplotlib as p
      d=input('Enter Domain Set (sample input format --> 10 30)  : ').split(' ')
      ip=int(d[0])
      fp=int(d[-1])
      x=[]
      y=[]
      l=['import math','ip,fp=0,0','def pf(ip,fp) : ',' y,z=[],[]',' for x in range(ip,fp+1) : ','  d='+m,'  y.append(d)','  z.append(x)',' return y,z']
      a=open('pspr.py','w')
      for i in l :
            a.write(i+'\n')
      a.close()
      import pspr
      t=pspr.pf(ip,fp)
      from matplotlib import pyplot as p
      b=open('pspr.py','w').close()
      p.plot(t[-1],t[0],color='y',label=eq)
      p.xlabel((s[-1]+'  ['+s[-1][0]+']').upper(),fontsize=20,style='italic')
      p.ylabel((s[0]+'  ['+s[0][0]+']').upper(),fontsize=20,style='italic')
      p.title('GRAPH OF '+s[0].upper()+' VS '+ s[-1].upper(),fontsize=20,style='italic')
      p.legend()
      p.show()
      analyser(t[-1],t[0])
installer()
distributor()


