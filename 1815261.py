#!/usr/bin/python3

import os, sys

print('Create a file of size 100 MB')
file_name = 'swift.dat'
file_create = os.system('head -c 100MB /dev/zero > {}'.format(file_name))
file_created = os.system('ls -l  {}'.format(file_name))
print(file_created)
print("----------------------------------------------------------------------")
print("Create 1000 buckets and upload above file on that created bucket")
for i in range(1,1001):
        os.system('swift -V 1.0 -A http://10.8.128.107:8080/auth/v1 -U operator:swift -K 8zrYBvc0XLia0C2Djl8KQVHQ4JQWbXCob7zkYqhH post swift-tesst-container{}'.format(i))
        print("Container {} created.".format(i))
        os.system('swift -V 1.0 -A http://10.8.128.107:8080/auth/v1 -U operator:swift -K 8zrYBvc0XLia0C2Djl8KQVHQ4JQWbXCob7zkYqhH upload swift-tesst-container{} {}'.format(i, file_name))
        print("{} is uploaded to container {}.".format(file_name, i))
print("----------------------------------------------------------------------")
print("Containers list")
os.system("swift -V 1.0 -A http://10.8.128.107:8080/auth/v1 -U operator:swift -K 8zrYBvc0XLia0C2Djl8KQVHQ4JQWbXCob7zkYqhH list")
print("----------------------------------------------------------------------")
print("Users stats")
os.system("swift -V 1.0 -A http://10.8.128.107:8080/auth/v1 -U operator:swift -K 8zrYBvc0XLia0C2Djl8KQVHQ4JQWbXCob7zkYqhH stat")
print("---------------------------------END-------------------------------------")

