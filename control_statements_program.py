'''The following example uses the while statement to prompt users for input and echo the command that you entered back. It’ll run as long as you don’t enter the quit command:'''
command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")
#this program based printing nubers from 1 to n
n=int(input())
for i in range(1,n+1,1):
  print(i)
#this program calculates the table of n unmber
n=int(input("Enter the number"))
for i in range(1,11,1):
  print(f"{n}x{i}={n*i}")
#ternary operator calculating vote eligibility
age=int(input())
votes_eligibility="not eligible" if age<=17 else "eligible"
print(vote_eligibility)
