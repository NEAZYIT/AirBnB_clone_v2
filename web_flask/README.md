# AirBnB clone - Web framework

An implementation of an AirBnB clone using a web framework.

## Table of Contents

- [Requirements](#requirements)
- [Python Scripts](#python-scripts)
- [HTML/CSS Files](#htmlcss-files)
- [More Info](#more-info)
- [Manual QA Review](#manual-qa-review)
- [Video Library](#video-library)
- [Tasks](#tasks)

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Mandatory README.md file
- Code adheres to PEP 8 style (version 1.7)
- All files are executable
- File length tested using `wc`
- Modules, classes, and functions have documentation
- HTML/CSS files W3C compliant, validate with W3C-Validator
- CSS files in `styles` folder, images in `images` folder
- No use of `!important` or id (`#...`) in CSS files
- All tags in uppercase
- Screenshots from Chrome 56.0.2924.87
- No cross-browser support

## Python Scripts

- Install Flask: `$ pip3 install Flask`
  
### Tasks

### 0. Hello Flask!
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Route `/`: display "Hello HBNB!"
  - Use `strict_slashes=False` in the route definition

### 1. HBNB
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
  - Use `strict_slashes=False` in route definition

### 2. C is fun!
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by value of `text` (replace underscore with space)
  - Use `strict_slashes=False` in route definition

### 3. Python is cool!
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by value of `text` (replace underscore with space)
    - `/python/<text>`: display "Python " followed by value of `text` (replace underscore with space)
    - Default value of `text`: "is cool"
  - Use `strict_slashes=False` in route definition

### 4. Is it a number?
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by value of `text` (replace underscore with space)
    - `/python/(<text>)`: display "Python " followed by value of `text` (replace underscore with space)
    - Default value of `text`: "is cool"
    - `/number/<n>`: display "`n` is a number" only if `n` is an integer
  - Use `strict_slashes=False` in route definition

### 5. Number template
- Start a Flask web application:
  - Listen on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display "Hello HBNB!"
    - `/hbnb`: display "HBNB"
    - `/c/<text>`: display "C " followed by value of `text` (replace underscore with space)
    - `/python/(<text>)`: display "Python " followed by value of `text` (replace underscore _ symbols with a space)
    - Default value of `text`: "is cool"
    - `/number/<n>`: display "`n` is a number" only if `n` is an integer
    - `/number_template/<n>`: display an HTML page only if `n` is an integer:
        - H1 tag: "Number: `n`" inside the tag BODY
  - Use `strict_slashes=False` in route definition

### Task 6: Odd or Even?

**Description:** Implement a function that checks whether a given number is odd or even. The function should take an integer as input and return a boolean indicating whether the number is odd or even.

**Implementation Details:** The function should use a simple mathematical check by dividing the number by 2. If the remainder is 0, the number is even; otherwise, it's odd.

### Task 7: Improve Engines

**Description:** Enhance the search engine functionality to allow users to filter results based on various criteria such as price, location, amenities, etc. This task involves expanding the search functionality to provide more refined and relevant results to users.

**Implementation Details:** Implement additional query parameters in the search function and modify the database query to consider these parameters when fetching results.

### Task 8: List of States

**Description:** Create an endpoint that returns a list of states available in the system. This endpoint will be used to populate a dropdown menu for users to select states in various parts of the application.

**Implementation Details:** Fetch the list of states from the database and format the response in a JSON format to be used by the frontend.

### Task 9: Cities by States

**Description:** Develop an API endpoint that retrieves a list of cities based on a selected state. This endpoint will provide the cities associated with the chosen state for users to select when searching for accommodations.

**Implementation Details:** Retrieve the cities corresponding to the selected state from the database and format the response to provide a list of cities in JSON format.

### Task 10: States and State

**Description:** Write a script that starts a Flask web application with specific requirements for handling states and cities.

**Mandatory Requirements:**
- Your web application must listen on 0.0.0.0, port 5000.
- Use storage for fetching data from the storage engine (FileStorage or DBStorage) by importing `storage` from models (`from models import storage`).
- Load all cities of a State:
  - If using DBStorage, utilize the cities relationship.
  - Otherwise, use the public getter method `cities`.
- Remove the current SQLAlchemy Session after each request using `@app.teardown_appcontext`.
- Routes:
  - `/states`: Display an HTML page with a list of all State objects present in DBStorage, sorted by name.
  - `/states/<id>`: Display an HTML page showing cities linked to the State with the given id or show "Not found!" if no State is found.
- Use the option `strict_slashes=False` in route definitions.
- Import a provided dump file (`7-dump.sql`) for initial data.
  
**Setup Instructions:**
- Ensure a valid `setup_mysql_dev.sql` exists in your AirBnB_clone_v2 repository.
- Confirm all tables are created by running specific commands.

### Task 11: HBNB filters

**Description:** Write a script that starts a Flask web application to display an HTML page similar to a previous project.

**Mandatory Requirements:**
- Similar setup to Task 10 with specific HTML page display requirements and files to copy to the `web_flask/static` folder.
- Import a provided dump file (`10-dump.sql`) for initial data.

**Setup Instructions:**
- Similar to Task 10, ensure valid setup files and database tables exist.

## How to Run

To run this project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Set up the required environment variables.
4. Run the Python files associated with the tasks.

## Contributors

- [NEAZYIT](https://github.com/NEAZYIT) - Full-Stack Engineer/Full-Stack-Entwickler
