import streamlit as st
import pickle
import numpy as np

# Load the serialized model
def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


best_model_loaded = data['model']
le_reward = data['le_reward']
le_mailerType = data['le_mailerType']
le_incomeLevel = data['le_incomeLevel']
le_overdraftProtection = data['le_overdraftProtection']
le_creditRating = data['le_creditRating']
le_homeOwner = data['le_homeOwner']

def show_predict_page():
    st.title("Machine Learning Model Prediction")
    st.write(" ### Enter the feature values to get a prediction:")
    
    reward = ('Air Miles',
              'Cash Back',
              'Points')
    
    mailType = ('Letter', 
                'Postcard')
    
    incomeLevel = ('High',
                   'Medium',
                   'Low')
    
    overdraftProtection = ('No', 'Yes')
    
    creditRating = ('High',
                    'Medium',
                    'Low')
    
    homeOwner = ('No', 'Yes')
    
    selected_reward = st.selectbox('Mail Type', reward)
    
    selected_mailType = st.selectbox('Mail Type', mailType)
    
    selected_incomeLevel = st.selectbox('Income Level', incomeLevel)
    
    enter_nbrOfBankAccountsOpen = st.number_input('# Bank Accounts Open', min_value=0, step=1, format='%d', value=0)
    
    selected_overdraftProtection = st.selectbox('Overdraft Protection', overdraftProtection)
    
    selected_creditRating = st.selectbox('Credit Rating', creditRating)
    
    enter_nbrOfCreditCardsHeld = st.number_input('# Credit Cards Held', min_value=0, step=1, format='%d', value=0)
    
    enter_nbrOfHomesOwned = st.number_input('# Homes Owned', min_value=0, step=1, format='%d', value=0)
    
    enter_nbrOfHouseholdSize = st.number_input('Household Size', min_value=0, step=1, format='%d', value=0)
    
    selected_homeOwner = st.selectbox('Own your home', homeOwner)

    enter_averageBalance = st.number_input('Average Balance', min_value=0.0, step=0.1)
    
    enter_q1Balance = st.number_input('Q1 Balance', min_value=0.0, step=0.1)
    
    enter_q2Balance = st.number_input('Q2 Balance', min_value=0.0, step=0.1)
    
    enter_q3Balance = st.number_input('Q3 Balance', min_value=0.0, step=0.1)
    
    enter_q4Balance = st.number_input('Q4 Balance', min_value=0.0, step=0.1)
    
    ok = st.button("Predict")
    
    if ok:
        X= np.array([[selected_reward, selected_mailType, selected_incomeLevel, enter_nbrOfBankAccountsOpen, selected_overdraftProtection,
             selected_creditRating, enter_nbrOfCreditCardsHeld, enter_nbrOfHomesOwned, enter_nbrOfHouseholdSize, selected_homeOwner,
             enter_averageBalance, enter_q1Balance, enter_q2Balance, enter_q3Balance, enter_q4Balance]])
        X[:, 0] = le_reward.fit_transform(X[:, 0])
        X[:, 1] = le_mailerType.fit_transform(X[:, 1])
        X[:, 2] = le_incomeLevel.fit_transform(X[:, 2])
        X[:, 4] = le_overdraftProtection.fit_transform(X[:, 4])
        X[:, 5] = le_creditRating.fit_transform(X[:, 5])
        X[:, 9] = le_homeOwner.fit_transform(X[:, 9])
        X = X.astype(float)
        
        prediction = best_model_loaded.predict(X)
        
        if prediction[0] == 0:
            st.subheader("The customer will accept the offer 😊")
        else:
            st.subheader("The customer will not accept the offer 😞")
            
            
            

    
    

