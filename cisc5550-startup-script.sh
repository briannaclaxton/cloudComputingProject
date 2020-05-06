#Install Python Pip
sudo apt install -y python3-pip
pip3 install flask

#Install git
sudo apt-get install -y git

#Fetch files
git clone https://github.com/briannaboyce/cloudComputingProject
cd cloudComputingProject

#Start server
python3 todolist.py

