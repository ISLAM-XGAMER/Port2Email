# Port2Email
Python script that checks the open ports in the network and send an Email to your Email box
#### Coming Features
- [ ] The Error Handling Codes 
- [ ] Stored EmailSender
- [ ] Change The Email content feature
- [ ] fixing some issues 
## Important Note !!
### This step for the Sender Email you will use ,  Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). You can however, turn on/off this safety feature In The Sender Email Settings by going to the link below:
Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps
### you must do this step or you will get SMTPAuthenticationError when sending mail read this :
https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
### The Script Is Codded For Gmail Accounts And Not Tasted Yet At Another Accounts like yandex , yahoo ....  



## Requirment
- smtp library 
```
python pip install smtplib
```
- pyfiglet library
```
python pip pyfiglet
```
## Usage 

```
python Port2Email
```
