You are supporting a hotel with a project aimed to increase revenue from their room bookings. 
  
They believe that they can use data science to help them reduce the number of cancellations.  
  
This is where you come in! They have asked you to use any appropriate methodology to   
identify what contributes to whether a booking will be fulfilled or cancelled.   

They intend to use the results of your work to reduce the chance someone cancels their booking.   
  
Our goal is to determine which features or variables are most influential in causing customers to cancel their bookings. In addition, we constructed two machine learning models for classification to predict when a customer will cancel. Specifically, we were interested in constructing the models using Extreme Gradient Boosting (XGBoost) with cross-validation and a neural network with tensorflow.

We divided our work into three phases:

*    Importing and cleaning the data
*    Conducting exploratory data analysis
*    Building the machine learning models: XGBoost with cross-validation and a Neural network with TensorFlow.

For the XGBoost model, we achieved an accuracy of 89% and an AUC score of 0.95 on a test set. For the neural network, we obtained an accuracy of 87% and an AUC score of 0.92.    
We create a streamlit.py script for a web deployment of our model and results.
