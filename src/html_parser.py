#-*- encoding: gb2312 -*-
'''
Created on 2011-3-18

@author: leishouguo

handle_startendtag ����ʼ��ǩ�ͽ�����ǩ
handle_starttag     ����ʼ��ǩ������<xx>
handle_endtag       ���������ǩ������</xx>
handle_charref      ���������ַ�����������&#��ͷ�ģ�һ���������ʾ���ַ�
handle_entityref    ����һЩ�����ַ�����&��ͷ�ģ����� &nbsp;
handle_data         �������ݣ�����<xx>data</xx>�м����Щ����
handle_comment      ����ע��
handle_decl         ����<!��ͷ�ģ�����<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
handle_pi           ��������<?instruction>�Ķ���
        �������Դ���ҳ�л�ȡ��urlΪ��������һ�¡�Ҫ���ȡ��url���϶���Ҫ����<a>��ǩ��Ȼ��ȡ������href���Ե�ֵ�������Ǵ��룺
'''

import HTMLParser

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)       
       
    def handle_starttag(self, tag, attrs):
        # �������¶����˴���ʼ��ǩ�ĺ���
        if tag == 'a':
            # �жϱ�ǩ<a>������
            for name,value in attrs:
                if name == 'href':
                    print value
       

if __name__ == '__main__':
    a = '<html><head><title>test</title><body><a href="http://www.163.com">���ӵ�163</a></body></html>'
   
    my = MyParser()
    # ����Ҫ���������ݣ���html�ġ�
    my.feed(a)
