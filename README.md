App for streaming mini podcast and stories (as Tiktok and reels🙃)
setup :
```bash
#clone the repository 
git clone https://github.com/GHASSAN007/Podcast.git

#move to the directory
cd /podcast/Podcast_Mini_Backend/
# install requiermints 
python3 -m pip install -r requirements.txt

# make migrations 
python3 mange.py makemigrations
python3 mange.py migrate

#create admin user 
python3 mange.py createsuperuser

#get your ip adress by
python3 COMMON/ip_address.py

#Run server on your network 
python3 mange.py runserver {YOUR_IP_ADDRESS}:{PORT}

```


