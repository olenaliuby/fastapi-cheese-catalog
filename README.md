# FastAPI Cheese Catalog

## Description
The FastAPI Cheese Catalog is a web application that allows you to manage and catalog different types of cheeses. It provides a set of endpoints for creating, listing, and viewing cheese types and individual cheeses.

## Endpoints

1. **Create Cheese Type**
   - Endpoint: `/cheese_types/` (POST)
   - Description: Create a new cheese type with a name and description.

2. **List All Possible Cheese Types**
   - Endpoint: `/cheese_types/` (GET)
   - Description: Retrieve a list of all available cheese types.

3. **Create Cheese**
   - Endpoint: `/cheeses/` (POST)
   - Description: Create a new cheese with details such as name, description, packing type, and cheese type.

4. **List All Cheeses**
   - Endpoint: `/cheeses/` (GET)
   - Description: Retrieve a list of all cheeses. Optionally, you can filter the results by packing type and cheese type.

5. **Detail Cheese**
   - Endpoint: `/cheeses/{cheese_id}/` (GET)
   - Description: Retrieve detailed information about a specific cheese by providing its unique identifier (`cheese_id`).

## Stack

- FastAPI: A modern web framework for building APIs with Python.
- SQLAlchemy: An Object-Relational Mapping (ORM) library for database interaction.
- Pydantic: A data validation and serialization library, used for API input and output validation.
- Alembic: A tool for managing database schema migrations.

## How to Run

To run the FastAPI Cheese Catalog application, follow these steps:

1. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. Apply database migrations using Alembic:

   ```bash
   alembic upgrade head
   ```

3. Start the FastAPI application using Uvicorn with automatic reloading for development:

   ```bash
   uvicorn main:app --reload
   ```
   
Your FastAPI Cheese Catalog should now be running locally at `http://127.0.0.1:8000/`. You can access the API using your preferred API client or web browser.
