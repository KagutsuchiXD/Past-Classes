## Organization and name scheme: 
Readme in the build directory, a folder named "cs3450" for the Django project and all the code, and a data folder for other files and assets such as the prototypes and diagrams.

## Version-control procedure: 
Pull requests for everything, merge your own if it's an arbitrary change.

## Tool stack: 
- Python version 3.7
- Django version 2.2.5
- Javascript
- Vue

## Build intructions: 
In the project root directory (this one) follow these commands for Linux:

$ python3 manage.py makemigrations
$ python3 manage.py migrate

Congratulations! Now your database is set up!

$ python3 manage.py runserver

Now your server is live locally. Go to localhost:8000 in your browser to access the site.

## Unit testing intructions: 
1. Navigate to the cs3450 directory
2. run python3 manage.py test auction
(if you are not on linux you will need to use a command other than 'python3' to execute the python file. On Windows the command is usually 'py', but use whatever command executes python 3.X in your terminal emulator.)

## System testing intructions: 
{update system testing instructions}

## Notes:
