# Part 4 — FastAPI Churn Scoring Service & Reproducible ML Workflow

## Objective

Expose the churn model through a simple FastAPI service for internal CRM or retention use.

## Project Structure

- `app/main.py` — FastAPI app with `/health`, `/predict`, and `/batch_predict`
- `tests/test_api.py` — basic API tests
- `monitoring_plan.md` — post-deployment monitoring and responsible-use notes
- `requirements.txt` — reproducible dependency setup
- `model.pkl` — trained model artifact from Part 3 (place in the repo root)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API

Make sure `model.pkl` is present in the repository root.

```bash
uvicorn app.main:app --reload
```

Open docs at:

- `http://127.0.0.1:8000/docs`

## Endpoints

### `GET /health`
Returns service health and model file status.

### `POST /predict`
Scores one customer payload.

Sample body:

```json
{
  "customer_id": "CUST0001",
  "recency_days": 95,
  "total_orders": 3,
  "total_spend": 2400,
  "avg_discount": 0.28,
  "return_rate": 0.10,
  "ticket_count": 1,
  "sessions_30d": 2,
  "loyalty_tier": "Silver",
  "acquisition_channel": "Paid Search",
  "segment_name": "At Risk"
}
```

### `POST /batch_predict`
Scores multiple customer payloads in one request.

## Notes

- The app expects `model.pkl` from Part 3.
- Prediction output includes churn probability, predicted class, and a short risk explanation.
- Input validation is handled with Pydantic.
