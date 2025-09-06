#FutureTime.py
#Name: Emily Billings
#Date: 9-6-25
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute,) 
  #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  add_hours = int(input("Enter number of hours to add: ")) 
  #Ask user for minutes
  add_mintues = int(input("Enter number of mintues to add: "))

  #Calculate the time after the user-supplied time has passed.
  total_mintues = currentMinute + add_mintues 
  extra_hours = total_mintues // 60
  final_mintues = total_mintues % 60

  total_hours = currentHour + add_hours + extra_hours
  final_hours = total_hours % 24 
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"Future time: {final_hours:02}:{final_mintues:02}")

if __name__ == '__main__':
 main()

