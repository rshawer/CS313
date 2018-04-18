#  File: BabyNames.py 

#  Description: A database of all baby names that allow users to query baby name popularity

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 3/21/18

#  Date Last Modified: 3/23/18
import urllib.request
#create global dictionary
global baby_dict
baby_dict={}
#read the file
def read_file(url):
   try: 
       in_file=urllib.request.urlopen(url)
       read_file=in_file
   except:
       print("Use a valid URL")
       exit()
   finally:
       for line in read_file:
           line = str (line, encoding = 'utf8')
           line=line.strip()
           line=line.split()
           ranks=[]
           name=""
           for i in line:
               if i.isalpha():
                   name=i
               else:
                   ranks.append(int(i))
           baby_dict[name]= ranks
#determines if a name exist in the dictionary
def name_search(name):
   if name in baby_dict:
      return True
   else:
      return False
#convert index to decade years
def decade(index):
   for i in range (0,11):
      if index==i:
         return (1900+i*10)
# search names and prints the greatest ranking decade
def choice_one(name):
   if name_search(name):
      print("The matches with their highest ranking decade are: ")
      temp=baby_dict[name]
      minumum=min(temp)
      while (minumum in temp):
         print(name, decade(temp.index(minumum)))
         temp[temp.index(minumum)]=-9999
   else:
      print(name, "does not appear in any decade.")
# prints all the data for one name
def choice_two(name):
   if name_search(name)==False:
      print(name, "does not appear in any decade.")
      return None
   decade=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
   ranks=""
   for i in baby_dict[name]:
      ranks+=str(i)+" "
   print(name+": "+ranks)
   for i, dec in enumerate(decade):
      print(str(dec)+": "+str(baby_dict[name][i]))
# prints all names that appear in only one decade 
def choice_three(decade):
   given_dec={}
   if decade !=2000:
      decade=(decade//10)%10
   if decade==2000:
      decade=10
   for key in baby_dict:
      given_dec[key]=baby_dict[key][decade]
   print("The names are in order of rank:")
   for i in range (1,1001):
      for key in given_dec:
         if i==given_dec[key]:
            print(key+": "+str(i))
# prints the names that are in all decades         
def choice_four():
   masterlist=[]
   for key in baby_dict:
      if 0 not in baby_dict[key]:
         masterlist.append(key)
   print(str(len(masterlist))+" names appear in every decade. The names are:")
   masterlist.sort()
   for name in masterlist:
      print(name)
#prints the names that get more popular
def choice_five():
   morepop=[]
   for key in baby_dict:
      if baby_dict[key]==sorted(baby_dict[key],reverse=True) and (0 not in baby_dict[key]):
         morepop.append(key)
   print(str(len(morepop))+" names are more popular in every decade.")
   for name in morepop:
      print(name)
#prints the names that get less popular 
def choice_six():
   morepop=[]
   for key in baby_dict:
      if baby_dict[key]==sorted(baby_dict[key]) and (0 not in baby_dict[key]):
         morepop.append(key)
   print(str(len(morepop))+" names are less popular in every decade.")
   for name in morepop:
      print(name)
def main():
    read_file("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
    print("Options:")
    print("Enter 1 to search for names.")
    print("Enter 2 to display data for one name.")
    print("Enter 3 to display all names that appear in only one decade.")
    print("Enter 4 to display all names that appear in all decades.")
    print("Enter 5 to display all names that are more popular in every decade.")
    print("Enter 6 to display all names that are less popular in every decade.")
    print("Enter 7 to quit.")
    print()
    choice=int(input("Enter choice: "))
    #implements all the options, till you quit
    while choice!=7:
       if choice ==1:
          name=str(input("Enter name: "))
          print()
          choice_one(name)
       elif choice == 2:
          name=str(input("Enter name: "))
          print()
          choice_two(name)
       elif choice ==3:
          decade=int(input("Enter decade: "))
          choice_three(decade)
       elif choice ==4:
          choice_four()
       elif choice ==5:
          choice_five()
       elif choice ==6:
          choice_six()
       elif choice>=7:
          break
       print()
       print("Options:")
       print("Enter 1 to search for names.")
       print("Enter 2 to display data for one name.")
       print("Enter 3 to display all names that appear in only one decade.")
       print("Enter 4 to display all names that appear in all decades.")
       print("Enter 5 to display all names that are more popular in every decade.")
       print("Enter 6 to display all names that are less popular in every decade.")
       print("Enter 7 to quit.")
       print()
       choice= int(input("Enter choice: "))
    #quits the program
    if choice>=7:
       print()
       print()
       print("Goodbye.")
       
  














main()
