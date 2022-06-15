 Podcast
Web app for streaming mini podcast and stories 
max length 5min 

setup
```bash
#clone the repository 
git clone https://github.com/GHASSAN007/Podcast.git

#move to the directory
cd Podcast_Mini_Backend/
# install requiermints 
python3 -m pip install -r requirements.txt

# make migrations 
python3 mange.py makemigrations
python3 mange.py migrate

#create admin user 
python3 mange.py createsuperuser

# run server
python3 manage.py runserver (ip adress):(port number) 

```


