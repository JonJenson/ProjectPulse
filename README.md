# ProjectPulse

ProjectPulse is a project management web application built with Django and PostgreSQL. It helps teams efficiently track and manage their projects, tasks, and collaborations.

## Features
- User authentication and role-based access control
- Create, update, and delete projects
- Assign tasks to team members
- Track project progress with status updates
- Collaboration features like comments and notifications
- Dashboard for quick insights
- PostgreSQL as the database backend

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Django Templates, HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Authentication**: Django built-in authentication system
- **Deployment**: Gunicorn, Nginx (optional for production)

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- Virtualenv

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ProjectPulse.git
   cd ProjectPulse
   ```
      
2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

