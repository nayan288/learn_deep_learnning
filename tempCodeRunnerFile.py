d.DataFrame({'Actual': Ytest, 'Predicted': predictedYtest.flatten()})
# newdata.to_csv("predicted_results.csv", index=False)    