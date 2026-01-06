## 📊 Nutrition Data Engineering Pipeline (End-to-End)

An **end-to-end Data Engineering mini-project** designed to track daily nutrition and hydration data, process it using scalable ETL principles, and generate actionable insights through dashboards and rule-based intelligence.

This project demonstrates real-world data engineering concepts using PySpark, Power BI, and Python — built entirely using open-source and free tools.

## 🎯 Project Objectives

Track daily calorie intake, hydration, and nutrition metrics

Design a **Bronze → Silver → Gold data pipeline using PySpark***

Perform data cleaning, transformations, and aggregations

Build Power BI dashboards to visualize trends and adherence

Implement rule-based AI alerts for nutrition and hydration monitoring

Simulate automated health insights similar to production systems

## 🏗️ Architecture Overview

**Bronze Layer**

Raw daily nutrition & water intake data (CSV / JSON)

**Silver Layer**

Cleaned, standardized, and validated datasets

Null handling, type casting, derived columns

**Gold Layer**

Aggregated daily metrics

Analytics-ready tables for visualization and alerts

## 📈 Visualization (Power BI)

Daily calorie consumption trends

Target vs actual calorie comparison

Daily water intake trend with goal reference lines

Insight-focused visuals optimized for storytelling

Dashboards focus on trend analysis and adherence, not cosmetic visuals.

## 🤖 AI / Intelligence Layer (Rule-Based)

A lightweight rule-based intelligence module implemented in Python:

Hydration alert if water intake < 2L

Calorie surplus alert if intake exceeds target

Low-energy alert if calories are significantly below target

Positive reinforcement when metrics are within range

This simulates how business rules or ML-driven alerts can be integrated into data pipelines.

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| **PySpark (JupyterLab)** | ETL processing and data transformations |
| **Power BI Desktop** | Data visualization and analytical dashboards |
| **Python** | Rule-based intelligence and alert logic |
| **Docker** | Local reproducible development environment |
| **GitHub** | Version control and project portfolio |


## 🚀 Future Enhancements

Replace rule-based alerts with ML models

Automate alerts via email or notifications

Schedule pipelines using orchestration tools

Extend to weekly/monthly summary analytics
