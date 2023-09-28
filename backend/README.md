# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation
#### API Reference
##### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

##### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable



##### Endpoints
`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a two keys:
  - `success`: a boolean indicating the success of the API call, returns `True` when the call is successful.
  - `categories`: an object containing `id: category_string` key: value pairs representing the available categories.

```json
{ "success": True,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```



`GET '/questions`

- Fetches a paginated list of questions, the total number of questions, and a list of all available categories.
- Request Arguments: None
- Returns: An object containing:
  - success: a boolean indicating the success of the API call, returns True when the call is successful.
  - questions: an array of the current set of questions in the paginated series.
  - total_questions: an integer representing the total number of questions available.
  - categories: an object containing id: category_string key: value pairs representing the available categories.


```json
{
  "success": true,
  "questions": [
   {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    },
    // Additional questions if available
  ],
  "total_questions": 100,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

`GET '/categories/<int:category_id>/questions'`

- Fetches a list of questions associated with the specified category_id, along with the total number of questions in this category.
- Request Arguments:
  - `category_id` (path parameter, integer): The ID of the category for which questions are to be retrieved.
- Returns: An object containing:
  - success: a boolean indicating the success of the API call, returns True when the call is successful.
  - `questions`: an array of questions associated with the specified category_id.
  - total_questions: an integer representing the total number of questions available in the specified category.
  - `current_category`: a string representing the type of the specified category.
  - `categories`: an object containing id: category_string key: value pairs representing the available categories.

```json
{
  "success": true,
  "questions": [
   {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    },
    // Additional questions if available
  ],
  "total_questions": 100,
  "current_category": "Science",
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

`DELETE '/questions/<int:question_id>`

- Deletes the question of the given ID if it exists. Will return a 404 error if the question does not exist.
- Request Arguments:
  - `question_id` (path parameter, integer): The ID of the question to be deleted.
- Returns: An object containing:
  - success: a boolean indicating the success of the API call, returns True when the call is successful.
  - deleted: an integer representing the ID of the deleted question.


`POST '/questions'`

- This endpoint serves two purposes based on the presence of a `searchTerm` in the request body:
    1. **Search Questions:** If `searchTerm` is provided, it will return any questions for which the `searchTerm` is a substring of the question.
    2. **Create Question:** If `searchTerm` is not provided, it will create a new question using the details provided in the request body.

- Request Body:
  - If searching:
    - `searchTerm`: a string representing the term to search for in the questions.
  - If creating:
    - `question`: a string representing the question text.
    - `answer`: a string representing the answer text.
    - `category`: an integer representing the category ID of the question.
    - `difficulty`: an integer representing the difficulty level of the question (optional, default is 1).

- Returns:
  - If searching:
    - success: a boolean indicating the success of the API call, returns True when the call is successful.
    - questions: an array of questions for which the search term is a substring.
    - total_questions: an integer representing the total number of questions returned.
      ```json
      {
        "success": True,
        "questions": [
         {
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4
          },
          // Additional questions if available
        ],
        "total_questions": 10,
      }
      ```
  - If creating:
    - success: a boolean indicating the success of the API call, returns True when the call is successful.
    - created: an integer representing the ID of the newly created question.
      ```json
      {
        "success": True,
        "created": 19,
      }
      ```

`POST '/quizzes'`

- Fetches a random question for the quiz game. The question returned is one that has not been previously asked in the current game round, and if a category is specified, the question will belong to that category.

- Request Arguments:
    - `previous_questions`: An array of question IDs that have already been asked in the current quiz game round.
    - `quiz_category`: An object representing the selected category. It contains:
        - `id`: The ID of the selected category. If `id` is 0 or not specified, questions from all categories are considered.

- Returns: An object containing:
    - `success`: A boolean indicating the success of the API call, returns True when the call is successful.
    - `question`: An object representing the selected question, formatted as follows:
      ```json
      {
        "successs": True,
        "question": {
          "id": "integer",
          "question": "string",
          "answer": "string",
          "category": "integer",
          "difficulty": "integer"
        }
      }
      ```

- Errors:
    - 404: If there are no remaining questions that meet the specified criteria (i.e., not previously asked and within the specified category).

- Example:
    ```json
    {
        "success": True,
        "question": {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    }
    ```

- Notes:
    - The question is selected randomly from the available questions that meet the criteria of not being previously asked in the current round and belonging to the specified category (if any).


## Testing
To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
