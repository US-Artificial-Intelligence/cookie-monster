
This is a server for collecting cookie responses.

# How to first run

- Set up venv with:

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

- Change permissions on bash script: `chmod +x run.sh`

# How to run after it's set up

- Start the server

`nohup ./run.sh &`

- Connect ngrok (and use nohup)

`nohup ngrok http --domain=cookie-monster.ngrok.io 7999 &`
