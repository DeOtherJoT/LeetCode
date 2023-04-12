def simplifyPath (path: str):
	token_lst = path.split('/')
	ret_lst = list()

	# print(token_lst)
	for token in token_lst:
		if (token == '..'):
			if (len(ret_lst) == 0):
				continue
			else:
				ret_lst.pop()
		elif (token == '.' or token == ''):
			continue
		else:
			ret_lst.append(token)
	# print(ret_lst)
	print('/' + '/'.join(ret_lst))


simplifyPath('/../')