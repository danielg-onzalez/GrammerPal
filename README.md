# Grammar Pal
A program that aims to be used as a web application to assist elementary school students in learing with interactive lessons and an AI Tutor for feedback and questions.

## Included
- Interactive lessons (1 per grade as a proof of concept)
- Sign-in/Sign-up through database integration
- AI Tutor to help mid lesson and usable for any feedback needs
- Parental controls to ensure maximum security and saftey in AI responses and website use

## Running the FastAPI Server

1. Clone the repository

2. Create and activate a virtual environment

3. Install the following:
   pip install fastapi uvicorn mysql-connector-python

4. Run the FastAPI server:
   uvicorn api.main_api:app --reload

5. Access the API:
   Swagger UI:
   http://127.0.0.1:8000/docs
   
   Health check endpoint:
   http://127.0.0.1:8000/test
