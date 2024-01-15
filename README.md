# Telegram Chat Bot using OpenAI api

## Run Development Server

- Copy and fill environment variables to an `.env` file

```bash
cp example.env .env
```

- Run development server:

With docker:

  ```bash
  docker compose up -d
  ```
  
Without docker:

  ```bash
  pip install -r requirements.txt
  python3 run.py
  ```
