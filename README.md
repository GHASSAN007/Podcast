 Podcast
Webapp for streaming mini_podcast and stories 
max length 2min 

setup
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

# run server
python3 manage.py runserver 

#if you want to run it in your network run 
python3 mange.py runserver --network

```


