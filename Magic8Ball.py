#Magic8Ball.py
#Name: Emily Billings
#Date: 9-6-25
#Assignment:
#We will need random for this program, import to use this package.
import random

def main():
 print("Magic 8 Ball")
 

  #Prompt the user for their question.
 question = input("Ask the Magic 8 Ball a question: ")

  #Answer question randomly with one of the options from your earlier list.

 answer = ["maybe", "defintely no", "defintely yes", "my sources say no", "outlook is great"]
 print("Magic 8 Ball says: ", random.choice(answer))
if __name__ == '__main__':
  main()
