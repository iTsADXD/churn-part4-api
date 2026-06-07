# Churn Scoring API

A FastAPI-based machine learning API for customer churn scoring. The service exposes a health-check endpoint, a single-record prediction endpoint, and a batch prediction endpoint.[cite:3][cite:77]

## Model and Source Data Notes

This API uses a pre-trained churn prediction model stored in `model.pkl`. The model artifact was generated during the earlier modeling stage of the project and is loaded by the FastAPI app at runtime for inference. The training/source datasets used during development are not required to run this API, because predictions are served directly from the saved model file.

## Project Structure

```text
churn-part4-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_api.py
├── model.pkl
├── monitoring_plan.md
├── README.md
└── requirements.txt
```

This repository is organized for Part 4 submission and contains the FastAPI app, tests, dependency file, monitoring plan, and trained model artifact.[cite:4][cite:3]

## Features

- `GET /health` returns a simple status response to confirm the API is running.[cite:77]
- `POST /predict` scores one customer record and returns churn probability, predicted class, and risk level.[cite:3][cite:77]
- `POST /batch_predict` scores multiple customer records in a single request.[cite:3][cite:76]
- Swagger UI is available through FastAPI docs for interactive testing in the browser.[cite:77][web:47]

## Installation

1. Clone the repository.
2. Open the project folder in VS Code or a terminal.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the API server:

```bash
python -m uvicorn app.main:app --reload
```

FastAPI serves interactive API documentation at `http://127.0.0.1:8000/docs` by default.[web:47]

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Check whether the API is running.[cite:77] |
| POST | `/predict` | Predict churn for one customer record.[cite:3] |
| POST | `/batch_predict` | Predict churn for multiple customer records.[cite:3] |

## Sample Request

### Single Prediction

```json
{
  "recencydays": 10,
  "frequency180d": 5,
  "monetary180d": 200.0,
  "sessions30d": 3,
  "lastvisitdaysago": 2
}
```

### Sample Response

```json
{
  "churn_probability": 0.29,
  "predicted_class": 0,
  "risk_level": "low"
}
```

The live API testing screenshots showed successful 200 responses for `/predict`, `/batch_predict`, and `/health` during validation.[file:107][file:102][file:124]

## Running Tests

Run the automated tests with:

```bash
python -m pytest
```

The current test suite checks `/health`, `/predict`, and `/batch_predict` responses.[file:92][cite:3]

## Monitoring

Operational and responsible-use notes are documented in `monitoring_plan.md` as part of the Part 4 deliverables.[cite:3]

## Tech Stack

- FastAPI
- Uvicorn
- scikit-learn
- Pydantic
- pytest

These dependencies align with the current API implementation and test workflow.[web:126][web:37]
