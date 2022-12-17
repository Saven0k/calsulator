import input_number
import Log

def calc():
    fv = input_number.first_val
    sv = input_number.second_val
    op = input_number.operation
    if op == '+':
        Log.wr2(f"Calc work  = +")
        return (fv + sv)
    elif op == '-':
        Log.wr2(f"Calc work = -")
        return (fv - sv)
    elif op == '*':
        Log.wr2(f"Calc work = *")
        return (fv * sv)
    elif op == '/':
        Log.wr2(f"Calc work = /")
        return (fv / sv)
    elif op == '**':
        Log.wr2(f"Calc work = **")
        return (fv ** sv)