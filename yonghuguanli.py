# coding:gb2312


'''
�û�ע����Ϣ����ϵͳ
���ܰ���:
        1.�鿴ȫ����ע���û���Ϣ
        2.�����û���Ϣ
        3.�޸��û���Ϣ
        4.ɾ���û���Ϣ
        5.������û�
        6.���û���Ϣ�����ļ�
ÿ��ע���û�����Ϣ�ö����ʾ����������ʱ���Զ������ļ��б�����û���Ϣ
������������ʾ�����˵���������ѡ��ִ�в�ͬ�Ĳ���
���ֲ˵���������Ϊ���������ú�����ɶ�Ӧ����
'''
'''
����pickleģ���е�dump��load����
dump����������д���ļ���load�������ļ��������
'''
from pickle import dump,load



##����user�࣬ʵ�������uname���Դ洢�û�����pwd���Դ洢��¼����########################################################
class user:
    #���캯��__init__()����ʵ������ʱ��ʼ���û����͵�¼���룬Ĭ��ֵΪNone
    def __init__(self,uname=None,pwd=None):
        self.uname = uname
        self.pwd = pwd

    #update()�����޸��û����͵�¼����
    def update(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

    #__repr__()������������ӡ��ʽ
    def __repr__(self):
        return 'username=%s \tpassword=%s'%(self.uname,self.pwd)
    ##user��������
##����showall()��ʾ��ǰ��ע���û���Ϣ###################################################################################
def showall():
    global userlist
    if len(userlist)==0:                     #����ʹ��ȫ���û��б����
        print('\t��ǰ��ע���û�')
    else:
        print('\t��ǰ��ע���û���Ϣ����: ')
        n = 0
        for x in userlist:
            n+=1
            print('\t%s. '%n,x)
    input('\n\t��Enter������......\n')
    ##����showall()�������

##����check_update()ִ�в��ҡ��޸Ļ�ɾ������############################################################################
def check_update():
    global userlist                               #����ʹ��ȫ���û��б����
    uname = input('\t������Ҫ���ҵ��û���:')
    index = find(uname)
    if index==-1:
        print('\t%s ������! '%uname)
    else:
        #�û�����ע�ᣬִ���޸Ļ�ɾ������
        print('\t%s �Ѿ�ע��!' % uname)
        print('\t ��ѡ�����:')
        print('\t 1.�޸��û�')
        print('\t 2.ɾ���û�')
        op = input('\t ���������ѡ���Ӧ����:')
        if op=='2':
            #ɾ���û�
            del userlist[index]
            print('\n\t �ѳɹ�ɾ���û�!')
        else:
            #�޸��û���Ϣ
            uname = input('\t �������µ��û���:')
            if uname=='':
                print('\t �û���������Ч!')
            else:
                #����Ƿ��Ѵ���ͬ����ע���û�
                if find(uname)>-1:
                    print('\t ��������û����Ѿ�ʹ��!')
                else:
                    pwd = input('\t ���������û���¼����:')
                    if pwd=='':
                        print('\t ��¼����������Ч!')
                    else:
                        userlist[index].update(uname,pwd)
                        print('\n\t �ѳɹ��޸��û�!')
    input('\n\t ��Enter������......\n')
    ##����check_update()�������

##����adduser()������û�###############################################################################################
def adduser():
    global userlist                                             #����ʹ��ȫ���û��б����
    uname = input('\t �������µ��û���:')
    if uname=='':
        print('\t �û���������Ч!')
    else:
        #����Ƿ��Ѵ���ͬ����ע���û�
        if find(uname)>-1:
            print('\t��������û����Ѿ�ʹ�ã�����������û�!')
        else:
            pwd = input('\t ���������û���¼����:')
            if pwd=='':
                print('\t ��¼����������Ч!')
            else:
                userlist.append(user(uname,pwd))
                print('\t �ѳɹ�����û�!')
    input('\t ��Enter������......')
    ##����adduser()�������

##����find(namekey)�����Ƿ�����û���Ϊnamekey��ע���û�################################################################
def find(namekey):
    global userlist                                           #����ʹ��ȫ���û��б����
    #���ע���û��б�userlist�д�����namekeyֵͬ�����û�������λ�ã����򷵻�-1
    n=-1
    for x in userlist:
        if x.uname == namekey:
            break
    else:
        n = -1
    return n
    ##����find(namekey)�������

##����save()����ǰ�û���Ϣд���ļ����ñ���##############################################################################
def save():
    global userlist                                  #����ʹ��ȫ���û��б����
    #���û���Ϣд���ļ����ñ���
    myfile = open(r'userdata.bin','wb')         #���ļ�
    global userlist
    dump(userlist,myfile)
    myfile.close()
    print('\t �ѳɹ������û���Ϣ')
    input('\n\t ��Enter������......')
    ##����save()�������

#��������ʱ�������ļ��е��û�����
myfile = open(r'userdata.bin','rb')
x = myfile.read(1)
if x==b'':
    userlist = list()               #��ʼ�����б�
else:
    myfile.seek(0)
    userlist = load(myfile)   #���ļ�������ע���û��б�
myfile.close()                 #�ر��ļ�


#����ѭ����ʽϵͳ�����˵���ֱ��ѡ���˳�ϵͳ
while True:
    print('�û�ע����Ϣ����ϵͳ')
    print('\t1. ��ʽȫ����ע���û�')
    print('\t2.����/�޸�/ɾ���û���Ϣ')
    print('\t3. ������û�')
    print('\t4.�����û�����')
    print('\t5. �˳�ϵͳ')
    no = input('���������ѡ���Ӧ�˵�:')
    if no=='1':
        showall()               #��ʽȫ���û���Ϣ
    elif no == '2':
        check_update()            #ִ�в��ҡ��޸Ļ�ɾ������
    elif no == '3':
        adduser()                 #ִ��������û�����
    elif no == '4':
        save()                   #�����û�����
    elif no =='5':
        print('ллʹ�ã�ϵͳ���˳�')
        break
