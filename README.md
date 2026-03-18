# AI-Powered Health Diagnosis Assistant

## Overview
The AI-Powered Health Diagnosis Assistant is an innovative web application designed to provide users with personalized health diagnoses based on their input symptoms. By leveraging state-of-the-art AI technology, this application aims to assist individuals in identifying potential health concerns and recommend further actions. It is particularly beneficial for individuals seeking preliminary health advice before consulting a healthcare professional. Additionally, it serves as a valuable resource for healthcare providers looking to integrate AI-driven insights into their practice.

This application features a user-friendly interface where users can enter symptoms, receive AI-generated health recommendations, and access a wealth of health-related resources. It also includes a contact form for users to reach out with inquiries or feedback, ensuring an interactive and engaging user experience.

## Features
- **Symptom Checker**: Users can input symptoms to receive AI-driven health recommendations, helping them identify potential health issues.
- **Health Resources**: Access a curated list of health tips and educational content to stay informed about various health topics.
- **Contact Form**: Allows users to submit inquiries or feedback directly through the application, ensuring responsive communication.
- **Responsive Design**: Ensures optimal viewing experience across various devices, from desktops to mobile phones.
- **Database Integration**: Stores user information, symptoms, and resources in a SQLite database, ensuring data persistence and reliability.
- **Static and Dynamic Content**: Combines static resources (CSS, JS) with dynamic content rendering using Jinja2 templates.
- **RESTful API**: Provides endpoints for diagnosis, resources, and contact functionalities, facilitating seamless integration and interaction.

## Tech Stack
| Technology   | Description                      |
|--------------|----------------------------------|
| FastAPI      | Web framework for building APIs  |
| Uvicorn      | ASGI server for running FastAPI  |
| Jinja2       | Templating engine for HTML       |
| SQLite3      | Database for storing application data |
| HTML/CSS/JS  | Frontend technologies            |

## Architecture
The project is structured to separate concerns between the frontend and backend. The FastAPI backend serves HTML templates rendered with Jinja2 and handles API requests. The SQLite database is used to store user data, symptoms, and resources.

```plaintext
+-------------------+
|   Frontend (UI)   |
+-------------------+
| HTML/CSS/JS       |
|                   |
+-------------------+
         |
         v
+-------------------+
|    FastAPI App    |
+-------------------+
| API Endpoints     |
| - /api/diagnosis  |
| - /api/resources  |
| - /api/contact    |
+-------------------+
         |
         v
+-------------------+
|     SQLite DB     |
+-------------------+
| Tables:           |
| - users           |
| - symptoms        |
| - diagnoses       |
| - resources       |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-health-diagnosis-assistant-auto.git
   cd ai-powered-health-diagnosis-assistant-auto
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Start the application using Uvicorn:
```bash
uvicorn app:app --reload
```
Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path             | Description                                      |
|--------|------------------|--------------------------------------------------|
| GET    | /                | Home page with introduction and navigation       |
| GET    | /diagnosis       | Symptom checker page                             |
| GET    | /resources       | List of health resources                         |
| GET    | /about           | About us page                                    |
| GET    | /contact         | Contact form page                                |
| POST   | /api/diagnosis   | Submit symptoms and receive a diagnosis          |
| GET    | /api/resources   | Retrieve all health resources                    |
| POST   | /api/contact     | Submit contact form data                         |

## Project Structure
```
.
├── Dockerfile                # Docker configuration file
├── app.py                    # Main application logic
├── requirements.txt          # Python dependencies
├── start.sh                  # Shell script to start the application
├── static                    # Static files (CSS, JS)
│   ├── css
│   │   └── style.css         # Custom styles
│   └── js
│       └── main.js          # Client-side JavaScript
├── templates                 # HTML templates
│   ├── about.html            # About page
│   ├── contact.html          # Contact page
│   ├── diagnosis.html        # Symptom checker page
│   ├── index.html            # Home page
│   └── resources.html        # Resources page
└── health_diagnosis.db       # SQLite database file
```

## Screenshots
*Screenshots of the application interface will be included here.*

## Docker Deployment
Build and run the application using Docker:
```bash
docker build -t ai-health-diagnosis .
docker run -p 8000:8000 ai-health-diagnosis
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.