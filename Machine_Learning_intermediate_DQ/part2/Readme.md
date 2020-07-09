Part 2 is a Machine Learning Project with Lending Club dataset. It goes through cleaning unused features and create dummy variables for categorical data. 
Then we train a logictic regression and Random Forest to classify whether a borrower defaults on the loan or pays off on time. We attempt to descrease false positive rate (fpr)
because we do not want to invest in someone who defaults in reality (but predicted as a customer who pays on time by our model). So far, our model has a fpr of 9% and true positive rate (tpr)
of 24% (very low).
