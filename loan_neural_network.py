# import section
import pandas as pd 
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Input
import numpy as np



# data preparation
data = pd.read_csv("data.csv")
x = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]
Xtrain,Xtest, Ytrain,Ytest = train_test_split(x,y,test_size=0.2,random_state=43452)




# model seletion and modification
model = Sequential([Input (shape=(11,)),













Dense(12, input_dim=11, activation='relu'), Dense(8, activation='relu'),Dense(1, activation='sigmoid') ])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(Xtrain, Ytrain, epochs=150,verbose=1)

data = np.array([[1,1,1,2,0,4,3,0,2,0,3]])

predictedYtest = model.predict(data)

print(predictedYtest)



# newdata = pd.DataFrame({'Actual': Ytest, 'Predicted': predictedYtest.flatten()})
# newdata.to_csv("predicted_results.csv", index=False)    