def p(s):
	longest = 1
	count = 1
	length = len(s)
	for i in range(length):
		if s[i] == '<' :
			count = count+1
			if count > longest :
				longest = count
		elif s[i] == '>' :
			count = 1
		elif s[i] == '=':
			pass
	print(longest)
	
t = int(input())
test= []
for i in range(t):
	demo_test = input()
	test.append(demo_test)
	demo_test = ""
for i in range(t):
	p(test)

if __name__ == "main":
    main()
