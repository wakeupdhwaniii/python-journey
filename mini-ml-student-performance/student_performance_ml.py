"""
Mini ML Project: Student Performance Analysis & Prediction

Models used:
- Logistic Regression
- Decision Tree
- Random Forest

Concepts:
- Supervised Learning
- Feature Encoding
- Model Comparison
- Bias-Variance Thinking
"""
import pandas as pd

data = {
    "Age": [21, 22, 23, 24, 25, 26, 22, 24, 23, 25],
    "Department": ["CS", "EE", "CS", "EE", "CS", "EE", "EE", "CS", "CS", "EE"],
    "Marks": [85, 78, 90, 70, 88, 65, 75, 92, 80, 72]
}

df = pd.DataFrame(data)
print(df)
df["passed"]= df["Marks"]>=75
print(df)
df_encoded=pd.get_dummies(df, columns=["Department"])
print(df_encoded)
x=df_encoded[["Age","Marks","Department_CS","Department_EE"]]
y=df_encoded["passed"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
#logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
log_model=LogisticRegression()
log_model.fit(x_train,y_train)
log_pred=log_model.predict(x_test)
log_acc=accuracy_score(y_test,log_pred)
print("Logistic Regression Accuracy:", log_acc)
#decision tree
from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier(max_depth=3,random_state=42)
dt_model.fit(x_train,y_train)
dt_pred=dt_model.predict(x_test)
dt_acc=accuracy_score(y_test,dt_pred)
print("Decision Tree Classifier Accuracy:", dt_acc)
#random forest
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(x_train,y_train)
rf_pred=rf_model.predict(x_test)
rf_acc=accuracy_score(y_test,rf_pred)
print("Random Forest Classifier Accuracy:", rf_acc)
#model comparison
results=pd.DataFrame({
    "Model":["Logistic Regression","Decision Tree","Random Forest"],
    "Accuracy":[log_acc,dt_acc,rf_acc]
})
print(results)
