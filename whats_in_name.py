def formatting(test_case):
    
    formated = test_case.title().split()
    
    length = len(formated)
    if length == 1 :
        print(formated[0])
    elif length ==2:
        print("{}. {}".format(formated[0][0],formated[1]))
    elif length ==3 :
        print("{}. {}. {}".format(formated[0][0],formated[1][0],formated[2]))
    else :
        print("Not A valid name")





t = int(input("please enter no. of cases"))
test_cases = []
for i in range(t):
    demo_test = input("please enter a case")
    test_cases.append(demo_test)
    demo_test =''
for i in range(t):
    formatting(test_cases[i])
    

if __name__=="main":
main()
