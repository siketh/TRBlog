These instructions are just a modification of Max Halford's old Digital Ocean deployment instructions found [here.](https://github.com/MaxHalford/Flask-Boilerplate/blob/8bc1c2740e58bf8ef1d3849d382e4ed6e48b5dc9/deployment/Digital-Ocean.md)

I found that to successfully deploy my app I had to combine different guides as well as modify my .wsgi and .conf from the examples given. For this reason I found it worthwhile to include my own instructions to help anyone else trying to deploy their Flask app.

# Deployment Instructions

The following instructions are used to set up an Ubuntu VPS and deploy this application. Replace everything in '<>'

```sh
# Login and change password
ssh root@<IP>

# Add a new user "<USER>" and give them a password
adduser <USER>
# Give "<USER>" sudo rights
usermod -aG sudo <USER>

# I add my ssh key when creating my server, but I want the new user to have
# it too so **I copy it by running this from my workstation**
@local ssh-copy-id <USER>@<VPS IP>

# Change "PermitRootLogin yes" to "PermitRootLogin no"
# Change "PasswordAuthentication yes" to "PasswordAuthentication no"
sudo nano /etc/ssh/sshd_config

# Restart SSH Daemon
sudo systemctl reload sshd

# Switch to user "<USER>"
sudo su <USER>

# Configure the timezone
sudo dpkg-reconfigure tzdata

# Setup Python and Apache
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3

# Clone the repository containing the code
cd /var/www
sudo apt-get install git
sudo git clone <GIT REPO URL>
sudo chmod -R 777 <GIT REPO DIRECTORY>
cd <GIT REPO DIRECTORY>

# Create the virtual environment and install dependencies
sudo python3 -m venv flask
. flask/bin/activate
pip3 install -r deployment/requirements.txt
deactivate

# Configure and enable a virtual host
sudo cp deployment/<APACHE CONFIG FILENAME>.conf /etc/apache2/sites-available/
sudo a2ensite <APACHE CONFIG FILENAME>.conf
sudo service apache2 reload
sudo service apache2 restart

# Reboot the server
sudo reboot
```