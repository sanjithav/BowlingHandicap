# Description of Program: Takes user inputs of name and 3 game scores, calculates average and handicap, outputs handicap report for name given

from math import floor #imports function needed to round numbers

#takes user input
name=input("Enter bowler's name: ")
game1=int(input("Enter Game 1: "))
game2=int(input("Enter Game 2: "))
game3=int(input("Enter Game 3: "))

#calculates avg and handicap
average=floor((game1+game2+game3)/3)
handicap=floor((200-average)*0.8)
handicap=max(0,handicap)

#prints output
print()
print("Handicap report for ",name,":",sep="")
print("  ",name,"'s average is: ",average,sep="")
print("  ",name,"'s handicap is: ",handicap,sep="")
print()
print("It's time to Bowl!")
print()
