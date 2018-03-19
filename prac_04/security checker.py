def main():
    """This program checks and grants access if username is in allowed usernames."""
    allowed_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
    'InterpreterInterface', 'StartServer', 'bob']
    message = "Access denied."
    user_input = str(input("Enter your username: "))
    for username in allowed_usernames:
        if username == user_input:
            message = "Access granted."
    print("{0}".format(message))

main()