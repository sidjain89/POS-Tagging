import nltk
import numpy as np
import os
import re

# global vars
fileList = [] 
folderPath = "D:\\IDS 566\\Assignment 3\\Text Files\\"
posTagsDocsArray = []
# end vars

# functions

###################################################
# method to calculate jaccard score(bit vectors)  #
# @param docItems1 : list containing POS tags     #
# @param docItems2 : list containing POS tags     #
# @return retStr : jaccard score in text format   #
###################################################
def JaccardScore(docItems1, docItems2):
    retStr = ""
    union = set(docItems1).union(set(docItems2))
    intersect = set(docItems1).intersection(set(docItems2))
    jaccardScore = float(len(intersect)) / float(len(union))
    retStr = str(jaccardScore)
    return retStr
# end def

###################################################
# method to calculate jaccard score(bit vectors)  #
# @param filePath : path of the file              #
# @description :generate pos tags for document    #
#   and fill the posTagsDocsArray                 #
###################################################
def GeneratePosTags(filePath):
    print("Generating pos tags for file: " + str(filePath))
    file = open(filePath, "r")
    text = file.read().decode("utf-8",errors="ignore")
    text = re.sub('[^0-9a-zA-Z]+', " ", text.lower())
    tokens = nltk.word_tokenize(text)
    posTuples = nltk.pos_tag(tokens)
    posTags = []

    for posTuple in posTuples:
        posTags.append(posTuple[1])
    #end for

    global posTagsDocsArray
    posTagsDocsArray.append(posTags)
#end def

###############################################
# Parses the files and fills posTagsDocsArray #
###############################################
def ParseFiles():
    print("Parsing files....")
    for file in os.listdir(folderPath):
        fileList.append(file)
        GeneratePosTags(folderPath + file)
   #end for
#end def
# end functions 

# script starts
ParseFiles()
print("Done with parsing, now generating jaccard scores...")
print("Jaccard index between files - " + fileList[0] + " and " + fileList[1] 
      + " is: " + JaccardScore(posTagsDocsArray[0], posTagsDocsArray[1]))
print("Jaccard index between files - " + fileList[1] + " and " + fileList[2] 
      + " is: " + JaccardScore(posTagsDocsArray[1], posTagsDocsArray[2]))
print("Jaccard index between files - " + fileList[0] + " and " + fileList[2] 
      + " is: " + JaccardScore(posTagsDocsArray[0], posTagsDocsArray[2]))
print("Done!")
# end of script