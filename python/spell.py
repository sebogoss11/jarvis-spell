# -*- coding: utf-8 -*-
import os


def spell() :
    path = os.getcwd() + "/plugins_installed/jarvis-spell/python/spell.txt"
    file = open(path)
    line = file.readline()

    file.close()
    lineSplit = line.split()

    
    lineCopy = "" 
    copy = False
    i = 0
    while i < len(lineSplit) :
        if copy == True :
            lineCopy += lineSplit[i] + " "
        else :
            if lineSplit[i] == "écrit-on" and lineSplit[i-1] == "comment" :
                copy = True
        i += 1

    reply = "On écrit " + lineCopy + "comme ceci.\n"
    i = 0
    while i < len(lineCopy) :
        if str(ord(lineCopy[i])) == "195" and str(ord(lineCopy[i+1])) == "169" :
            reply += "é\n"
            i += 1
        elif str(ord(lineCopy[i])) == "195" and str(ord(lineCopy[i+1])) == "170" :
            reply += "ê\n"
            i += 1
        elif str(ord(lineCopy[i])) == "195" and str(ord(lineCopy[i+1])) == "160" :
            reply += "à accent grave\n"
            i += 1
        elif str(ord(lineCopy[i])) == "195" and str(ord(lineCopy[i+1])) == "168" :
            reply += "è\n"
            i += 1
        elif str(ord(lineCopy[i])) == "195" and str(ord(lineCopy[i+1])) == "185" :
            reply += "ù\n"
            i += 1
        elif lineCopy[i] == "y" :
            reply += "y grec\n"
        elif lineCopy[i] == "e" :
            reply += "eux\n"
        elif lineCopy[i] == "'" :
            reply += "apostrophe\n"
        elif lineCopy[i] == " " :
            reply += "espace\n"
        else :
            reply += lineCopy[i] + "\n"
        i += 1

    reply = reply[0:len(reply)-7]
    reply += "\n"
    
    file = open(path, 'w')
    file.write(reply)
    file.close()

spell()
