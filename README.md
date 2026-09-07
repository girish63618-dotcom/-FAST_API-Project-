# -FAST_API-Project-
FastAPI is a Python web framework used to create APIs.

An API (Application Programming Interface) allows two different applications to communicate with each other.
Frontend (React)
      ↓
    API Request
      ↓
   FastAPI
      ↓
 Python code / Database / AI model
      ↓
   API Response
      ↓
Frontend
The FastAPI backend receives this request, gets restaurant information from the database, and sends it back:
[
  {
    "name": "ABC Restaurant",
    "location": "Bengaluru"
  },
  {
    "name": "XYZ Restaurant",
    "location": "Mysuru"
  }
]
Python can run normal programs, but if you want other applications to communicate with your Python program over the internet, you need a web framework.
