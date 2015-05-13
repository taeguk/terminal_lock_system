#!/bin/bash
clear
trap "echo -ne \"\\n[ Terminal Lock System ] Don't hack!!\\nInput Password >> \"" {1..100} 2> /dev/null
echo -e "\n\n\n\n\n\n\n\n\n\t\t\t\t Terminal Lock System\n\n\n\n"
echo -n "Input Password >> "
read -s pass
while [ "`echo -n $pass | md5sum | awk '{print $1}'`" != "70bef168e62a4008c3a38acdfdfba1a9" ]
do
	echo -e "\n[ Terminal Lock System ] Wrong Password!!"
	echo -n "Input Password >> "
	read -s pass
done
clear