#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import getpass
import os

script_path = os.path.dirname(__file__)
output_file = script_path + "/tls.sh"

print "\n\n\n\n\n\n\n\n\n\t\t Terminal Lock System INSTALL\n\n\n\n"

print "[*] Setting Password for authentication"
pw = getpass.getpass("Input Password >> ")
pw2 = getpass.getpass("Input Password (Re-typing) >> ")

if pw != pw2:
	print "[!] Fail to set password! (not match)"
	exit()

print "\n[*] Making tls.sh..."

content_front = """
#!/bin/bash
clear
trap "echo -ne \\"\\\\n[ Terminal Lock System ] Don't hack!!\\\\nInput Password >> \\"" {1..100} 2> /dev/null
echo -e "\\n\\n\\n\\n\\n\\n\\n\\n\\n\\t\\t\\t\\t Terminal Lock System\\n\\n\\n\\n"
echo -n "Input Password >> "
read -s pass
while [ "`echo -n $pass | md5sum | awk '{print $1}'`" != "
"""
content_behind = """
" ]
do
	echo -e "\\n[ Terminal Lock System ] Wrong Password!!"
	echo -n "Input Password >> "
	read -s pass
done
clear
"""
content_center = hashlib.md5(pw).hexdigest()

content = content_front.strip() + content_center.strip() + content_behind.strip()

f = open(output_file,"w")
f.write(content)
f.close()

os.chmod(output_file, 0700)

print "\n[*] All progress was finished!!"
print "\n[*] [Usage] ./tls.sh\n"
