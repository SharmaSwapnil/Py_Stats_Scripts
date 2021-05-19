def count_substring(string, sub_string):
	counter = []
	for i in range(len(string)):
			ss = string.count(sub_string,i,i+len(sub_string))
			counter.append(ss)

	return sum(counter)



if __name__ == '__main__':
    string = input("Enter string ").strip()
    sub_string = input("Enter substring ").strip()    
    count = count_substring(string, sub_string)
    print(count)