# FastAPI Todo + MySQL (Simple Demo)

## Prereqs
- Python 3.10+
- MySQL server
- (recommended) virtualenv

## Setup
1. Clone/copy the project files.
2. Create and edit `.env` from `.env.example`:
   - Update `DATABASE_URL` like: `mysql+pymysql://user:pass@localhost:3306/fastapi_todo`
   - Set `JWT_SECRET_KEY`.
3. Create the database in MySQL:
   ```sql
   CREATE DATABASE fastapi_todo;
