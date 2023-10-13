import myparamiko
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

ssh_client = myparamiko.connect('192.168.0.133', 22, username, password)
shell = myparamiko.get_shell(ssh_client)

new_user = input('Enter new username: ')
new_passwd = getpass.getpass('Enter new password: ')

command = "sudo useradd -m -d /home/" + new_user + " -s /bin/bash " + new_user
myparamiko.send_command(shell, command)
myparamiko.send_command(shell, new_passwd)
print("A new user " + new_user + " has been created")

answer = input("Display the new user information? (yes/no): ")
if answer == 'yes' or answer == "y":
    command = "sudo cat /etc/passwd | grep " + new_user
    myparamiko.send_command(shell, command)
    print(myparamiko.show(shell))

myparamiko.close(ssh_client)
