Our project deals with a marketing problem in the banking field, which is knowing which customers to target to offer a given banking product. The specific case of credit cards will be the subject that we will analyze today, with the aim of identifying bank customers likely to accept a credit card offer. To answer this problem, we decided to create an algorithm which will allow us to predict the customers corresponding to this offer and likely to accept it. 

Data source:  https://data.world/gautam2510/credit-card-dataset

# Project Objective 

After analyzing the customer data made available to us, we would like to be able to predict customer acceptance behavior using machine learning techniques, segment or classify your customers who are all different on the outside (each customer is unique), into several small groups (we will find customers who have similar or similar behavior or habits and put them in the same group) in order to target the right customers for this offer. We will also look at the role played by two important elements in customer decisions: the type of reward offered with the credit card (in our case Air Miles, Points or Cash Back) and the type of mail used to send the offer. Other elements apart from these two will also be evaluated in detail. 

The goal of this analysis will be to build a logistic regression model to be able to predict the proportion of customers subscribing to a credit card based on the data characteristics studied. But also, to understand the behavior of those who have not accepted the offer-to-offer other products that correspond to them or to improve the characteristics of the product offered. 

By exploring this data, we want to better understand the elements that influence the acceptance of offers to improve future marketing campaigns and increase the satisfaction levels of this banking establishment's customers. 

# Data Description 

This dataset contains the results of a credit card offer campaign carried out by a bank, with the decision that the customers of that bank made: acceptance or refusal. The overview of the structure and format of the data will be presented to you below: 

customer_number (Integer) 

offer_accepted (Boolean) 

Reward (String) 

mailer_type (String) 

income_level (String) 

bank_accounts_open (Integer) 

overdraft_protection (Boolean) 

credit_rating (String) 

credit_cards_held (Integer) 

homes_owned (Integer) 

household_size (Integer) 

own_your_home (Boolean) 

average_balance (Float) 

q1_balance (Integer) 

q2_balance (Integer) 

q3_balance (Integer) 

q4_balance (Integer) 

# Methodology 

Here are the steps I will follow to be able to create and deploy my logistic regression model:  

1- Importing packages 

2- loading data 

2.1- description of all the variables that are in the database 

2.2- Evaluate the quality of the data (Shape of the data, Data type of each attribute, Checking the presence of missing values, 5 points summaries of numerical attributes, Checking the presence of outliers) 

3- Description of the database 

3.1- Univariate analysis of qualitative variables 

3.2- Univariate analysis of quantitative variables 

4- selection of relevant variables 

4.1- Bivariate analysis and selection of qualitative variables 

4.2- Bivariate analysis and selection of quantitative variables 

5- Construction of the model with several approaches 

6- Interpretation of the model 

7- Evaluate the performance of the model and selection of the most efficient model. 

8- Optimize model performance with GridSearchCV or RandomizedSearchCV tools 

9- Find the optimal threshold to decide 

10- Test the model on new data to make sure it all works well 

11- Export model for deployment 

12- Build the application that will allow the use of the model 

13- Create a git repository 

14- Deploy the model 

# Expected Deliverables 

After having trained the data at our disposal, we will set up a logistic regression model capable of predicting whether a bank customer will accept a credit card offer. We will use Streamlit in VScode to deploy the model. 

# Link to my application: https://predictive-analysis-of-acceptance-a-credit-card-offer.streamlit.app/
