strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))
print strHello
#�������the length of (Hello World) is 11

nHex = 0x20
#%x --- hex ʮ������
#%d --- dec ʮ����
#%d --- oct �˽���
print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)

#�������ĸ�ʽ�������ȡ��Ⱥ�
#width = 10,precise = 3,align = left
print "PI = %10.3f" % math.pi
#width = 10,precise = 3,align = rigth
print "PI = %-10.3f" % math.pi
#ǰ������ַ�
print "PI = %06d" % int(math.pi)

#print ���Զ�����ĩ���ϻس�,�������س���ֻ����print���Ľ�β���һ�����š�,�����Ϳ��Ըı�������Ϊ��
print "sssgsg",
sys.stdout.write("������ִ�")