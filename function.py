
def countwordsfromfile ():
    filename=input("type the name of the file - ")

    #Opening the file in reading mode
    file=open(filename,"r")
    numberofwords=0
    for line in file:
        #Splitting the lines wherever spaces are present
        words=line.split()
        #len() - counts the number of elements in any list
        numberofwords=numberofwords+len(words)

    print(numberofwords)

countwordsfromfile ()