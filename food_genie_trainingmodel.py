import pandas as pd
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
df=pd.read_csv('food_craving_dataset_5000.csv')
print(df)
label_encoders={}
for column in ["Craving Type", "Cuisine", "Mood Associated", "Food Name"]:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le
x=df[['Craving Type','Cuisine','Mood Associated']]
y=df['Food Name']
model=SVC()
model.fit(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
y_pred=model.predict(x_test)
ar=accuracy_score(y_test, y_pred)
print(f"\n The accuracy for the model: {ar*100:.2f}")
con=confusion_matrix(y_test, y_pred)
print("\n The confusion matrix for the model:\n",con)
cl=classification_report(y_test, y_pred,zero_division=1)
print("\n The classification report:\n",cl)
sns.heatmap(con, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

joblib.dump(model,'svm.pkl')
joblib.dump(label_encoders,'label_encoders.pkl')
