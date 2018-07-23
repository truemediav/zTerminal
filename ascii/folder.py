def request(txt, output_arr=False, v='', n='', output=''):
	v=open('ascii/'+ txt +'.txt', 'r', encoding="utf8").read().split('\n')
	if output_arr == False:
		for x in range(len(v)):
			output += n + v[x]
			n='\n'
		return output
	else:
		output=[]
		for x in range(len(v)):
			output.append(n + v[x])
			n='\n'
		return output