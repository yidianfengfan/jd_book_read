#python enumerate
#����Ϊ�ɱ����ı������� �ַ������б�ȣ�����ֵΪenumerate�ࣺ
#
#line �Ǹ� string ���� 0 �� 1��Ҫ��1���ҳ�����

#����һ
print "start..."
def read_line(line):
    sample = {}
    n = len(line)
    for i in range(n):
        if line[i]!='0':
            sample[i] = int(line[i])
    return sample
 
#������
def xread_line(line):
    return((idx,int(val)) for idx, val in enumerate(line) if val != '0')
 
print read_line('0001110101')
print list(xread_line('0001110101'))
print "finish..."
