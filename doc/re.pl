#replceAll
newstring = 'ee'
subject = 'abbbbadddd'
reobj = re.compile('a')
result,number = reobj.subn(newstring, subject)

regex = "a"
reobj = re.compile(regex)
result = reobj.split(subject)


#re.search(regex, subject): match: have start, end, group
#re.match(regex, subject)
#re.finall(regex, subject) finditer(regex, subject)
#also can use reobj.search(subject) replace to use re.search(regex, subject)

#ʹ���滻�������ܹ�ʵ�ֶ�ƥ��Ĳ�ͬ����ʵ�ֲ�ͬ���滻��ʽ 
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
 
 
re.sub('-{1,2}', dashrepl, 'pro----gram-files')
#���Ϊ 'pro--gram files'