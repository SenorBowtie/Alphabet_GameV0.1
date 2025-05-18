import os
import string


def read_lyrics(file):
   lyrics = open(file)
   Song=str(lyrics.read().lower())
   #Turns the string to lowercase and into a split string
   lyrics.close()
   SongList=Song.split()
   #closes file
   return SongList
# Changed so that it is automatically changed to a split string
# I made the variable song different so that i could close the file


def input_lyrics():
    lyrics=str(input()).lower().split()
    return lyrics


def AlphCheck (Song,StartingLetter):
    #Takes the Song and goes through the game starting at the chosen initial letter (Defined by a value between 0 and 25)
    FirstLetter = list(word[0] for word in Song)
    #The def function was just one line of code so i simplified it to get the first letter of each word in the song
    alphabet = list(string.ascii_lowercase)
    #Creates a list with the letters in the alphabet
    i=0
    j=StartingLetter

    while (i<len(FirstLetter)):
        if j<26:
            if FirstLetter[i] is alphabet[j]:
                #print(Song[i])
                #!!!!!!!!!!!!!!!!!!!Erase Comment hashtag above to see which words get you through !!!!!!!!!!!!!!!!!! <----------------------------------------------------------------------------
                j+=1
        i+=1       

    if j<26:
        Text=alphabet[StartingLetter] + '->' + alphabet[j]
        print(Text)
        total=j-StartingLetter
    if j==26:
        Text=alphabet[StartingLetter] + '->end'
        print(Text)
        total=26-StartingLetter
    return total

song=read_lyrics("lyrics.txt")

i=0
Tally=0
while (i<26):
    #Checks for every letter of the alphabet
    Tally+=AlphCheck(song,i)
    i+=1
Average=Tally/26
print(Average)
