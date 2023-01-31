## Polls App 📊

This is a project for [**Platzi's Django course.**](https://platzi.com/cursos/django/)

![main page](https://user-images.githubusercontent.com/26366790/215878936-3072bad0-7e1d-4644-b901-741ebc98ef7f.png)
<br></br>
![detail page](https://user-images.githubusercontent.com/26366790/215879062-fb7df6f4-4eab-4344-9283-8acad08929d5.png)
<br></br>
![votes page](https://user-images.githubusercontent.com/26366790/215879347-e6921792-3622-4c5c-aa1e-2c6347f9e18b.png)
<br></br>

## Contents:
- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [Contributing](#contributing)
- [License](#license)

## Description

Polls app developed in Django for learning purposes, the app can load questions and assosiated choices in the admin panel from Django. Home view only show questions 
with more than two choices.

## Features:
- SQLite3 connection
- Manage app from Django admin
- Only show Question with more than 1 choice
- Votes saver

## Tech Stack

- Django, Python3.10, SQLite3, HTML, CSS.

## Installation
    
  1. Clone or download the repository:

  ` git clone https://github.com/Tecdaz/premios_platzi.git`

  2. Go to the project directory

  `cd premios_platzi/`

  2. Create and activate a virtual environment :
  
  Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
  
  3. Install dependencies:

  ` pip install -r requirements.txt`

## Run it locally

  1. Go to the proyect directory:
  
  `cd premios_platzi/premiosplatziapp/`

  2. Make migrations:
  
  `python3.10 manage.py migrate`

  3. Create super user:
  
  `python3.10 manage.py createsuperuser`

  4. Run server:
  
  `python3.10 manage.py runserver`

  5. Open a browser and go to: ` http://127.0.0.1:8000/admin/`, put your credentials from the third step and create questions with answers. Remember 
  that the question need minimum two choices to be displayed
  
  6. The last step is see your polls and vote `http://127.0.0.1:8000/polls/`
  
 ## Contributing

Contributions are always welcome!

- Fork this repository;

- Create a branch with your feature: `git checkout -b my-feature`;

- Commit your changes: `git commit -m "feat: my new feature"`;

- Push to your branch: `git push origin my-feature`.

## Authors

- [@tecdaz](https://www.github.com/tecdaz)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#polls-app-)

