# Welcome to your Bootcamp SRE Capstone Project!

Remember that you can find the complete instructions for this project **[here](https://classroom.google.com/w/NTQyMDcxOTEwMzMw/tc/NTQyMDcxOTEwMzQ0)**.

If you have any questions, feel free to contact your mentor. We are here to support you.

# Setup

## Install dependencies

``` bash
pip3 install -r requirements.txt
```

## Setup dotenv (environment variables)

Copy the .env.example file to .env

``` bash
cp .env.example .env
```

Replace the values of the variables in the .env file

## Run project

``` bash
python3 api.py
```

## Endpoints

- [post] /login
- [get] /_health
- [get] /cidr-to-mask?value=?
- [get] /mask-to-cidr?value=?
