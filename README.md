# checkmate

basically gandalf as a discord bot

## create the discord bot

follow this [tutorial](https://discordpy.readthedocs.io/en/stable/discord.html) to create your discord bot.

you must invite the bot on the discord server you want it to authenticate users!

## installation

the bot requires at least python 3.8

```bash
git clone https://github.com/EsprIx/checkmate
```

then run under the `checkmate` directory

```bash
pip install -r requirements.txt
pip install -U git+https://github.com/Rapptz/discord.py
```

under the `checkmate` directory, you need to create a `credentials.json` as well as a `config.json` file.

they should look like this:

`credentials.json` :

```json
{
    "token": "str",
    "gmailUser": "str",
    "gmailPassword": "str"
}
```

| Key           | Description                                                               | Default | Required |
| ------------- | ------------------------------------------------------------------------- | ------- | -------- |
| token         | secret token of your discord bot                                          | None    | True     |
| gmailUser     | gmail address from which you want the bot to send the emails to the users | None    | True     |
| gmailPassword | gmail password of the above gmail address                                 | None    | True     |

`config.json` :

```json
{
    "prefix": "str",
    "checkedRoleName": "str",
    "uncheckedRoleName": "str",
    "checkChannelName": "str",
    "userInDbEndpoint": "str",
    "addUserEndpoint": "str",
    "checkChannelMessage": "str",
    "basicErrorMessage": "str",
    "checkProcessAskEmailMessage": "str",
    "checkProcessAskCodeMessage": "str",
    "checkProcessTimeOutErrorMessage": "str",
    "checkProcessAccountErrorMessage": "str",
    "checkProcessCodeErrorMessage": "str",
    "checkProcessEmailErrorMessage": "str",
    "checkProcessCompletedMessage": "str"
}
```

| Key                             | Description                                                                 | Default | Required |
| ------------------------------- | --------------------------------------------------------------------------- | ------- | -------- |
| prefix                          | the prefix of your discord bot                                              | None    | True     |
| checkedRoleName                 | the display name of the checked role                                        | None    | True     |
| uncheckedRoleName               | the display name of the unchecked role                                      | None    | True     |
| checkChannelName                | the display name of the verification channel                                | None    | True     |
| userInDbEndpoint                | the endpoint to check if the user email is in the db                        | None    | True     |
| addUserEndpoint                 | the endpoint to link the discord user id to it's account on your website    | None    | True     |
| checkChannelMessage             | the message sent in the check channel below the "start verification button" | None    | True     |
| basicErrorMessage               | the message shown when an unknown error raises                              | None    | True     |
| checkProcessAskEmailMessage     | the message shown to the user to ask them their email                       | None    | True     |
| checkProcessAskCodeMessage      | the message shown to the user to ask them to enter the code they received   | None    | True     |
| checkProcessTimeOutErrorMessage | the message shown to the user when they take too long to reply              | None    | True     |
| checkProcessAccountErrorMessage | the message shown to the user when they are not registered on the website   | None    | True     |
| checkProcessCodeErrorMessage    | the message shown to the user when they enter an invalid code               | None    | True     |
| checkProcessEmailErrorMessage   | the message shown to the user when they enter an invalid email              | None    | True     |
| checkProcessCompletedMessage    | the message shown to the user when they complete the verification           | None    | True     |

## run the bot

execute the `client.py` file at the root of the `checkmate` directory.

```bash
python client.py
```

## license

[MIT](https://choosealicense.com/licenses/mit/)

made with 🤍 by Bonsaï#8521
