# Lending automation for LendingClub

This repository contains the data wrangling and exploratory analysis of the LendingClubs accepted and rejected datasets. Also there are three files for models that are build to complete the plan presented below. There is a separate python file for custom made functions that are used in the notebooks.

## Summary

The LendingClub company wants to automate their lending decisions fully and hired me to lead this project. In this project I am using somewhat clean dataset that is kept in a public bucket. In addition, I have proposed a three-step plan on how to approach this problem.  
- The first step is to create a machine learning model to classify loans into accepted/rejected.  
- The second step is to predict the grade for the loan.  
- The third step is to predict the subgrade and the interest rate.  

## Deployed models

- Application classification model with an accuracy of 98% and F1 score of 88 [HERE](https://loan-application-service-etzmwl27qq-lm.a.run.app/docs)
- Grade prediction model with an accuracy of 83% 
- Subgrade prediction model with an accuracy of 33%
- Interest rate prediction model with an accuracy of 99%