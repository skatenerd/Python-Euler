#!/bin/bash
#Start a new project euler problem!
#The first argument is the problem description, usually a number


PROBLEMPREFIX="problem"
DOTPY=".py"

if [ -z "$1" ]
then
        cowsay -d "arg not defined."

        exit 1
else
        problemNum=$1
        folderName=$PROBLEMPREFIX$problemNum
        fileName=$folderName$DOTPY
        mkdir $folderName
        cd $folderName
        touch $fileName
        idle-python2.6 $fileName &
        exit 0
fi



