import Log
import input_number
from cal import calc
import result


input_number.first_val = first_val = complex(input("Enter first number: "))
input_number.operation = operation = input("Enter operation sign: ")
input_number.second_val = second_val = complex(input("Enter second number: "))
Log.wr("start")

def main(first_val , second_val , operation):
    if first_val:
        Log.wr2(f"User enter number first {first_val}")
    else:
        Log.wr2('error')
    if operation:
        Log.wr2(f"User enter operation {operation}")
    else:
        Log.wr2('error')
    if second_val:
        Log.wr2(f"User enter second number {second_val}")
    else:
        Log.wr2('error')
    Log.wr2("all")
    result.res(calc())
    Log.wr2("end")

main(first_val , second_val, operation)










