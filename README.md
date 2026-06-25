After reviewing your README and the work you've actually completed, I would make some major changes.

Your project has evolved from a broad "Food Security Intelligence Platform" into a much stronger and more focused **County-Level Food Security Forecasting System for Kenya** using real IPC food security data, market prices, rainfall, SQL integration, and forecasting models.

Most importantly:

* You are **not building a Food Security Index anymore**.
* Your target variable is already available: **IPC3plus Population**.
* You removed agricultural production due to severe data alignment issues.
* You removed poverty data because it was regional while the rest of your analysis is county-level.
* You are working with **four pillars of food security conceptually**, but forecasting food insecurity using the strongest available indicators.

---

# KENYA FOOD SECURITY FORECASTING SYSTEM

## A County-Level Multivariate Time Series Forecasting Approach Using IPC Food Security, Food Prices, and Rainfall Data

---

# 1. EXECUTIVE SUMMARY

Food insecurity remains a persistent challenge in Kenya, particularly within arid and semi-arid regions where climatic shocks, market disruptions, and economic pressures affect household access to food.

This project develops a county-level Food Security Forecasting System that integrates food security assessments, staple food prices, and rainfall indicators into a unified forecasting framework.

The study uses Integrated Food Security Phase Classification (IPC) data as the target measure of food insecurity and combines it with maize prices, bean prices, rainfall, and rainfall anomalies to forecast future food security conditions.

The project demonstrates the complete data science workflow including:

* Data collection
* SQL database development
* Data integration
* Exploratory analysis
* Feature engineering
* Statistical forecasting
* Machine learning
* Deep learning

---

# 2. PROBLEM STATEMENT

Food insecurity assessments are often produced after food crises have already developed.

Government agencies, humanitarian organizations, and policymakers require tools capable of forecasting future food insecurity conditions before crises emerge.

Kenya experiences recurring food insecurity due to:

* Drought
* Rainfall variability
* Rising food prices
* Market shocks
* Climate change

Current assessments provide valuable monitoring information but limited predictive capability.

There is a need for a forecasting framework capable of predicting future food insecurity levels using historical food security, climate, and market data.

---

# 3. PROJECT GOAL

To develop a county-level food security forecasting system capable of predicting future food insecurity conditions in Kenya using multivariate time-series, machine learning, and deep learning models.

---

# 4. SPECIFIC OBJECTIVES

### Objective 1

Develop a centralized SQL database containing food security, rainfall, and market price data.

### Objective 2

Analyze spatial and temporal patterns of food insecurity across Kenyan counties.

### Objective 3

Identify relationships between food insecurity, rainfall conditions, and staple food prices.

### Objective 4

Develop predictive models capable of forecasting future food insecurity levels.

### Objective 5

Compare classical statistical models, machine learning models, and deep learning models.

### Objective 6

Identify the most important drivers of food insecurity in Kenya.

---

# 5. UNDERSTANDING FOOD SECURITY

Food security exists when people have reliable access to sufficient, safe, and nutritious food.

The study is guided by the four internationally recognized pillars of food security.

---

## 5.1 Food Availability

Food availability refers to the physical presence of food within a region.

Examples:

* Agricultural production
* Food imports
* Market supply

Although production data was explored during preliminary analysis, inconsistencies across data sources led to its exclusion from the forecasting framework.

Food availability is indirectly represented through food security assessments and market conditions.

---

## 5.2 Food Access

Food access refers to the ability of individuals and households to obtain food.

Indicators used:

* IPC Phase Classification
* IPC3+ Population

Food access is directly reflected through the number of people experiencing food insecurity.

---

## 5.3 Food Affordability

Food affordability measures whether households can financially access food.

Indicators used:

* Maize Price
* Bean Price

Maize and beans were selected because they are among Kenya's most widely consumed staple foods.

Changes in staple food prices often precede worsening food security conditions.

---

## 5.4 Food Stability

Food stability measures the consistency of food availability and access over time.

Indicators used:

* Rainfall
* Rainfall Anomaly

Rainfall variability is a major determinant of food security in Kenya, particularly within ASAL counties.

Rainfall anomalies help identify periods of drought or unusually wet conditions.

---

# 6. STUDY AREA

The analysis focuses on Kenyan counties with sufficient overlap across:

* IPC Food Security Assessments
* Market Price Data
* Rainfall Data

Counties with insufficient observations were excluded to ensure robust forecasting.

Final dataset:

```text
23 Counties
2021–2026
Approximately 500 observations
```

---

# 7. DATA SOURCES

## Food Security Data

Source:

World Food Programme

Variables:

* IPC3plus Population
* IPC3plus Fraction

---

## Market Price Data

Source:

World Food Programme

Variables:

* Maize Price
* Bean Price

---

## Climate Data

Source:

World Food Programme

Variables:

* Rainfall
* Rainfall Anomaly

---

# 8. DATABASE DEVELOPMENT

A SQLite database was developed to store:

```text
Food Security Data
Market Price Data
Rainfall Data
Merged Dataset
```

Database Workflow:

```text
Raw Datasets
       ↓
SQLite Database
       ↓
Data Cleaning
       ↓
Data Integration
       ↓
Forecasting Dataset
```

---

# 9. TARGET VARIABLE

## Primary Target

### IPC3plus Population

Definition:

Number of people classified in IPC Phase 3 or higher.

These phases represent:

* Crisis
* Emergency
* Catastrophe

Higher values indicate worsening food insecurity.

---

# 10. FEATURE VARIABLES

## Food Security Features

* IPC3plus Fraction

## Market Features

* Maize Price
* Bean Price

## Climate Features

* Rainfall
* Rainfall Anomaly

## Time-Series Features

* Lag1
* Lag2
* Lag4
* Rolling2
* Rolling4
* Month_Sin
* Month_Cos

---

# 11. METHODOLOGY

### Phase 1: Data Collection

Collect food security, market price, and rainfall data.

### Phase 2: SQL Integration

Store datasets in SQLite.

### Phase 3: Data Cleaning

* Standardize county names
* Convert dates
* Handle missing values
* Remove duplicates

### Phase 4: Data Integration

Merge datasets using:

```text
County
Month
```

### Phase 5: Feature Engineering

Generate:

* Lag Features
* Rolling Statistics
* Seasonal Features

### Phase 6: Exploratory Data Analysis

Investigate:

* Trends
* Seasonality
* Correlations
* County-level patterns

### Phase 7: Forecasting

Develop and compare forecasting models.

---

# 12. FORECASTING MODELS

## 12.1 Naive Forecast

Purpose:

Benchmark model.

Method:

Future food insecurity is assumed to be equal to the most recent observation.

Why:

Provides the minimum performance threshold all other models must beat.

---

## 12.2 SARIMAX

Purpose:

Classical multivariate time-series forecasting.

Inputs:

* Maize Price
* Bean Price
* Rainfall
* Rainfall Anomaly

How it works:

SARIMAX extends ARIMA by incorporating external variables that influence food insecurity.

Why:

Provides interpretable statistical relationships between food security and its drivers.

---

## 12.3 XGBoost

Purpose:

Machine learning forecasting.

Inputs:

* Prices
* Rainfall
* Lag Features
* Rolling Features
* Seasonal Features

How it works:

Builds sequential decision trees that learn complex nonlinear relationships.

Why:

Often performs exceptionally well on tabular forecasting data.

Expected Outcome:

Likely strongest performer in this study.

---

## 12.4 Long Short-Term Memory (LSTM)

Purpose:

Deep learning forecasting.

Inputs:

Sequential historical observations.

How it works:

Uses memory cells to learn long-term temporal patterns.

Why:

Food insecurity is influenced by cumulative climatic and economic conditions over time.

---

# 13. MODEL EVALUATION

Models will be compared using:

### MAE

Mean Absolute Error

### RMSE

Root Mean Squared Error

### MAPE

Mean Absolute Percentage Error

### R²

Coefficient of Determination

---

# 14. EXPECTED DELIVERABLES

* SQLite Database
* Clean Integrated Dataset
* Exploratory Analysis Report
* Forecasting Models
* Model Comparison Report
* Tableau Dashboard
* GitHub Repository
* Final Research Report


