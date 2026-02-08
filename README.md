# TinkerHub Dashboard

A Django-based dashboard application that fetches participant data from a Google Sheet, generates tech-themed aliases and avatars, and displays them in a responsive UI.

## Features

- **Google Sheets Integration**: Fetches real-time participant data (Name, Role, Domain) from a public Google Sheet CSV.
- **Tech Aliases**: Automatically generates consistent, tech-inspired aliases (e.g., `name.sh`, `0xname`) from user names.
- **Avatars**: Generates unique robot avatars using the DiceBear API based on the alias.
- **Easter Egg**: Includes a hidden "antigravity" easter egg in the code.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [git](https://git-scm.com/)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd tinkerhub-dashboard
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file** in the root directory (same level as `manage.py`).

2.  **Add the following environment variables:**

    ```env
    # Security key for Django (keep this secret in production)
    DJANGO_SECRET_KEY=django-insecure-your-secret-key-here

    # URL to the published Google Sheet CSV
    # Example: https://docs.google.com/spreadsheets/d/e/.../pub?output=csv
    GSHEET_URL=https://docs.google.com/spreadsheets/d/your-sheet-id/pub?output=csv
    ```

## Database Setup

Run the standard Django migrations to set up the SQLite database:

```bash
python manage.py migrate
```

## Running the Application

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the dashboard:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Logic Overview

-   **Alias Generation**: The `generate_tech_alias` function in `dashboard/views.py` creates a deterministic tech-themed suffix for each name.
-   **Avatar Generation**: The `generate_avatar_url` function uses the generated alias as a seed for the DiceBear Bottts style.

## Troubleshooting

-   **Missing Data**: Ensure your `GSHEET_URL` is correct and the Google Sheet is published to the web as a CSV.
-   **Environment Variables**: Make sure `.env` is in the root directory and you have restarted the server after making changes to it.
