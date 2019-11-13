file = open('file.txt','r')
final = open('final.txt','w+')

for line in file:
	words = line.split(':')
	if(len(words)>1):
		final.write((words[2]).strip() + '\n')

final.close();
file.close()
