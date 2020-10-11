import platform
import os

# Sanity checks
if os.environ.get('CONDA_DEFAULT_ENV') == None:
	print('You must run this program from within the Anaconda environment')
	os.exit(1)
if platform.system() != 'Windows':
	print('You must run this program on Windows')
	os.exit(1)

print("Installing advanced OpenSSH and git packages with Conda")
os.system('conda install -y git m2-openssh')


# Specify the directory to ensure that this script is running the correct commands
cmdPrefix = f"{os.environ['USERPROFILE']}\\Anaconda3\\Library"


print("Creating SSH client configuration directory")
sshDir = os.environ['USERPROFILE'] + "\\.ssh"
if not os.path.exists(sshDir):
    os.makedirs(sshDir)


print("Creating SSH client configuration file")
ukhf = 'UserKnownHostsFile ' + os.environ['USERPROFILE'] + '\\.ssh\\known_hosts'
ukhf = ukhf.replace('\\', '\\\\')
with open(sshDir + '\\config', 'w') as sshCfg: 
	sshCfg.write('# SSH client configuration file')
	sshCfg.write('\n')
	sshCfg.write(ukhf)


print("Configuring git to use a particular sshCommand")
sshCommand = f"{cmdPrefix}\\usr\\bin\\ssh -i {os.environ['USERPROFILE']}\\.ssh\\id_rsa -F {os.environ['USERPROFILE']}\\.ssh\\config"
sshCommand = sshCommand.replace('\\', '\\\\')
os.system(f'{cmdPrefix}\\bin\\git config --global core.sshCommand "{sshCommand}"')


print("Generating RSA public/private keypair")
os.system(f'{cmdPrefix}\\usr\\bin\\ssh-keygen -a 100 -P "" -f %USERPROFILE%\.ssh\id_rsa')


print("\n\n\n")
print("""Log into Bitbucket
Click on your Avatar -> Bitbucket settings -> Security -> SSH keys
Click on "Add key"
Copy and paste this data into Bitbucket
Click on "Add key" to save
Close the Notepad window when done""")
os.system('notepad %USERPROFILE%\.ssh\id_rsa.pub')
