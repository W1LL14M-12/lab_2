Laboratory Activity 2: Working with HTTP actions and API parameters
In this lab, we’re creating a simple To-Do List API using FastAPI. The main goal is to get familiar with how to use HTTP methods to perform basic operations like adding, retrieving, updating, and deleting tasks.

The API has these key endpoints:

GET /tasks/{task_id} – This lets us get a specific task by its ID.
POST /tasks – Here, we can create a new task.
PATCH /tasks/{task_id} – This is used to update an existing task using its ID.
DELETE /tasks/{task_id} – This allows us to delete a task based on its ID.
Each of these actions returns a response that tells us if it worked or if there was an error. We also made sure to add some validation to check that the inputs are correct, like making sure task titles aren’t left empty. This activity helped us learn how to set up and manage a RESTful API with FastAPI, which was pretty cool

