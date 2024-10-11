from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# In-memory "database"
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# Pydantic model for Task
class Task(BaseModel):
    task_title: str = Field(..., min_length=1, example="New Task")
    task_desc: str = Field(..., min_length=1, example="Complete the task")
    is_finished: bool = Field(default=False, example=False)

# GET: Retrieve a specific task by its ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = next((item for item in task_db if item["task_id"] == task_id), None)
    if task:
        return {"status": "ok", "task": task}
    raise HTTPException(status_code=404, detail={"error": "Task not found"})

# POST: Create a new task
@app.post("/tasks")
async def create_task(task: Task):
    new_task = {
        "task_id": len(task_db) + 1,
        "task_title": task.task_title,
        "task_desc": task.task_desc,
        "is_finished": task.is_finished
    }
    task_db.append(new_task)
    return {"status": "ok", "task": new_task}

# PATCH: Update an existing task by its ID
@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for existing_task in task_db:
        if existing_task["task_id"] == task_id:
            # Using exclude_unset to update only provided fields
            existing_task.update(task.dict(exclude_unset=True))
            return {"status": "ok", "task": existing_task}
    raise HTTPException(status_code=404, detail={"error": "Task not found"})

# DELETE: Remove a task by its ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global task_db
    task_db = [task for task in task_db if task["task_id"] != task_id]
    return {"status": "ok", "message": "Task deleted successfully"}