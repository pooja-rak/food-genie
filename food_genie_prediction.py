import joblib
import pandas as pd
import sys
model = joblib.load('svm.pkl')
label_encoders = joblib.load('label_encoders.pkl')
print("Craving type \n 1. Sweet \n 2. Salty \n 3. Cold \n 4. Sour \n 5. Comfort \n 6. Spicy \n 7. Crunchy \n 8. Warm \n 9. Savory")
a = input("Enter your option: ")
if a == "1":
    a_ = "Sweet"
elif a == "2":
    a_ = "Salty"
elif a == "3":
    a_ = "Cold"
elif a == "4":
    a_ = "Sour"
elif a == "5":
    a_ = "Comfort"
elif a == "6":
    a_ = "Spicy"
elif a == "7":
    a_ = "Crunchy"
elif a == "8":
    a_ = "Warm"
elif a == "9":
    a_ = "Savory"
else:
    print("Invalid Choice")
    sys.exit()
print("what kinda cuisine you want to eat \n 1. Indian \n 2. Western \n 3. Mexican \n 4. American \n 5. Japanese \n 6. Italian \n 7. Korean\n 8. Various")
b = input("Enter your Option: ")
if b == "1":
    b_ = "Indian"
elif b == "2":
    b_ = "Western" 
elif b == "3":
    b_ = "Mexican"
elif b == "4":
    b_ = "American"
elif b == "5":
    b_ = "Japanese"
elif b == "6":
    b_ = "Italian"
elif b == "7":
    b_ = "Korean"   
elif b == "8":
    b_ = "Various"   
else:
    print("Invalid Choice")
    sys.exit()
print("whats your current mood? \n 1. Comfort \n 2. Movie Mood \n 3. Tired/Hot Day \n 4. Fun/playful \n 5. Sick/Relaxed \n 6. Low Mood \n 7. Snack Craving \n 8. Energetic \n 9. Rainy Day \n 10. Adventurous \n 11. Sad/comfort \n 12. Celebration \n 13. Stress Relief \n 14. Cozy/Winter \n 15. Appetite Boost \n 16. Happy/Chill \n 17. Excited \n 18. Relaxed \n 19. Stressed \n 20. Happy \n 21. Bored")
c=input("Enter your Mood:")
if c == "1":
    c_="Comfort"
elif c == "2":
    c_="Movie Mood"
elif c == "3":
    c_="Tired/Hot Day"
elif c == "4":
    c_="Fun/Playful"
elif c == "5":
    c_="Sick/Relaxed"
elif c =="6":
    c_ = "Low Mood"
elif c =="7":
    c_ = "Snack Craving"
elif c == "8":
    c_="Energetic"
elif c =="9":
    c_="Rainy Day"
elif c =="10":
    c_="Adventurous"
elif c == "11":
    c_="Sad/Comfort"
elif c == "12":
    c_="Celebration"
elif c == "13":
    c_="Stress Relief"
elif c == "14":
    c_="Cozy/Winter"
elif c == "15":
    c_="Appetite Boost"
elif c =="16":
    c_ = "Happy/Chill"
elif c =="17":
    c_ = "Excited"
elif c == "18":
    c_="Relaxed"
elif c =="19":
    c_="Stressed"
elif c =="20":
    c_="Happy"
elif c =="21":
    c_="Bored"
else:
    print("Invalid Choice")
    sys.exit()
print("\n--- Your Selections ---")
print("Craving:",a_)
print("cuisine:",b_)
print("Mood:",c_)
new = {
    'Craving Type': a_,
    'Cuisine': b_,
    'Mood Associated': c_
}
encoded_input = []
for col in ['Craving Type', 'Cuisine', 'Mood Associated']:
    try:
        val = label_encoders[col].transform([new[col]])[0]
        encoded_input.append(val)
    except ValueError:
        print(f"Invalid value for {col}: {new[col]}")
        exit()
input_df = pd.DataFrame([encoded_input], columns=['Craving Type', 'Cuisine', 'Mood Associated'])
prediction = model.predict(input_df)
food = label_encoders['Food Name'].inverse_transform(prediction)
print("Highly Recommended Food for your preferences is :", food[0])
