
# 🎧 Fog 

<font size="5">Listening to 2h Podcast maybe tough, Fog is the solution, you can listen to podcast with short length (5min max).</font >

&nbsp; &nbsp; 
## 📥 Installation

&nbsp;

Clone the repository 
```sh
git clone https://github.com/GHASSAN007/Podcast.git
```

Move to the directory
```sh
cd Podcast_Mini_Backend/
```

Install requirements
```sh
python3 -m pip install -r requirements.txt
```
Add SECRET_KEY to settings.py  
```python
SECRET_KEY= #Create any key
```

Make migrations 
```sh
python3 mange.py migrate
```

Create admin user 
```sh
python3 mange.py createsuperuser
```

Run server
```sh
python3 manage.py runserver (ip address):(port number) 
```
&nbsp;
## ⭐ Features  
- Uploading, Updating, Deleing Fogs
- Create, Updating, Deleting Users
- Create, Updating, Deleting Channels 
- Like, Comment to the Fog
- Creating privet Fogs

> Note: All these features are working only through API
&nbsp;
## ⚙️ Working On 
- Designing website layout



