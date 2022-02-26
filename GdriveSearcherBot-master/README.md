# GdriveSearcherBot
**Google Drive Searcher Bot Written In Python Using Pyrogram.
Moded by [@AbirHasan2005](https://github.com/AbirHasan2005).**

### Deploy to Heroku:
#### Via Button:
- [Import it as Private](https://github.com/new/import).
- [Follow Steps for Getting Google Cloud Console Project's `credentials.json` File](https://github.com/AbirHasan2005/GdriveSearcherBot#getting-google-oauth-api-credential-file).
- Send that `credentials.json` file to [@TokenPickle_Bot](https://t.me/TokenPickle_Bot) & get your `token.pickle` file.
- Upload that `token.pickle` file to your **Private** Imported GitHub Repository.
- Change Heroku Deploy Template Link with your **Private** Imported GitHub Repository Link.
- Press **Deploy to Heroku** Button.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AbirHasan2005/GdriveSearcherBot)

#### Via Heroku CLI:
##### Install Heroku on Linux:
```shell
apt install npm -y
npm i -g heroku
```
##### Login to Heroku CLI:
```shell
heroku login
heroku create app_name
```
##### Push to Heroku
Follow Steps for getting `credentials.json` file: [Here](https://github.com/AbirHasan2005/GdriveSearcherBot#getting-google-oauth-api-credential-file)
```shell
git clone https://github.com/AbirHasan2005/GdriveSearcherBot
cd GdriveSearcherBot
python3 generate_drive_token.py
git add .
git commit -am "Pushing to Heroku"
heroku git:remote -a app_name
git push heroku
```

### Deploy Locally:
##### Getting Google OAuth API credential file:

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of this bot, and rename it to credentials.json

**Here is video tutorial:**

[![YouTube](https://img.shields.io/badge/YouTube-Video%20Tutorial-red?logo=youtube)](https://youtu.be/B0_JY5QuWuE)
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Run these commands

```sh
pip3 install -U pip
pip3 install -U -r requirements.txt
python3 generate_drive_token.py
```
- Edit **config.py** with your own values
- Run  ```python3 main.py```  to start the bot.

### Docker Installation:
```sh
git clone https://github.com/thehamkercat/GdriveSearcherBot
cd GdriveSearcherBot
sudo docker build . -t GdriveSearcherBot
sudo docker run GdriveSearcherBot
```
### Credits:
- [@SVR666](https://github.com/SVR666) For Drive module.
- [@TheHamkerCat](https://github.com/TheHamkerCat/) For Noice Source Code.
