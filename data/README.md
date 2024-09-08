# Building a Data Warehouse for Business Analytics

## Overview

This project demonstrates how to build a data warehouse for business analytics using a retail dataset. The dataset includes sales transactions, and the project involves extracting, transforming, and loading (ETL) the data into a structured format suitable for analysis.

## Data Source

The dataset used is the "Online Retail" dataset from the UCI Machine Learning Repository. It contains transaction data from a retail store.

## Project Structure

- `scripts/`: Contains Python scripts for data extraction and transformation.
- `data/`: Contains the resulting dimension and fact tables in CSV format.

## ETL Process

1. **Extraction**: Load the raw dataset and clean it by removing rows with missing `CustomerID`, filling missing `Description` values, and creating a `TotalAmount` column.
2. **Transformation**: 
   - Create dimension tables for `Product`, `Customer`, and `Date`.
   - Create a fact table for `Sales`.
3. **Loading**: Save the cleaned data and dimension tables as CSV files in the `data/` folder.

## Running the Scripts

1. Install the necessary Python packages:
   ```bash
   pip install pandas