# alkye_blog
Simple blog application using Django and Django REST Framework, integrating basic CRUD (Create, Read, Update, Delete) functionalities.

## Installation

### Requirements
- Python
- Django
- Django rest Framework

  Complete list available in requirements.txt file

### Quickstart
- Clone the repo.  
    ```bash
    git clone https://github.com/shaweta/alkye_blog.git
    ```

- Inside the backend folder, make a virtual environment and activate it 
    ```bash
    cd myblog
    python -m venv env 
    source env/bin/activate(./env/Scripts/activate)

    ```

- Install requirements from requirements.txt
    ```
    pip install -r requirements.txt
    ```

- Makemigrations and migrate the project
    ```
    python manage.py makemigrations && python manage.py migrate
    ```

- Create a superuser
    ```
    python manage.py createsuperuser
    ```

- Runserver
    ```
    python manage.py runserver
    ```

**Note: After running the server, you can use the api inside browser or you can use Postman to make api calls. Make sure in each api call, you provide username, password by creating a user
Here  token authentication is applied so when testing with postman or thunder client in VSCode make sure to pass token in the header while making calls.
.**



While working with api in browser, you can login using `http://127.0.0.1:8000/api/` link.


## API
<details>
<summary> Post model </summary> 

- POST:
    - title: string(unique),
    - content: text,
    - author: text
    - published_date:Datetime field

</details>

<details>
<summary> Comments Model </summary>


</details>





### Endpoints

Brief explanation of endpoints:

| Function                                                                                               | REQUEST    | Endpoint                                                | Authorization | form-data                                 |
|--------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------|---------------|-------------------------------------------|
| Create new Post                                                                                      | POST       | http://127.0.0.1:8000/api/posts/                      | Token Auth                  |
| Returns list of all existing Posts                                                                   | GET        |  http://127.0.0.1:8000/api/posts/                     | Token Auth    |                                           |
| Returns the detail of an Post instance                                                               | GET        | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth    |                                           |
| Update the detail of an Post instance                                                                | PUT, PATCH | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth   |                                           |
| Delete an Post instance                                                                              | DELETE     | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth    |                                           |
| Returns a list of all Comments on  existing Post                                                         | GET        | http://127.0.0.1:8000/api/posts/{int:id}/comments  | Token Auth  |                                           |
| Creates a new comment                                 | POST       | http://127.0.0.1:8000/api/api/post/{int:id}/comments              | Token Auth   |  |
| Returns the details comment.                                                     | GET        | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth    |                                           |
| Update or edit an existing Comment . Returns updated Purchase orders                                  | PUT, PATCH | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth   |  |
| Deletes the existing comment                                                                   | DELETE     | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth    |                                           |

 
You can use  VSCode thunder client or postman to interact with the apis and to get access of apiyou need to give Token in Header 
Adding Pictures of my Tests using thunderclient
