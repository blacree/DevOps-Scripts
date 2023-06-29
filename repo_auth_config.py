import os
import subprocess

def awscodecommit_auth_config():
    config_ssh = False
    config_https_grc = False
    awscodecommit_options = """
    (1) SSH Configuration
    (2) HTTPS git-remote-codecommit(GRC) - Make sure you have AWS-CLI installed
    """

    while True:
        print(awscodecommit_options)
        option_selected = input("AWSCodeCommit (select a configuration option): ")
        try:
            option_selected = int(option_selected)
            if option_selected == 1:
                config_ssh = True
                break
            elif option_selected == 2:
                config_https_grc = True
                break
            else:
                print("[-] Invalid option")
        except:
            if len(option_selected) == 0:
                print("[-] Please select an option")
            else:
                print("[-] Invalid option")
    
    if config_ssh:
        ssh_key_id = input("SSH Key ID: ")
        home_directory = os.getenv("HOME")
        while True:
            path_to_identity_file = input("Enter file path to Identity File (SSH public key): ")
            check_path = os.path.isfile(path_to_identity_file)
            if check_path:
                break
            else:
                print("[-] File does not exist. Please provide a valid path")

        check_if_config_file_exists = os.path.exists(home_directory + "/.ssh/config")
        if check_if_config_file_exists == False:
            file_handler = open(home_directory + "/.ssh/config", "w")
            config_information="""Host git-codecommit.*.amazonaws.com
User {key_id}
IdentityFile {path_to_file}""".format(key_id=ssh_key_id, path_to_file=path_to_identity_file)
        else:
            file_handler = open(home_directory + "/.ssh/config", "a")
            config_information="""\n
Host git-codecommit.*.amazonaws.com
User {key_id}
IdentityFile {path_to_file}""".format(key_id=ssh_key_id, path_to_file=path_to_identity_file)
        file_handler.write(config_information)
        file_handler.close()
        print('\x1b[92m'+"[+] Configuration complete"+'\x1b[37m')

    if config_https_grc:
        successfull_config = 2
        print("Installing git-remote-codecommit")
        install_grc = subprocess.run(['sudo', 'pip', 'install', 'git-remote-codecommit'], text=True)
        if install_grc.returncode == 0:
            print("[+] Git-remote-codecommit Installed")
            successfull_config = successfull_config - 1
        else:
            print('\x1b[31m'+"[-] Git-remote-codecommit failed to install successfully (Failed command: sudo pip install git-remote-codecommit)"+'\x1b[37m')
        profile_name = input("Configuring AWS-CLI (Enter a profile name or press enter to use the default): ")
        if len(profile_name) == 0:
            configure_aws_cli = subprocess.run(['aws', 'configure'], text=True)
        else:
            configure_aws_cli = subprocess.run(['aws', 'configure', '--profile', profile_name], text=True)
        
        if configure_aws_cli.returncode == 0:
            successfull_config = successfull_config - 1
        
        if successfull_config == 0:
            print('\x1b[92m'+"[+] Configuration complete"+'\x1b[37m')
        else:
            print('\x1b[31m'+"[-] Configuration did not complete successfully"+'\x1b[37m')

def azuredevops_auth_config():
    username = input("User (Name of your Azure DevOps organization): ")
    home_directory = os.getenv("HOME")
    while True:
        path_to_identity_file = input("Enter file path to Identity File (SSH public key): ")
        check_path = os.path.isfile(path_to_identity_file)
        if check_path:
            break
        else:
            print("[-] File does not exist. Please provide a valid path")

    check_if_config_file_exists = os.path.exists(home_directory + "/.ssh/config")
    if check_if_config_file_exists == False:
        file_handler = open(home_directory + "/.ssh/config", "w")
        config_information="""Host ssh.dev.azure.com
User {user}
IdentityFile {path_to_file}""".format(user=username, path_to_file=path_to_identity_file)
    else:
        file_handler = open(home_directory + "/.ssh/config", "a")
        config_information="""\n
Host ssh.dev.azure.com
User {user}
IdentityFile {path_to_file}""".format(user=username, path_to_file=path_to_identity_file)
    file_handler.write(config_information)
    file_handler.close()
    print('\x1b[92m'+"[+] Configuration complete"+'\x1b[37m')

def github_bitbucket_auth_config():
    while True:
        proceed = input("[*] Note: Your private ssh key (if present) in your ~/.ssh/ directory would be changed. Do you wish to proceed? (yes/no | default = no): ")
        if proceed.lower() == 'yes':
            break
        elif proceed.lower() == 'no':
            return
        elif len(proceed) == 0:
            return
        else:
            print("[-] Invalid option")
    home_directory = os.getenv("HOME")
    while True:
        ssh_private_key = input("Enter file Path to your ssh private key: ")
        check_path = os.path.isfile(ssh_private_key)
        if check_path:
            break
        else:
            print("[-] File does not exist. Please provide a valid path")
    copy_file = subprocess.run(['cp', ssh_private_key, home_directory + '/.ssh/id_rsa'], text=True)
    if copy_file.returncode == 0:
        print('\x1b[92m'+"[+] Configuration complete"+'\x1b[37m')
    else:
        print('\x1b[31m'+"[-] File failed to copy successfully. You may not have the right permission to perform this operation"+'\x1b[37m')



def main():
    print("This Python script configures the requirements needed for authenticating with the following online repositories: AWSCodeCommit, Azure-DevOps Repo, GitHub, BitBucket")
    repositories = """
    (1) AWSCodeCommit (ssh-config & HTTPS-GRC)
    (2) Azure-DevOps Repo (ssh-config)
    (3) BitBucket / GitHub (ssh-config)
    """

    while True:
        print(repositories)
        repo_to_config = input("Which repository requirement would you like to conigure? (Select an option or type 'exit' to quit): ")
        try:
            repo_to_config = int(repo_to_config)
            if repo_to_config == 1:
                awscodecommit_auth_config()
            elif repo_to_config == 2:
                azuredevops_auth_config()
            elif repo_to_config == 3:
                github_bitbucket_auth_config()
            else:
                print("[-] Invalid option")
        except:
            #print(repo_to_config)
            if repo_to_config.lower() == 'exit':
                exit()
            elif len(repo_to_config) == 0:
                print("[-] Please select an option")
            else:
                print("[-] Invalid option")


main()