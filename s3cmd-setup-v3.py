#!/usr/bin/python3

import os
print('enable the epel repo or by default it may be installed')
enable_epel = os.system('yum-config-manager --enable epel')
print(enable_epel)
print("----------------------------------------------------------------------")
install_python2_pip = os.system('yum install python3-pip -y')
print(install_python2_pip)
print("----------------------------------------------------------------------")
upgrade_pip = os.system('pip3 install --upgrade pip')
print(upgrade_pip)
print("----------------------------------------------------------------------")
install_s3cmd = os.system('pip3 install s3cmd')
print(install_s3cmd)
print("----------------------------------------------------------------------")
create_user = os.system("radosgw-admin user create --uid=\"operator\" --display-name=\"S3 Operator\" --email=\"operator@example.com\" --access_key=\"12345\" --secret=\"67890\"")
print(create_user)
print("----------------------------------------------------------------------")
print('It will remove the default /root/.s3cfg file')
print("""For the configuration check the following things
        1. Enter the access-key & secret-key as per used above.
        2. Press enter in all the stages.
        3. Set - Use HTTPS protocol [No]: No.
        4. In last option - Test access with supplied credentials? [Y/n] n - use 'n'.
        5. Save settings? [y/N] y - Press 'y' here.""")
print("""

""")
print("---------check the above egs / defaults above--------------")
print("""

""")
s3cmd_configure = os.system('s3cmd --configure')
print(s3cmd_configure)
print("----------------------------------------------------------------------")
print('Make some changes to .s3cfg file')
hostname = input("Enter the hostname / machine-name, e.g-magna111: ")
port_number = input("Enter the port number e.g-8080/80: ")
print(hostname)
print(port_number)
print('Changing some configuration of the .s3cfg file')
os.system('sed -i -e \'s,^host_base *=.*,host_base = http://{}:{},;s,host_bucket *=.*,host_bucket = http://{}:{},;s,website_endpoint *=.*,website_endpoint = http://%(bucket)s.{}-%(location)s,\' /root/.s3cfg'.format(hostname, port_number, hostname, port_number, hostname))
print('.s3cfg file is edited successfully')
print("----------------------------------------------------------------------")
print('Check the s3cmd cmd is working fine - it should not return anything')
s3cmd_work = os.system('s3cmd ls')
print(s3cmd_work)
print("----------------------------------------------------------------------")
print('Create a bucket')
bkt_name = input("Enter a bucket name that you want to create: ")
bkt_create = os.system('s3cmd mb s3://{}'.format(bkt_name))
print(s3cmd_work)
print('Bucket created with name as {}'.format(bkt_name))
print("----------------------------------------------------------------------")
print('Create a file of size 100 MB')
file_name = input("Enter any file name you want to create of 100 MB: ")
file_create = os.system('head -c 100MB /dev/zero > {}'.format(file_name))
file_created = os.system('ls -l  {}'.format(file_name))
print(file_created)
print("----------------------------------------------------------------------")
print('Upload 100 same file on that created bucket')
#file_upload = os.system('for i in {1..100}; do s3cmd put {} s3://{}/{}${i}.iso & done'.format(file_name, bkt_name, file_name))
for i in range(1,101):
        os.system('s3cmd put {} s3://{}/{}{}.iso'.format(file_name, bkt_name, file_name, i))
print("Press ENTER once the uploading is done")
print("------------------------RGW IO OPERATION DONE---------------------------------")

