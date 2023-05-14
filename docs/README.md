# DATA_606 - Capstone Project
- Author : Yashwanth Reddy Gadepally
- Semester : Spring 2023
- Campus ID : FH44254

# Project Title : Credit Card Fraud detection

# Introduction
Credit card fraud is a major issue in the banking and finance sector, as it involves the use of stolen or illegally obtained credit cards for fraudulent activities. The US Federal Trade Commission estimated that the amount of money lost to credit card fraud in the US alone was $8.6 billion in 2018. This highlights the need for effective fraud detection systems to identify and prevent fraudulent transactions. This report will provide a critical evaluation of the fraud detection systems currently in use in banking and finance. The report will assess the current fraud detection systems in terms of their effectiveness, accuracy and scalability, in order to identify areas for improvement.

# Objective
To determine what features are most useful in predicting fraudulent credit card transactions? To identify what machine learning models are best suited for predicting fraudulent credit card transactions. To identify which machine learning model provides the best accuracy in predicting fraudulent credit card transactions.

# Motivation
This issue is important because credit card fraud is a major issue for banks and credit card companies, resulting in billions of dollars in losses each year. Understanding the factors that contribute to fraudulent transactions is key to preventing and minimizing fraud. By analyzing the data, it is possible to identify patterns that can be used to create more effective fraud detection methods and reduce losses.

# Data collection
The data used for this project will be a dataset from the Kaggle platform, which contains credit card transaction information from a bank in Europe. The dataset contains more than 30000 observations, 122 attributes. The target variable is labeled as either 1 for customer with payment issues or difficulties and 0 otherwise. This will be used to illustrate fraud or non-fraud transaction. The data is of poor quality and needs to be cleaned before any analysis is done. The source of data is reliable.

Final useful columns:
- EXT_SOURCE_1
- EXT_SOURCE_2
- EXT_SOURCE_3
- DAYS_BIRTH - Birthday
- DAYS_EMPLOYED - Start date of employment
- DAYS_REGISTRATION - Number of days registered
- DAYS_ID_PUBLISH - ID publised date
- AMT_ANNUITY - Amount credit and debited
- COMMONAREA_AVG - Difference of annuity
- AMT_CREDIT - credited amount

Final dataset provides a comprehensive view of all the information gathered from the data
![dataframe](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/95a9eb0d-ddff-4e55-a50e-8c046ffd885a)

# Exploratory Data Analysis

- A histogram of the AMT_CREDIT variable in the dataset using the hist function from the matplotlib library. The histogram is created with 20 bins and black edges around each bin. The title function is used to add a title to the plot. The resulting histogram is displayed using the show function.

![amount_credit](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/561404da-fd69-4dcd-8eef-0bdca55ca2eb)

An overview of how credit crad fraud transactions taking change over the years can be shown in the below picture

![overview](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/ae297a01-066c-40f5-8088-6a39b7ecd558)

- Feature importances are taken from the dataset and working on them can give simplified data with much information needed for the detection of credit crad fraud transactions.

![Features](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/139b3ddb-665f-4e92-9074-fbbe0768ba61)

# Machine Learning Models Used:
- Logistic Regression
- Random forest classifier
- Decision Tree Classifier
- K-Nearest Neighbors Classifier
- Support Vector Machine Classifier

### Classification Reports:
![logistic reg](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/5ee5d7c9-619c-488c-8747-9621be938182)

![random forest](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/dd9b2942-e428-44e9-ae25-b8111b19308b)

![DT](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/7db4a019-b8b9-4eb0-a1f1-284515b86a06)

![KNN](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/a9273bf7-a3d2-42d1-ad67-ee1c0e8dad8c)

![SVM](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/89aa762d-e6b2-44d9-b3ce-cc7096dc6faa)

# User interface:

The user interface allows users to input  details for detecting the transaction:

![Home](https://github.com/Yash42ds/Yashwanth_Data606/assets/124218850/18c80bc8-c61c-40a1-a741-2dc12eb93ea2)

# Conclusion:
- Looking at the accuracy scores and classification reports for each model, it appears that the logistic regression, random forest, and support vector machine (SVM) classifiers all have the same accuracy score of 94.54%. These three models correctly predict 1627 out of 1721 observations in the test set.

- However, when looking at the classification reports, we see that these three models have a precision of 0 for the positive class (class 1). This means that these models did not correctly predict any of the positive cases in the test set, indicating that they may not be the best choice for this particular problem.

- The K-Nearest Neighbors (KNN) classifier and the decision tree classifier, on the other hand, have lower accuracy scores of 94.36% and 89.48%, respectively. However, these two models do have a non-zero precision for the positive class in their classification reports. The KNN classifier has a precision of 0.20 and the decision tree classifier has a precision of 0.11.

- Overall, it appears that the Random forest classifier is the best model for this particular problem as it has a non-zero precision for the positive class and a relatively high accuracy score. However, it's important to note that the specific metrics and evaluation criteria may vary depending on the specific problem and domain, so it's always a good idea to consider multiple models and evaluation methods before making a final decision.

# References:
- Some insights which helped in project from kaggle

  https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

- dataset for the credit card fraud transaction detection

  https://www.kaggle.com/datasets/mishra5001/credit-card

- Credit card fraud prevention

  https://www.riskified.com/fraud/credit-card-fraud-prevention/?utm_source=google&utm_medium=cpc&utm_campaign=usaccfraud&utm_id=ccfraud&utm_term=ccraud&utm_content=platform&gad=1&gclid=CjwKCAjwjYKjBhB5EiwAiFdSfspGBG9EWRuOk2EUzV7rC0A_8ysdruzyjmjNrn87rKh3S4L-RGkNbhoCH8EQAvD_BwE
  
# Links:
Presentation link:

https://github.com/Yash42ds/Yashwanth_Data606/blob/main/docs/Capstone.pptx

youtube link:

https://youtu.be/t85eiNB94Bg
