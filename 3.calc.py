ef solution(test_case):
    n = int(test_case.split()[0])
    
    b = int(test_case.split()[1])
    
    a = 1
    max_a = n
    max_int = 0
    screen_b = 0
    for ai in range(max_a,0,-b):
            bi = (n-ai)//b
            print("{}*{}".format(ai,bi))
            screen_b = ai*bi
            if screen_b > max_int:
                max_int = screen_b
                    
    print(max_int)





#################################################

    
t = int(input("please enter the no. of test_cases"))
test_cases = []
for i in  range(t):
    test_case = input("please enter test_case")
    test_cases.append(test_case)
    test_case = ""
for i in range(t):
solution(test_cases[i])
