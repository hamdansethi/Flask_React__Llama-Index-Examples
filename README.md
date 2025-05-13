Flask-React-Llama-Index-Example

This project demonstrates how to integrate a Flask backend with a React frontend, with additional functionality provided by the LlamaIndex for managing and searching through data.
Table of Contents

    Project Overview

    Technologies Used

    Setup Instructions

    Backend Setup (Flask)

    Frontend Setup (React)

    Running the Application

    License

Project Overview

This project is a full-stack web application with:

    A Flask backend for handling API requests, including data management.

    A React frontend to interact with the backend and display data dynamically.

    LlamaIndex for advanced search and indexing features in the backend.

The application allows users to manage and search for documents or any data indexed in a more efficient way with LlamaIndex integration.
Technologies Used

    Flask: A lightweight Python web framework for building APIs.

    React: A popular JavaScript library for building user interfaces, used for the frontend.

    LlamaIndex: An open-source library for creating indexes and performing advanced searches.

    Docker: Containerization for easy setup and deployment.

    Node.js: JavaScript runtime used by React.

    Python: Backend programming language for Flask.

    Postman: For testing API endpoints.

Setup Instructions
Prerequisites

Before setting up the project, ensure you have the following installed:

    Node.js for the React frontend

    Python for the Flask backend

    Docker (optional, for containerization)

Backend Setup (Flask)

    Clone the repository:

git clone https://github.com/hamdansethi/Flask_React__Llama-Index-Examples.git
cd Flask_React__Llama-Index-Examples

Navigate to the Flask directory (if it's in a subfolder like flask_backend):

cd flask_backend  # (replace with the actual folder name)

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Run the Flask server:

    python app.py  # or the script that starts the server

Frontend Setup (React)

    Navigate to the React project directory:

cd react_frontend

Install the required dependencies:

npm install

Run the React development server:

    npm start

This should start your React app, usually on http://localhost:3000.
Running the Application

    Backend: The Flask backend will be running on http://localhost:5000 (or another port if configured).

    Frontend: The React frontend will be running on http://localhost:3000 by default.

Ensure the Flask API is running before starting the frontend, as the frontend makes requests to the backend.
