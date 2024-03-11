
# Project Title

A brief description of what this project does and who it's for


# Cloud Zenith (TCO Calculator)
[Deployed Model (Click Me)](http://zenithbucket.s3-website.ap-south-1.amazonaws.com/)

- The project's frontend is hosted on AWS S3, while the backend is deployed on AWS EC2 instances. Machine learning algorithms are trained on AWS SageMaker, and their endpoints are accessed within the project via Lambda functions,which deploy REST APIs.

- The AWS setup includes a CodePipeline for complete CI/CD integration.

[Recorded Video (Click Me)](https://youtu.be/jB9jTphWZkw)

Cloud Total Cost of Ownership (TCO) is a comprehensive analysis that evaluates the overall expenses associated with adopting and operating cloud-based services or infrastructure over a specified period.


## Group Members

- Rumman Shaikh
- Abraham Ahmed
- Mohit Lalwani

## Project Overview

This project features a homepage with two input sections. On the left side, users input parameters such as vCPUs, instance memory, budget, and instance storage to determine the most suitable cloud package. Below, users input vmcreated, vmdeleted, vmcorecountbucket, and vmmemorybucket to predict auto-scaling needs.

After entering the desired inputs, the user is presented with available package options from different cloud service providers. Additionally, there's a section displaying the predicted cost and whether auto-scaling is recommended. Below this, a graph illustrates the comparison of on-demand cost values across different configurations.
## Machine Learning Models used 
There are altogether three models used 

1) Cost Prediction (Random Forest):
A Random Forest model was utilized for cost prediction. Users input instance memory and vCPUs, and the model predicts the cost price.


Below is the sample dataset:
[Dataset](https://drive.google.com/file/d/1LIAqHj1_Gssd2sCiOsJXBcxZsR1oBrmq/view?usp=sharing)
| Attribute          | Value            |
| ------------------ | ---------------- |
| Instance Memory          | 0.5 GiB          |
| vcpus          | 1 vCPUs          |
| On demand  | $0.0052 hourly   |

2) AutoScaling Prediction (Xgboost):
An XGBoost model was employed for auto-scaling prediction based on various attributes.

Below is the sample dataset:
[Dataset](https://drive.google.com/drive/folders/1_tp9LqyovxzFmzSqypItUu0JaaOX7O0V?usp=sharing)
| Attribute          | Value            |
| ------------------ | ---------------- |
| vmcreated          | 558300         |
| vmdeleted          | 1673700          |
| vmcorecountbucket  | 8   |
|vmmemorybucket|32|

## Deployment

To setup the vite react frontend project locally. Change directory into the frontend folder and run

```bash
  npm install
```
To start the frontend of the project run

```bash
  npm run dev
```

To setup the django backend project locally. Change directory into the MainProject folder and run

```bash
  pip install -r requirements.txt
```
To start the backend of the project run

```bash
  python manage.py runserver
```
To test the connectivity locally navigate to src/components/Dashboard.jsx of frontend and change to localhost:8000

```bash
  const response = await
            axios.post('http://localhost:8000/MainApp/sample/',
                {
            instance_memory: instance_memory,
            vcpus: vcpus,
            avgcpu_usage: avgcpu_usage,
            vmmemorybucket: vmmemorybucket,
            bucket: bucket,
            vmcreated: vmcreated,
            vmdeleted: vmdeleted,
            vmcorecountbucket: vmcorecountbucket
        });
```
To interact with the calculator fill the fields and click on Calculate to get the output and click again to compare with other specifications.
