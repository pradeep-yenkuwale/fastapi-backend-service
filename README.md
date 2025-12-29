
# FastAPI Backend Service Boilerplate

This is a **Python FastAPI boilerplate** project for learning and building backend REST APIs with **MongoDB**. It includes two main modules:

- **User Module:** CRUD operations for managing users
- **Auth Module:** Basic authentication (login)

This boilerplate is ideal for learning FastAPI, MongoDB integration, and structuring a modular API.

---

## Features

- RESTful API built with **FastAPI**
- **MongoDB** database integration
- Modular structure (`user` and `auth` modules)
- User CRUD operations
- User login endpoint
- Ready-to-use for personal projects or learning

---

## Tech Stack

- **Python 3.x**
- **FastAPI** – Web framework
- **MongoDB** – Database
- **Motor / PyMongo** – Async MongoDB driver
- **Pydantic** – Data validation and schema definition

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/pradeep-yenkuwale/fastapi-backend-service.git
cd fastapi-backend-service

## Install python packages with following command
pip install -r requirements.txt

## Run FastAPI server
python app/main.py
