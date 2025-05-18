import os
import string


def read_lyrics(file):
   lyrics = open(file)
   Song=str(lyrics.read().lower().split())
   #Turns the string to lowercase and into a split string
   print(Song)
   lyrics.close()
   #closes file
   return Song
# Changed so that it is automatically changed to a plit string
# I made the variable song different so that i could close the file


def input_lyrics():
    lyrics=str(input()).lower().split()
    return lyrics

def get_lyrics_fl(lyrics,type=list):
    lyrics_fl=list(word[0] for word in lyrics)
    #This is the problem because it doesn't associate "Word" with each individual item in list but instead treats every individual character as a "Word"
    print(word[0] for word in lyrics)
    #Case in point
    return(lyrics_fl)

lyrics=read_lyrics("lyrics.txt")

alphabet = list(string.ascii_lowercase)
FirstLetter = get_lyrics_fl(lyrics)

'''
#Frankenstein Code Attempt to get the length of the text file (Deemed Unnecesary)
with open(r'Lyrics.txt','r') as file:
        length=0
        data = file.read()
        w=data.split()
        length+=len(w)
        print(length)
'''

i = 0
j = 0
a=0
while (a<len(lyrics)):
    #Different attemot to make the lyrics seperat correctly (Didn't work)
    print(lyrics[a])
    a+=1

print(FirstLetter)
while (i<len(FirstLetter)):
    #Supposedly for every first letter there is a corrosponding "Word"
    if FirstLetter[i] is alphabet[j]:
        #Check to match with the apprpriate letter (This Works :))
        print('match')
        j+=1
    print(lyrics[i])
    #Output is printing each letter one by one instead of word by word
    i+=1
