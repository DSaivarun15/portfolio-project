# Portfolio Project Manager

A simple Django web application for managing portfolio projects. Users can view a list of projects and add new projects through a web form.

## Features

* View all projects
* Create new projects
* Track project progress
* Store project descriptions
* Automatically record project creation dates

## Project Structure

```
portfolio/
│
├── models.py
├── views.py
├── urls.py
├── forms.py
├── templates/
│   └── portfolio/
│       ├── index.html
│       └── create_project.html
```

## Project Model

The application uses a `Project` model with the following fields:

| Field       | Type          | Description                                |
| ----------- | ------------- | ------------------------------------------ |
| Title       | CharField     | Project title                              |
| description | TextField     | Detailed project description               |
| progress    | IntegerField  | Completion percentage                      |
| Created_at  | DateTimeField | Automatically generated creation timestamp |

## URL Routes

| URL     | View                  | Description          |
| ------- | --------------------- | -------------------- |
| `/`     | `projects_list`       | Display all projects |
| `/new/` | `create_project_view` | Create a new project |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/portfolio-project-manager.git
cd portfolio-project-manager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

or

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## Usage

### View Projects

Navigate to the home page to see all stored projects.

### Add a Project

Visit:

```
/new/
```

Fill out the project form and submit it to save a new project.

## Technologies Used

* Python
* Django
* SQLite (default Django database)
* HTML Templates

## Future Improvements

* Edit existing projects
* Delete projects
* Search and filter projects
* User authentication
* Project categories
* Progress bar visualization
* REST API integration

## License

This project is open source and available under the MIT License.
