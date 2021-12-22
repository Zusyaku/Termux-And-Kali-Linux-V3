#-------------------------------------------------------------------------------
# Name:        Flashcard Quizzer
# Purpose:     Learning
#
# Author:      George | Alias Kansas
#
# Created:     20/12/2013
# Copyright:   N/A
# Licence:     MIT License | http://choosealicense.com/licenses/mit/
#
# Ext:         Flash card file should be formatted like this:
#              test1 question|test1 answer
#              test2 question|test2 answer
#              test3 question|test3 answer
#              (and so on..)
#-------------------------------------------------------------------------------
import os
from random import randrange

if __name__ == '__main__':
    print "Welcome to Flash Card Quizzer 1.0.0 - Developed by George | Kansas"
    print "------------------------------------------------------------------"

    while True:
        fp = str(raw_input('File path to flash cards: '))
        print "File: %s" % fp

        try:
            if fp == '' or fp == ' ':
                raise Exception("No input recieved.")
            fileName, fileExtension = os.path.splitext(fp)
            if fileExtension != '.txt':
                raise Exception("Invalid file type.")
            else:
                with open(fp) as f:
                    rawFC = [ line.strip().split('|') for line in f ]
                if len(rawFC) == 0:
                    raise Exception("File is empty.")
                elif len(rawFC[0]) != 2:
                    raise Exception("Invalid file format, make sure it is formatted as follows:\nQuestion1|Answer1\nQuestion2|Answer2")
                else:
                    break
        except Exception, e:
            print "Import Failure: %s" % e

    print "Import Success: %s question and answer pairs loaded." % "{:,}".format(len(rawFC))

    while True:
        try:
            mode = raw_input('What mode would you like to use, easy or hard? (easy/hard): ')
            if mode == 'easy' or mode == 'hard':
                break
            else:
                raise Exception("Invalid answer, make sure to either use easy for easy mode, or hard for hard mode.")
        except Exception, e:
            print "Mode Error: %s" % e

    print "Using mode: %s" % mode.title()

    while True:
        i = 0
        errors = 0
        while i < len(rawFC):
            while True:
                if mode == 'hard':
                    answer = raw_input(rawFC[i][0]+": ")
                else:
                    answer = raw_input(rawFC[i][0]+" (type skip to skip question): ")
                if answer == 'skip':
                    print "You have chose to skip question #%s, this will be recorded as an error." % i
                    i+=1
                    errors+=1
                    break
                elif answer == rawFC[i][1]:
                    print "Good job! You got the answer to question #%s completely right, word for word!" % i
                    i+=1
                    break
                elif answer in rawFC[i][1] and mode == 'easy':
                    print "Good job! You got the answer to question #%s somewhat right, since you're in easy mode we'll give you the rest of it: %s" % (i, rawFC[i][1])
                    i+=1
                    break
                elif answer not in rawFC[i][1] and mode == 'hard':
                    print "You've answered question #%s wrong, since you're in hard mode, we're moving on to the next question. The answer was: %s" % (i, rawFC[i][1])
                    i+=1
                    errors+=1
                    break
                elif mode == 'hard':
                    print "You've answered question #%s wrong, since you're in hard mode, we're moving on to the next question. The answer was: %s" % (i, rawFC[i][1])
                    errors+=1
                    i+=1
                    break
                else:
                    print "Wrong answer, error recorded."
                    errors+=1

        if mode == 'easy':
            print "You've answered all of your questions in easy mode, with %s errors." % errors
        else:
            pointPer = 100 / int(len(rawFC))
            right = int(len(rawFC)) - errors
            print "You've answered all of your questions in hard mode, with % errors (%s\% percentage)." % errors, int(float(pointsPer*right))
        break