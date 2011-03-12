"""
����������ʹ�û�����yield�﷨,���ѵ������Ľ���ȴ����,������ĸ㶨yield,����ʱ�������������.
 
Ԥ������: ������(iterator)
ʹ�ó���: ������(constructor)
yield�÷�: �ݹ����
 
1. iterator
�������������Ӧ���������±��ˣ��ҿ������c++���룺
int array[10];
for ( int i = 0; i < 10; i++ )
    printf("%d ", array[i]);
������������һ��������(array[10])������һ��˳��(i++)��������ȡ��ֵ(array[i])�����в���(printf("%d ", array[i])��
 
����Ĵ��뷭���python��
array = [i for i in range(10)]
for i in array:
    print i,

���ȣ�array��Ϊһ��list�Ǹ����������list����ڽ�������Ĭ�ϵ�next��Ϊ��python������Щ֮���ȡ�����ܵ�û����λ�����Ķ����ǣ��ó�array��Ѿ�����ĵ�������������nextһ�°�ֵ��i��forѭ�����崦�ã�for�����ֵprint�ˡ�
 
���ڵ����������ݿ������������������������
 
2. constructor
��ô�Ѻ������constructor��  �ں���������yield�����ˣ�
def gen():
    print 'enter'
    yield 1
    print 'next'
    yield 2
    print 'next again'

for i in gen():
    print i
��λ��python����gen���������yield��֪��������next�ˣ���������ô�Դ������������next��
���������õ�iterator��ʱ������ʲôҲ���ǣ�����������ڴ�������������˵�����±�Ϊ-1�ĵط������ں�����˵���Ǻ����������û�ɣ��������¾㱸��Ƿnext��
��ʼfor i in g��next��itreator���е�yield�����ڵĵط�������ֵ,
�ٴ�next����������һ��yield�����ڵĵط�������ֵ,��������ֱ����������(������ͷ)��
��һ��������������������ǣ�
enter
1
next
2
next again
 
3. ʹ��yield
yield�Ĵ���������������ܴ�Ϻ���ִ�л��ܼ��¶ϵ㴦�����ݣ��´�next����ϻأ�
�����ǵݹ麯����Ҫ�ġ�
�������������������
(Ӧ����David Mertzд��)
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.label
        for x in inorder(t.right):
            yield x
for n in inorder(tree)
    print n

"""



#����ȫ����
def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p
 
#�������
def comb(items, n=None):
    if n is None:
        n = len(items)    
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c
 
a = perm('abc')
for b in a:
    print b
    break
print '-'*20
for b in a:
    print b 