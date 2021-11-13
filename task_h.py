from pip._vendor.colorama import Fore, init as colorama_init
# get the file
path=input("enter a full file's path")
file = open(path,"rb" )
#declare variables
numWords=0 ;maxSentenceLength=0;word='';wordsWithoutK='';countwordsWithoutK=True;colorsList=[] ; 
#number of lines in file-סעיף 1
lines=file.readlines()
numberOfLines=len(lines)
#counts number of words in each line-סעיף 2
for line in lines:
    wordsInLine = line.split()
    wordsInLine=str(wordsInLine).replace("-"," ")
    word+=wordsInLine+" "
    numWords += len(wordsInLine.split())

#finds the longest sentence-סעיף 4
sentences=word.split(".")
for sentence in sentences:
    wordsInsentence=sentence.split()
    if len(wordsInsentence)>maxSentenceLength:
       maxSentenceLength=len(wordsInsentence)
#finds the average length of sentence-סעיף 4
avgSentenceLength=numWords/(len(sentences)-1)
#clean the text
word = word.lower()
word=word.replace('.','').replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("b'","").replace('"','').replace("'","").replace("''","").replace(";","").replace("-"," ").replace("_","")
word = word.split()
#find the number of unique words in the file-סעיף 3 
unique = []
for w in word:             
    if w not in unique:
        unique.append(w) 
#find the colors in the text and the number of their appearences-סעיף 8
def countColorsAppearences(words): 
    colorsList=[] ;appearedColors=[] ;i=0;j=0;colorsA=''
    colorama_init(autoreset=True)
    colors = [x for x in dir(Fore) if x[0] != "_"]
    for color in colors:
        color=color.lower()
        colorsList.append(color)
    for word in words:
        if word not in colorsList :
            continue
        else:
            if word not in appearedColors:
                appearedColors.append(word)
                appearedColors.append(1)
            else:
                i=appearedColors.index(word)
                appearedColors[i+1]+=1
    for color in range(len(appearedColors)//2):
        colorsA+="the color "+ appearedColors[j]+" appears "+str(appearedColors[j+1])+" times in the file\n"
        if j<len(appearedColors)-2:
            j+=2
    return colorsA 
#find the longest sequence in the file without the letter "k"-סעיף 6
def longestSequenceWithoutK(words):
    lswk='';countlswk=0;i=0;maxcountlswk=0;maxlswk='';f=True
    if "k" not in words[i]:
        i=0
    elif len(words[i]>1):
        i+=1
    for item in range(len(words)):
        if f==False:
            break
        while("k" not in words[i] ):                
            countlswk+=1
            lswk+=words[i]+" "
            if i<len(words)-1:
                i+=1
            else:
                break            
        if countlswk>maxcountlswk:
            maxcountlswk=countlswk
            maxlswk=lswk
            countlswk=0
            lswk=''
        if i<len(words)-1:
            i+=1       
        item+=i
        if i==len(words)-1:          
            f=False
    return (maxlswk)  
#call functions        
lswk=longestSequenceWithoutK(word)
colorsA=countColorsAppearences(word)
#enter data into variables
lswkM="the longest sequence in the file without the letter 'k' is:"+str(lswk)+" its length is"+str(len(lswk.split()))
numoflines="number of lines in the file: "+str(numberOfLines)+" \n" 
numofWords="number of words in the file: "+str(numWords)+" \n"    
longestSentence="the longest sentence in the file has "+str(maxSentenceLength) +" words\n"    
avgSentence="the average length of a sentence in the file is "+str(avgSentenceLength) +" words\n"    
numOfUniqueWords="the number of unique words in the file is: "+str(len(unique)) +" words\n"    
#write data in the report file
Statistics_report1 = open(r"Statistics_report.txt", "w")
Statistics_report1.write(numoflines)
Statistics_report1.write(numofWords)
Statistics_report1.write(longestSentence)
Statistics_report1.write(avgSentence)
Statistics_report1.write(numOfUniqueWords)
Statistics_report1.write(colorsA)
Statistics_report1.write(lswkM)
