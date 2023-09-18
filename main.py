import ftplib

# Fill Required Information
HOSTNAME = "yourhost"
USERNAME = "username"
PASSWORD = "password"
UPLOAD_FOLDER = 'htdocs/messenger'

# Inputs
username = input('Enter your name: ')
message = input('Enter your message: ')

# Vars
upload_file = username + message + '.txt'

try:
    # Connect FTP Server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"
except:
    print("ERR: Can't connect to server")


def upload(folder_path, filename):

    # Moving to the folder
    try:
        ftp_server.cwd(folder_path)
    except ftplib.error_perm:
        print('ERR: Folder does not exist')
        return

    # Read file in binary mode
    with open(filename, "rb") as file:
        # Command for Uploading the file "STOR filename"
        ftp_server.storbinary(f"STOR {filename}", file)


def create_message_file(username, message):
    try:
        with open(username + message + '.txt', 'w') as f:
            f.write(message)
    except FileNotFoundError:
        print("The directory not found does not exist")

create_message_file(username, message)
upload(UPLOAD_FOLDER, upload_file)

# Get list of files
ftp_server.dir()
