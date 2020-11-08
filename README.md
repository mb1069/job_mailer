# job_mailer
E-mail notifications for jobs running on remote servers with large execution times

## Installation
`pip install git+https://github.com/mb1069/job_mailer`

## Configuration
Define the following env variables:
- EMAIL_HOST: smtp host address
- EMAIL_USER: smtp username
- EMAIL_PASSWORD: smtp password
- EMAIL_RECIPIENT: recipient's email address

## Usage
Wrap your command using the command `mailme` 

Eg: `mailme sleep 70`