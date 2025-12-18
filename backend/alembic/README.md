# Alembic Migrations

This directory contains database migrations for the Task Manager application.

## Usage

\\\ash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# Show migration history
alembic history
\\\

## Migration Files

Migration files are stored in the \ersions/\ directory.
Each file represents a database schema change.
