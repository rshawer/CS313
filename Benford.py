#  File: Benford.py

#  Description: a code that looks like population frequencies of cities

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/29/17

#  Date Last Modified: 11/29/17

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  # fill the rest
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    # get the first digit of the element
    pop_string=str(pop_num)
    pop_digit=int(pop_string[0])
    # make entries in the dictionary
    for i in range (1,10):
        if pop_digit==i:
            pop_freq[str(i)]=pop_freq[str(i)]+1
    
  # close the file
  in_file.close()

  # write out the result
  print("Digit	Count	%")
  for key in pop_freq:
      print("%-7d"%(int(key)),"%-7d"%(int(pop_freq[key])),"%0.1f"%((int(pop_freq[key])/sum(pop_freq.values()))*100))
  
  
main()
