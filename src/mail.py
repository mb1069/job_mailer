import smtplib
import os
import subprocess
import sys


def check_setup():
    try:
        host = os.environ['EMAIL_HOST']
        port = os.environ['EMAIL_PORT']
        user = os.environ['EMAIL_USER']
        password = os.environ['EMAIL_PASSWORD']
        recipient = [os.environ['EMAIL_RECIPIENT']]
        return host, port, user, password, recipient
    except KeyError:
        print('Missing config: ')
        print(f"\tHost: {os.environ.get('EMAIL_HOST')}")
        print(f"\tPort: {os.environ.get('EMAIL_PORT')}")
        print(f"\tUser: {os.environ.get('EMAIL_USER')}")
        print(f"\tPassword: {os.environ.get('EMAIL_PASSWORD')}")
        print(f"\tRecipient: {os.environ.get('EMAIL_RECIPIENT')}")
        quit(1)


def get_cmd():
    cmd = sys.argv[1:]
    if len(cmd) == 0:
        print('No command!')
        quit(1)
    return cmd


def run_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error, process.returncode


def mail_finish(host, port, user, password, recipient, cmd, output, err_msg, err_code):
    '''

    :param host: smtp host address
    :param user: smtp sender username
    :param password: smtp sender password
    :param recipient: recipient's email address
    :param cmd: BASH command wrapped by instance
    :param output: stdout of above command
    :param err_msg: stderr of above command
    :param err_code: return code of above command
    :return: None
    '''
    cmd = ' '.join(cmd)
    if err_code == 0:
        header = f'Success!: {cmd}'
    else:
        header = f'Error {err_code}: {cmd}'

    message = f"""From: From Work <{user}>
    To: To Person <{', '.join(recipient)}>
    Subject: {header}

    Output was:
    {output}

    Error message:
    {err_msg}
    """

    with smtplib.SMTP(host, port=587) as session:
        session.set_debuglevel(1)
        # if your SMTP server doesn't need authentications,
        # you don't need the following line:
        session.login(user, password)
        session.sendmail(user, recipient, message)


def main():
    host, port, user, password, recipient = check_setup()

    cmd = get_cmd()

    output, err_msg, err_code = run_cmd(cmd)

    if output is not None:
        output = output.decode('UTF-8')
    if err_msg is not None:
        err_msg = err_msg.decode('UTF-8')

    if err_code == 0:
        print('Success')
    else:
        print('Fail')
    print('Output was:')
    print(output)
    print('Err was:')
    print(err_msg)

    mail_finish(host, port, user, password, recipient, cmd, output, err_msg, err_code)


if __name__ == '__main__':
    main()
