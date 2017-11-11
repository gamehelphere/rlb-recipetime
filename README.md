Author: Ryan Baclit
Email: gamehelphere@gmail.com
Date: 11/11/2017
Disclaimer:

This software does not come with a warranty of any kind. It is your responsibility to take care of your computer, software, and related setups. You will not hold the author responsible for any problems that may arise during your use of the software.

Description:

The WSGI Python web server to handle HTTP requests from my AngularJS 5 project. The server consists of two files, and those are the rlb-recipetime.py and the rlb_sql.py files. You still need additional files and softwares to make this server run for testing.

The full schema document in Open Document Sheet format is included. That file has the extension .ODS in this project. You will
need to use an office software like LibreOffice (http://www.libreoffice.org) to view the file.

A text version of the schema is in the table structure document included with the project. I ran the .schema command in the SQLite3 command line.

Installation

My setup uses Ubuntu Linux 17. If you have another operating system, make the necessary adjustments by reading proper documents online based on your setup.

1. Install Python 3 (http://www.python.org).
2. Download and install SQLite 3 (http://www.sqlite.org).
3. Download Bottle Py (http://bottlepy.org).
4. Download all the files of this project in a directory or folder.
5. Extract the Bottle Py archive and find the bottle.py file. Copy that file in the directory or folder where you downloaded the project files. Do not forget this or the project will not run!!!
6. Open a command line or terminal, and go to the directory where you placed the project files.
7. Type this command

python3 rlb-recipetime.py

and press Enter key. My Python 3 is named as python3, and if yours is different, type the correct name of your Python 3.

You will see an output like this

Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:5002/
Hit Ctrl-C to quit.

And it is telling you that the server is running at port 5002 and listening to all incoming hosts.

Testing and Troubleshooting

You can test the running server by opening a web browser and typing this on the address box.

http://localhost:5002

And you will see some Bottle Py related output like an Error: 404 Not Found in large font. If you see otherwise like server is down, review all the steps. You can always shutdown the running server by pressing Control+c and redo the steps. If the server is running and you still cannot see any Bottle Py related output in your web browser, it is most likely you have a firewall running that blocks port 5002. Find and research online on how to allow connections for hosts coming to 5002 for your operating system.
