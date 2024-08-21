# IDI Take-Home Task
### Overview
This project is part of the IDI Take-Home assignment designed to evaluate the ability to handle a large dataset, package it into a queryable structure, and build a system that can efficiently perform specific queries. The project is implemented using Python, Flask, MongoDB, and Docker. The task is open-ended, and while it's not necessary to complete it fully, the focus is on demonstrating problem-solving skills, attention to detail, and effective documentation.

### Architecture
![Architecture Diagram](https://github.com/koushik0509/Fflask-NoSQL/blob/main/app/images/architecture_diagram.png)

The architecture consists of:

- Flask API: Handles client requests and queries data from MongoDB.
- MongoDB: Stores the tweet data and allows for efficient querying.
- Docker: Containerizes the Flask app and MongoDB, ensuring consistent deployment.
- PyCharm: Used for development and debugging.
### Design Choices
- MongoDB: Chosen for its ability to efficiently handle large datasets and complex queries.
- Flask: Lightweight and easy to set up for building RESTful APIs.
- Docker: Ensures the application runs consistently across different environments.
- Testing: Implemented with pytest to validate functionality and data integrity.

## Project Structure

Flask-NoSQL
│<br/>
├── app/<br/>
│ ├── run.py # Flask application<br/>
│ ├── init.py # Initialize the Flask app<br/>
│ ├── routes.py # Functions to handle data queries<br/>
│ ├── requirements.txt # List of Python dependencies<br/>
│ └── Dockerfile # Dockerfile for building the Flask app container<br/>
│ ├── docker-compose.yml # Docker Compose file to manage the services<br/>
│ ├── load/<br/>
│ │ ├── DataReader.py # Script for data ingestion into MongoDB<br/>
│ │ └── resources/<br/>
│ │ └── correct_twitter_201904.tsv # Input Data<br/>
│<br/>
├── tests/<br/>
│ ├── test_ingestion.py # Unit tests for data ingestion<br/>
│ └── test_queries.py # Unit tests for query functions<br/>
├── README.md # Project documentation<br/>
└── images/<br/>
└── architecture_diagram.png # Architecture diagram<br/>


## Setup and Installation
Prerequisites
- Python 3.8+
- Docker and Docker Compose
- MongoDB (if not using Docker)
- PyCharm (recommended IDE)
### Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/koushik0509/Fflask-NoSQL.git
cd app
#### Install Python Dependencies:

If running locally without Docker, set up a virtual environment and install dependencies:

python3 -m venv venv<br/>
source venv/bin/activate<br/>
pip install -r app/requirements.txt<br/>
Run with Docker:<br/>

Build and start the containers using Docker Compose:<br/>
docker-compose up --build<br/>
This will start the Flask app and MongoDB services.<br/>

### Data Ingestion:
Use the provided DataReader.py script to load the data into MongoDB:

python app/load/DataReader.py --file app/load/resources/correct_twitter_201904.tsv<br/>
Alternatively, if using Docker:

docker exec -it flask_app python app/load/DataReader.py --file app/load/resources/correct_twitter_201904.tsv<br/>
Querying the Data
Available Endpoints
Search Tweets by Term:

GET /search?term=music
Returns statistics and information about tweets containing the specified term.
#### Example Query:

bash
Copy code
curl http://localhost:8080/search?term=music
Query Results
For a given search term, the API returns:

1. Number of tweets containing the term on each day.
2. Number of unique users who posted tweets with the term.
3. Average likes for tweets containing the term.
4. Locations (place IDs) where tweets originated.
5. Times of day when the tweets were posted.
6. The user who posted the most tweets with the term.
7. Testing
8. Run tests using pytest to ensure that data ingestion and queries work correctly:

bash
Copy code
pytest tests/
  
#### Usage Instructions
Clone the repository and follow the installation steps.
Use the provided endpoints to query the data.
Refer to the Dockerfile and docker-compose.yml for setting up the environment.
#### Conclusion
This project demonstrates the ability to ingest and query large datasets, with an emphasis on code quality, documentation, and performance. For any questions, please contact me at koushik.sama9@gmail.com with [IDI TAKE-HOME] in the subject line.

Feel free to customize the README file to match your project specifics, such as file names or additional instructions.
