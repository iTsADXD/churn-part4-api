# Monitoring Plan

## What should be monitored after deployment

### 1. Data drift
Track whether incoming feature distributions are changing over time. Examples:
- recency_days
- total_orders
- total_spend
- sessions_30d
- return_rate
- ticket_count
- loyalty_tier mix
- acquisition_channel mix

If production traffic starts looking very different from training data, model quality may degrade.

### 2. Prediction distribution
Monitor:
- average churn probability
- share of customers predicted as churners
- score distribution by channel, tier, and segment

A sudden shift may indicate model drift, broken inputs, or business changes.

### 3. Business outcomes
Track whether scored customers actually churn and whether interventions improve retention. Useful measures:
- churn rate in high-risk band
- campaign conversion rate
- saved revenue from interventions
- retention cost per saved customer

### 4. API health
Monitor:
- error rate
- response latency
- failed batch requests
- model file load failures

### 5. Retraining triggers
Retrain if:
- model performance drops materially,
- feature drift becomes persistent,
- churn definition changes,
- customer behavior changes due to seasonality or strategy shifts.

## Responsible use

The API should support human decision-making, not replace it fully.

### Should be used for:
- prioritizing customers for review,
- planning retention outreach,
- identifying likely churn cohorts.

### Should not be used for:
- automatically denying benefits,
- making irreversible customer decisions,
- applying discounts blindly without business context.
