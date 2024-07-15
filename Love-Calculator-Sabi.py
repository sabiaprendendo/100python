print("Welcome to the love calculator!")
name1 = str (input("What is your name? "))
name2 = str (input("What is the name of your loved one? "))
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score =int (str(first_digit) + str(second_digit))
if (score > 90):
  print (f"Your score is {score}, you were born to be together! Must be nice, huh?")
elif (score < 10):
  print (f"Your score is {score}... huh....")
elif (score >= 40) and (score <= 50):
  print (f"Your score is {score}, you are cool together. Could be cooler tho. But That's just my opinion, I don't think you should listen to me.")
else:
  print(f"Your score is {score}, you should probably find someone else... that's awkward...")