# Dara To-Do App

Welcome to Dara To-Do! ૮ • ﻌ • ა

Dara To-Do is a simple task management application built with Django. It allows users to create, update, delete, and search for tasks. Users can also mark tasks as completed or incomplete.

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Search for tasks
- Mark tasks as completed or incomplete

## Installation

To get started with the Dara To-Do app, follow these steps:

1. **Clone the repository:**
   git clone https://github.com/capydaraa/dara-to-do.git
   cd dara-to-do
2. **Create a virtual environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the dependencies:**
   pip install -r requirements.txt
4. **Apply the migrations**
   python manage.py migrate
5. **Run the development server**
   python manage.py runserver
6. Open your browser and navigate to:
   http://127.0.0.1:8000/

## Usage

- Add a Task: Fill out the form and click the "+ Add a Task" button.
- Edit a Task: Click the edit button next to the task you want to edit, make changes, and click "Update Task".
- Delete a Task: Click the delete button next to the task you want to delete and confirm the deletion.
- Search for Tasks: Use the search box to find tasks by title.
- Mark as Completed/Incomplete: Click the complete button to toggle the task's status between completed and incomplete.
