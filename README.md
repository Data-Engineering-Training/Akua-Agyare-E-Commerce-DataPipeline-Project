# AKUA AGYARE

# ADVANCED E-COMMERCE DATA PIPELINE PROJECT

## TABLE OF CONTENTS
1. Overview of Data Pipeline Solution
2. Description of datasets
3. Requirements
4. Method
   a. Data Extraction
   b. Data Ingestion
   c. Schema evolution
   d. Data transformation
   e. Incremental updates
   f. Scalability and Parallel Processing
   g. Data storage
   h. Fault tolerance
5.  Data pipeline architecture and Data flow
6.  Documentation: Data pipeline initiation and maintenance

## Overview of Data Pipeline Solution-

This repository presents a detailed description of all the processes and tools involved in building an advanced data pipeline to process and store data from an e-commerce platform. As the data engineer assigned to this project, the goal is to design a robust data pipeline that is scalable, fault-tolerant and handles complexities including schema evolution, incremental loading and diverse data formats. Ultimately, the data pipeline designed should effieciently process all data provided from the e-commerce platfrom for analytics purposes. 

## Description of Datasets-

The repository contains three (3) datasets of different formats obtained from two(2) distinct e-commerce market.

### A. Customer Data - Market 1 & 2 (`customers.json`)

the first dataset provides information about user transactions, including Customer ID, Last Used Platform, Is Blocked, Created At, Language, Outstanding Amount, Loyalty Points, Number of employees for each market.

### B. Orders Data - Market 1 & 2 (`order.csv`)

The second dataset contains orders data, including Order ID, Order Status, Category Name, SKU, Customization Group, Customization Option, Quantity, Unit Price, Cost Price, Total Cost Price, Total Price, Order Total, Sub Total, Tax, Delivery, Charge, Tip, Discount, Remaining Balance, Payment Method, Additional Charge, Taxable Amount, Transaction ID, Currency Symbol, Transaction Status, Promo Code, Customer ID, Merchant ID, Description, Distance (in km), Order Time, Pickup Time, Delivery Time, Ratings, Reviews, Merchant Earning, Commission Amount, Commission Payout Status, Order Preparation Time, Debt Amount, Redeemed Loyalty Points, Consumed Loyalty Points, Cancellation Reason, Flat Discount, Checkout Template Name, Checkout Template Value, for each market.

### C. Deliveries Data - Market 1 & 2 (`deliveries.csv`)

the third dataset contains deliveries data, including Task_ID, Order_ID, Relationship, Team_Name, Task_Type, Notes, Agent_ID, Agent_Name, Distance(m), Total_Time_Taken(min), Task_Status, Ref_Images, Rating, Review, Latitude, Longitude, Tags, Promo_Applied, Custom_Template_ID, Task_Details_QTY, Task_Details_AMOUNT, Special_Instructions, Tip, Delivery_Charges, Discount, Subtotal, Payment_Type, Task_Category, Earning, Pricing, for each market.

## Requirements -

### Data Extraction and transformation:
All data from the two markets were extracted from their respective formats using pandas. Each data was read using pandas and various preprocessing and transformation tasks undertaken to prepare the data for ingestion.
The 'ETLfile.py' python script provides the step-by-step processes taken in extracting data from the various sources and transformation processes.

### Data Ingestion:
The `ingestion.py` script demonstrates how to each transformed data is ingest the integrated data into the respective database created. Follow the instructions in the script for your specific requirement.
There are aslo sql files contained in this repository to demonstrate how to run the database schemas.

### Hanadling Schema evolution:
- Handle schema evolution scenarios, where the data schema may change over time.

### Incremental Updates:

- Design the data pipeline to support incremental updates, allowing it to process only new or modified records since the last execution.
- Consider scenarios where the data is continuously updated.

### Data Transformation:

- Implement data transformations to enrich the orders and delivery data with user information.
- Calculate aggregate metrics, such as total transaction amount per user. Bonus points for including as many aggregations as possible suitable for an eCommerce platform.

