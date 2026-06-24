# Telco Customer Churn MLOps

## Business Problem

A telecommunications company wants to identify customers who are likely
to stop using its services so that the retention team can intervene before
the customers leave.

## Machine-Learning Objective

Build a supervised binary-classification system that predicts whether an
individual customer will churn.

## Prediction Unit

One customer record.

## Target Variable

`Churn`

- `Yes`: the customer churned
- `No`: the customer did not churn

The positive class is `Yes`.

## Dataset

The raw dataset contains 7,043 customer records and 21 columns.

The untouched source file is stored locally at:

`data/raw/Telco-Customer-Churn.csv`

## Initial Quality Observations

- Every customer ID is unique.
- There are no exact duplicate customer records.
- `TotalCharges` is stored as text.
- `TotalCharges` contains 11 whitespace-only values.
- The target is imbalanced, with fewer churned customers than
  non-churned customers.

## Leakage Policy

- The raw dataset will remain unchanged.
- Basic schema validation may examine the complete raw dataset.
- The data will be split before detailed EDA.
- Detailed EDA will use the training dataset only.
- Preprocessing will be fitted using the training dataset only.
- The test dataset will remain untouched until final model evaluation.

## Evaluation

The project will monitor:

- Recall for churned customers
- Precision for churned customers
- F1 score
- ROC-AUC
- Precision-recall AUC
- Confusion matrix

The final primary metric and prediction threshold will be selected after
considering the business cost of missed churners and unnecessary retention
interventions.