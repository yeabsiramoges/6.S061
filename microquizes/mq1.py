# assume s is already defined
# your code here

def question_1(s):
    if len(s) >= 3:
        print(s[1:len(s)-1])
    elif len(s) == 2:
        print(s[::-1])
    elif len(s) == 1:
        print(s)
    else:
        print(None)

def question_2(s):
    ns = abs(s)
    print(len(str(ns))-1 if len(str(int(s))) != len(str(s)) else len(str(ns)))

question_2(12624.0)