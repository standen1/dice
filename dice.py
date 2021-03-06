#!/usr/bin/env python
#coding=utf-8

#This application simulates dice.  A user enters a number of dice
#they would like to roll and then generates a random number for 
#each die.  It then prints a virtual die for each number to the
#console.
#Note: This is from a tutorial.  I have followed these instructions
#   however, I have implemented my own logic.  Such as a constant
#   loop until the user quits the program.  I also used a main()
#   function for running the code.
#Link to tutorial: 
#   https://realpython.com/python-dice-roll/

#imports
from dice_class import Dice


#Function: main
#   Arguments: N/A
#   Variables: number_dice_prompt, dice_roll, dice_face_diagram
#   Return: N/A
#   Calls: prompt_user, roll_dice, generate_dice_faces
#   Called By: N/A
def main():
    #prompt user
    print("Welcome!!!")
    number_dice_prompt = prompt_user()

    #if user enters q, prompt_user returns 0, which will end the loop
    #and quit the program.
    while number_dice_prompt != 0:
        dice_roll = Dice(number_dice_prompt)
        dice_face_diagram = dice_roll.generate_dice_faces()
        print(f"\n{dice_face_diagram}")
        number_dice_prompt = prompt_user()
    print("Thanks for playing.  See you next time!!!")
    exit()


#Function: prompt_user
#   Arguments: N/A
#   Variables: VALIDATION, QUIT_VALIDATION, num_dice_input, format_num_dice_input
#   Return: returns an integer value between 1 and 6
#   Calls: prompt_user() - recursive if variable is invalid.
#   Called By: main
def prompt_user():
    VALIDATION = ["1", "2", "3", "4", "5", "6"] #for validating input
    QUIT_VALIDATION = ["q", "Q"]

    #prompt user
    num_dice_input = input("How many dice would you like to roll?\nPlease pick a number between 1 and 6 only.\nTo quit the program, press Q.\n")

    format_num_dice_input = num_dice_input.strip() #strip any space and \n characters.

    #validate input, if not valid, rerun function.
    if format_num_dice_input in VALIDATION:
        return int(format_num_dice_input)
    elif format_num_dice_input in QUIT_VALIDATION:
        return 0
    else:
        print("Your input is invalid.  Please try again.")
        return prompt_user()

#Call main
main()

#Function info template:

#Function: f_ name
#   Arguments: 
#   Variables: 
#   Return: 
#   Calls: 
#   Called By: