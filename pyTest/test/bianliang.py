#!/usr/bin/python3
#coding=utf-8
#--------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-05-23 下午5:19
#---------------------说明--------------------------
#  
#---------------------------------------------------
a = 102;
b = 201;
name = 'xiaoming';
iii = jjj = kkk = 1000.123;
z, x, c = 1, 2, 3;
radio = 10.17;
sum = a+b;
summ=111;
print(summ);
summ = sum* radio;
print(sum);

print(sum*radio);

print(type(name));
print(type(a));
print(type(sum));
print(type(radio));
print(type(summ));

print(isinstance(name,int));
print(isinstance(name,str));

# boolean test

a = True;
b = False;

print(a==b);
print (a);
print (type(a));
c = a+3;
print (c);
print (type(c));

# del 删除引用

del a,b;
#print (a);
print (c);

# 数值计算
a,b,c=1,2,3;
sum=a+b;
jian=c-a;
chen=b*c;
chu=c/b;
chu1=c//b;
mochu=c%b;
chenfan=b**c;
print(sum,jian,chen,chu,chu1,mochu,chenfan);


# String字符串操作

str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串








