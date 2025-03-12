# How this project way created: 
This webapp is a dummy project created by just promoting github copilot in VSCODE. 
The purpose to test the boundry of vide coding. 

# Task Manager Documentation

## Overview

This project is a web-based Task Manager application built using Flask. It allows users to manage projects and tasks, including adding, updating, and deleting projects and tasks. The application also supports drag-and-drop functionality for task management and color customization for projects.

## Project Structure

### Files and Directories

- [`app.py`](app.py): The main Flask application file.
- [`data.xlsx`](data.xlsx): The Excel file used to store project and task data.
- [`README.md`](README.md): The readme file for the project.
- [`static`](static): Directory containing static files such as JavaScript and CSS.
  - [`static/dragula.min.js`](static/dragula.min.js): Dragula library for drag-and-drop functionality.
  - [`static/style.css`](static/style.css): Custom CSS for styling the application.
- [`templates`](templates): Directory containing HTML templates.
  - [`templates/index.html`](templates/index.html): The main HTML template for the application.

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

4. Run the Flask application:
```sh
python app.py
```

## Usage
### Home Page
The home page displays a list of projects and their associated tasks. Users can add new projects and tasks, update task states, and delete projects and tasks.

### Adding a Project
To add a new project, enter the project name and select a color using the color picker, then click the "Add Project" button.

### Adding a Task
To add a new task to a project, enter the task name in the input field under the desired project and click the "Add Task" button.

### Updating Task State
Tasks can be moved between columns (Backlog, Ongoing, Finished) using drag-and-drop functionality. The task state is updated automatically.

### Deleting a Task
To delete a task, click the trash icon next to the task.

### Deleting a Project
To delete a project and all its tasks, click the trash icon next to the project header.

### Updating Task Notes
Double-click on a task to open the notes editor. The notes are saved automatically when the editor loses focus.

### Updating Task Name
Double-click on a task name to edit it. Press Enter or click outside the input field to save the new name.

### Updating Project Color
Click the dropper icon next to the project name to open the color picker. Select a new color to update the project color.

### API Endpoints
GET /
Renders the home page with the list of projects and tasks.

POST /add_project
Adds a new project.

Request parameters:
project: The name of the project.
color: The color of the project (optional, default: #e0f7fa).
POST /add_task/<int:project_id>
Adds a new task to a project.

Request parameters:
task: The name of the task.
POST /update_task_state/<int:task_id>
Updates the state of a task.

Request body:
state: The new state of the task (backlog, ongoing, finished).
POST /update_task_notes/<int:task_id>
Updates the notes of a task.

Request body:
notes: The new notes for the task.
POST /update_task_name/<int:task_id>
Updates the name of a task.

Request body:
name: The new name of the task.
POST /delete_task/<int:task_id>
Deletes a task.

POST /delete_project/<int:project_id>
Deletes a project and all its tasks.

POST /update_project_color/<int:project_id>
Updates the color of a project.

Request body:
color: The new color for the project.
Data Storage
The project and task data are stored in an Excel file (data.xlsx). The data is loaded from the file when the application starts and saved back to the file whenever changes are made.

## Build exe
```
pyinstaller --name TaskManager --onefile --add-data "templates;templates" --add-data "static;static" app.py

cd dist
TaskManager.exe
```

## Dependencies
Flask
pandas
openpyxl
License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Dragula for drag-and-drop functionality.
Quill for rich text editing.
Font Awesome for icons.
Marked for Markdown parsing.
Contact
For any questions or issues, please contact your-email@example.com.

