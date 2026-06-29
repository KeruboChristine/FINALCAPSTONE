# Research Proposal

## Title

**Forecasting Food Security Trends in Kenya Using Historical Integrated Food Security Phase Classification (IPC) Data: A Comparative Study of Statistical, Machine Learning and Deep Learning Models**

## 1. Background

Food insecurity remains one of the most pressing humanitarian and socioeconomic challenges in Kenya. The country frequently experiences droughts, erratic rainfall, conflicts, economic shocks, and other factors that significantly affect household food security, particularly within the arid and semi-arid lands (ASALs). Timely forecasting of food security conditions is therefore essential for governments, humanitarian organizations, and policymakers to implement early interventions, allocate resources efficiently, and minimize the impact of food crises.

The Integrated Food Security Phase Classification (IPC) is an internationally recognized analytical framework used to assess and classify the severity of food insecurity. The IPC categorizes food security conditions into five phases ranging from Minimal (Phase 1) to Famine (Phase 5), enabling consistent monitoring and comparison of food security conditions across regions and over time.

Recent advances in artificial intelligence have demonstrated that machine learning and deep learning techniques can identify complex temporal patterns within historical data. Statistical forecasting models such as AutoRegressive Integrated Moving Average (ARIMA) remain widely used because of their simplicity and interpretability, while machine learning algorithms such as Random Forest and Extreme Gradient Boosting (XGBoost) capture nonlinear relationships within structured data. Long Short-Term Memory (LSTM) networks, a specialized form of recurrent neural network, have become particularly effective for sequential forecasting because they learn long-term temporal dependencies.

This study proposes a comparative forecasting framework that evaluates statistical, machine learning, and deep learning approaches using historical IPC data to predict future food security conditions in Kenya.

---

# 2. Problem Statement

Food security assessments are generally descriptive and focus on current or past conditions. Although these assessments are essential for understanding ongoing humanitarian situations, they provide limited capability for predicting future food security conditions.

Many previous studies have attempted to forecast food insecurity by integrating multiple datasets such as climate observations, food prices, conflict indicators, and socioeconomic variables. However, combining heterogeneous datasets often introduces challenges related to inconsistent temporal coverage, differing spatial resolutions, missing values, and complex preprocessing requirements.

To address these limitations, this study focuses exclusively on historical IPC data. Since IPC assessments already summarize multiple dimensions of food security through a standardized analytical framework, historical IPC observations contain valuable temporal information that can be exploited for forecasting future food security conditions without requiring additional external datasets.

---

# 3. Aim of the Study

To develop and evaluate statistical, machine learning, and deep learning models for forecasting future food security conditions in Kenya using historical Integrated Food Security Phase Classification (IPC) data.

---

# 4. Objectives

The study aims to:

1. Examine historical food security trends in Kenya using IPC data.
2. Perform comprehensive exploratory data analysis to understand temporal and spatial characteristics of the dataset.
3. Preprocess and prepare the IPC dataset for time-series forecasting.
4. Develop statistical, machine learning, and deep learning forecasting models.
5. Compare the forecasting performance of ARIMA, Random Forest, XGBoost, and LSTM models.
6. Identify the model that provides the most accurate predictions of future food security conditions.

---

# 5. Dataset Description

This study will use the **Kenya Current Situation FEWS NET IPC Classification** dataset obtained from the Humanitarian Data Exchange (HDX). The dataset is published by the Famine Early Warning Systems Network (FEWS NET) and contains historical IPC-compatible food security assessments for Kenya.

The dataset is available through the Humanitarian Data Exchange (HDX) and was downloaded from:

https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_classification/resource/cc36f64d-75ef-4f7b-b644-8983873932b8

The dataset contains historical food security observations collected over approximately fifteen years and includes repeated assessments for multiple geographic analysis units across Kenya.

### Dataset Characteristics

* Number of observations (rows): **27,694**
* Number of variables (columns): **42**
* Time coverage: **2011–2026**
* Number of unique geographic units: **593**
* Geographic unit types:

  * Administrative units
  * Administrative livelihood zones
  * Internally Displaced Persons (IDP) camps
* Data frequency: Repeated IPC assessment periods conducted over time

The dataset contains variables describing:

* Projection start and end dates
* Geographic identifiers
* Administrative analysis units
* IPC classifications
* Classification metadata
* Assessment information

The fifteen-year temporal coverage provides sufficient historical observations for learning long-term temporal patterns, making the dataset appropriate for time-series forecasting.

---

# 6. Research Methodology

The proposed methodology consists of seven phases.

## Phase 1: Data Understanding

The first stage will involve understanding the dataset by examining:

* Dataset dimensions
* Variable descriptions
* Data types
* Missing values
* Duplicate observations
* Geographic structure
* Time coverage
* Distribution of IPC observations

This phase will establish a clear understanding of the dataset before preprocessing begins.

---

## Phase 2: Data Preprocessing

The preprocessing stage will include:

* Removing duplicate observations
* Handling missing values
* Converting date variables into appropriate datetime formats
* Sorting observations chronologically
* Standardizing categorical variables
* Selecting relevant variables
* Organizing data into time-series format

The cleaned dataset will then be prepared for forecasting.

---

## Phase 3: Exploratory Data Analysis

Exploratory data analysis will be conducted to investigate:

* Historical food security trends
* Distribution of IPC classifications
* Seasonal patterns
* Geographic variation
* Frequency of assessments
* Data completeness
* Temporal changes in food security

Appropriate statistical summaries and visualizations will be produced to better understand the data.

---

## Phase 4: Feature Engineering

To improve forecasting performance, temporal features will be generated from historical observations, including:

* Lagged observations
* Rolling averages
* Rolling minimum values
* Rolling maximum values
* Time-based variables such as year, month, quarter, and assessment period

These engineered features will enable machine learning models to capture historical dependencies within the data.

---

## Phase 5: Model Development

Four forecasting models will be developed and compared.

### AutoRegressive Integrated Moving Average (ARIMA)

ARIMA will serve as the classical statistical forecasting model. It will establish a benchmark by modeling temporal relationships within historical IPC observations.

### Random Forest

Random Forest will be used as a machine learning model capable of learning nonlinear relationships while providing robustness against overfitting.

### Extreme Gradient Boosting (XGBoost)

XGBoost will be implemented because of its strong predictive performance on structured datasets and its ability to model complex nonlinear interactions.

### Long Short-Term Memory (LSTM)

LSTM will serve as the primary deep learning model. Unlike conventional forecasting models, LSTM networks are specifically designed for sequential data and can capture long-term temporal dependencies within historical IPC observations.

---

## Phase 6: Model Evaluation

The forecasting performance of each model will be evaluated using appropriate performance metrics. Depending on the prediction target, these may include:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)
* Accuracy
* Precision
* Recall
* F1-score

The evaluation will compare forecasting accuracy, robustness, and generalization ability across the four models.

---

## Phase 7: Forecasting and Interpretation

The best-performing model will be used to forecast future food security conditions. The forecasting results will be analyzed and interpreted to demonstrate how historical IPC observations can support humanitarian planning, early warning systems, and evidence-based decision-making.

---

# 7. Expected Outcomes

The study is expected to:

* Produce a clean and well-structured IPC dataset suitable for forecasting.
* Identify long-term temporal patterns in Kenya's food security.
* Develop accurate statistical, machine learning, and deep learning forecasting models.
* Compare the strengths and limitations of ARIMA, Random Forest, XGBoost, and LSTM.
* Recommend the most suitable forecasting approach for predicting future food security conditions in Kenya.

---

# 8. Significance of the Study

This study contributes to the growing application of data science in humanitarian and food security research by developing a comprehensive forecasting framework based solely on historical IPC data. Unlike studies that depend on multiple external datasets, this research demonstrates how standardized IPC assessments can be used to forecast future food security conditions using statistical, machine learning, and deep learning techniques.

The findings are expected to support governments, humanitarian agencies, and policymakers by improving early warning capabilities, enhancing preparedness, and informing timely interventions for populations vulnerable to food insecurity.
