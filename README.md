<div align="center">
 <h1>Atenea</h1>
</div>

<br><br>
## Description
Service for processing incoming messages using AI models

<br><br>
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [More info](#more-info)

<br><br>
## Requirements

 ```
Python v3.13 or later
 ```

<br><br>
## Installation
  1. First clone this repository:
     
      ```
      git clone https://github.com/GabrielLaTorre/Atenea.git
      ```
  2. Create a virtual environment to avoid conflicts with local packages on your machine:

      ```
      pip install virtualenv
      virtualenv venv
      ```

  3. Activate virtual environment

      ```
      source venv/bin/activate
      ```

  4. Install the required dependencies:

      ```
      pip install -r requirements.txt
      ```

  5. Create a .env file on root and set the necessary environment variables

     ```
       LANGSMITH_TRACING=
       LANGSMITH_ENDPOINT=
       LANGSMITH_API_KEY=
       LANGSMITH_PROJECT=
       OPENAI_API_KEY=
       SUPABASE_URL=
       SUPABASE_API_KEY=
       INCOMING_MESSAGE_
       OUTGOING_MESSAGE_QUEUE_URL=
       AWS_REGION=
       AWS_ACCESS_KEY_ID=
       AWS_SECRET_ACCESS_KEY=
      ```
<br><br>
## Usage

1 Run the command

    ```
    python src/main.py
    ```

2. Go to bot https://t.me/final_expense_bot and send the start command

    ```
    /start
    ```

<br><br>
## More info

This project is responsible for processing messages using AI models to identify whether they are expenses. Once the message is identified, it will store the information in a database and send a response to the [Hermes](https://github.com/GabrielLaTorre/Hermes) connector, who will notify the user through the Telegram API.
