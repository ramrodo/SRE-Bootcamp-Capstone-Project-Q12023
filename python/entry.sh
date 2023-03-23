#!/bin/sh

if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec ~/.aws-lambda-rie/aws-lambda-rie /home/ramrodo/venvs/SRE-Bootcamp-Capstone-Project-Q12023/bin/python -m awslambdaric $1
else
    exec /usr/local/bin/python -m awslambdaric $1
fi