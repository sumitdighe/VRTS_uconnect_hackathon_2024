VRTS_uconnect_hackathon_2024

# Total Cost of Ownership (TCO) Calculator

## Team Information
- Team Name: Team Imposters
- Team Members:
  - Bhargavi Bhende
  - Gitanjali Shinde
- College: JSPM's Rajarshi Shahu College of Engineering, Pune
- Branch: Computer Science & Business Systems

## Introduction
Welcome to the Total Cost of Ownership (TCO) Calculator, a submission for the Vertias UConnect Hackathon. This tool is designed to assist organizations in making informed decisions when comparing on-premises and cloud-based infrastructure costs. TCO encompasses all direct and indirect costs associated with an asset or acquisition over its entire life cycle. Our calculator takes into account server workload, storage, and labor costs, offering insights into the most cost-effective solutions for your specific needs.

## Problem Statement
TCO is a financial metric that estimates and compares the costs of a product or service. Our TCO Calculator model provides a comprehensive analysis, comparing the cost of different cloud vendors and on-premises deployments. It factors in server specifications, storage requirements, and labor costs, alongside network demands, to deliver a detailed total cost of ownership estimation.

## Installation
### For Google Colaboratory : 
To run the TCO Calculator, follow these steps:
1. Ensure to run model.ipynb file so that dataset and trained model will be generated
2. Open the provided TCOFinal.ipynb file in Google Colab or any Jupyter Notebook environment.
3. Execute the notebook cells sequentially to run the TCO calculator. 

### For Website Execution (Flask):
To run the TCO Calculator as a website using Flask, follow these steps:
1. Clone the repository from GitHub.
2. Open the project in Visual Studio Code (VSCode) or any other text editor.
3. Install Flask and any other required dependencies by running `pip install flask`.
4. Navigate to the `FrontendWithFlask` folder.
5. Run the Flask application by executing `python app.py` in the terminal.
6. Access the TCO Calculator website by opening a web browser and entering `http://localhost:5000` in the address bar.
For a visual guide on how to install and use the TCO Calculator, refer to the demo video added in TeamImposters Repository

## Features
### Inputs:
- Server Workload
- Storage Costs
- Labor Costs

### Functions:
- Predict deployment CU
- Currency converter
- Estimate TCO costs

## Methodology
The TCO Calculator utilizes a detailed, object-oriented approach to estimate the total cost of ownership for both cloud and on-premises deployments. It gathers input on server workloads, including operating system, server count, auto-scaling capabilities, and specific workload types, alongside storage and labor costs. This data feeds into functions that calculate server, storage, and labor costs based on whether the deployment is in the cloud or on-premises. For cloud deployments, it further adjusts calculations based on the selected cloud provider (AWS, Azure, GCP).

## Advanced Features
- Global Applicability: capability to provide cost estimates in local currencies, enhancing its utility for international businesses
- Exchange Rate Integration: real-time currency conversion based on current exchange rates
- Deployment CU Prediction: Introducing the feature that uses machine learning model to predict the optimal Compute Units based on input data, aiding in precise resource allocation
- Model Training and Accuracy: Trained an ML model on synthesized dataset with accuracy 96.89%
- Audio and Video Response: Capable of providing audio and video responses to user queries

## Benefits
- Provides a comprehensive comparison between cloud-based and on-premises deployment costs, enabling users to identify the most cost-effective option tailored to their specific needs.
- Offers clear financial insights and highlights operational advantages, directing users towards choices that match their strategic and financial goals.

## Conclusion
The TCO Calculator is designed to answer your queries about TCO costs and guide you on actions related to optimizing TCO. It empowers organizations to make informed decisions regarding infrastructure deployments, ensuring cost-effectiveness and performance optimization.

**Global Applicability. Precise Predictions. Informed Decisions.**
