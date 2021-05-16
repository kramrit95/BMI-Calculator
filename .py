#your code goes here
weight=int(input())
height=float(input())
result=(weight/(height**2))
if result<18.5:
   print("Underweight")
if result>=18.5 and  result<25:
   print("Normal")
if result>=25 and result<30:
   print("Overweight")
if result>=30:
   print("Obesity")

   


