import codecs
suffixes_list = []
suffixes_list.append(u'\u0947' + u'\u0902')
suffixes_list.append(u'\u0947')
suffixes_list.append(u'\u094B' + u'\u0902')
suffixes_list.append(u'\u094B')
suffixes_list.append(u'\u093E' + u'\u0901')
suffixes_list.append(u'\u090F' + u'\u0901')
suffixes_list.append(u'\u0901')
suffixes_list.append(u'\u093E' + u'\u0902')
outfile = open("output.txt","w")
with codecs.open('hindi.txt', encoding='utf-8') as f:
	for line in f:
		for word in line.split():
			flag = 0;
			for suffix in suffixes_list :
			    if word.endswith(suffix) :
			        outfile.write(word+" Plural\n")
			        flag = 1
			        break;
			if flag==0 :
			    outfile.write(word+" Singular\n")
outfile.close()
