import streamlit as st
import pandas as pd
import joblib

model = joblib.load('svm.pkl')
label_encoders = joblib.load('label_encoders.pkl')

st.set_page_config(page_title="Food Genie", page_icon="💫", layout="wide")

st.markdown("""
    <style>
        h1, h2, h3 {
            color: #d92344;
        }
        .stButton>button {
            width: 100% !important;
            height: 50px !important;
            font-size: 16px !important;
            border-radius: 10px !important;
            margin-bottom: 10px;     
        }
    </style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "input_data" not in st.session_state:
    st.session_state.input_data = None

st.sidebar.title("📋🍴 Dish Directory")
if st.sidebar.button("🔦 Spotlight"):
    st.session_state.page = "Home"
if st.sidebar.button("🍲🔍 Dish Decoder"):
    st.session_state.page = "Input"
if st.sidebar.button("😋🔓 Craving Cracked"):
    st.session_state.page = "Result"
if st.sidebar.button("📖✨ Our Story"):
    st.session_state.page = "About"

if st.session_state.page == "Home":
    st.title("🍽️ Welcome to Your Personalized Food Genie!")
    st.markdown("Feeling hungry but unsure what to eat? Here is Your personal Genie for satisfying cravings!")
    st.write("Let your cravings and mood do the talking — we’ll find the perfect dish for you.")

    st.title("🔍 What This App Does")
    st.markdown("This intelligent food recommendation system helps you:")
    st.write(""" 
             - Discover delicious dishes tailored to your current cravings
             - Match your mood and cuisine preferences with the right food
             - Get inspired with new and exciting meal ideas instantly
             """)

    st.title("✨ How It Works")
    st.markdown("""
                1. Choose your craving – Are you in the mood for something spicy, sweet, or crunchy?
                2. Pick a cuisine – Indian, Korean, Italian, or something global?
                3. Tell us your mood – Happy, relaxed, tired, or just bored?
                4. Get a suggestion – Our trained ML model recommends the ideal dish!
                """)

    st.title("🎯 Why You’ll Love It")
    st.markdown("""
                - 🧠 AI-powered recommendations trained on real food & mood data
                - 🌎 Diverse dish suggestions from different cultures
                - 😋 Helps you explore new foods or rediscover your favorites
                """)

    st.title("🚀 How to Get Started")
    st.markdown("""
                Head over to the 🍲🔍 Dish Decoder section and tell us what you’re craving.
                We’ll serve you a mouth-watering dish in no time!
                """)

    if st.button("Next ➡️"):
        st.session_state.page = "Input"

elif st.session_state.page == "Input":
    st.title("📝 Tell Us What You're Craving")

    craving = st.selectbox("😋 What are you craving for?", 
                           ["Sweet", "Salty", "Cold", "Sour", "Comfort", "Spicy", "Crunchy", "Warm", "Savory"])
    st.write("Your selected the choice is :",craving)
    cuisine = st.selectbox("🍜 What cuisine are you in the mood for?", 
                           ["Indian", "Western", "Mexican", "American", "Japanese", "Italian", "Korean", "Various"])
    st.write("Your selected the choice is :",cuisine)
    mood = st.selectbox("😊 How are you feeling today?", 
                        ["Comfort", "Movie Mood", "Tired/Hot Day", "Fun/Playful", "Sick/Relaxed", "Low Mood",
                         "Snack Craving", "Energetic", "Rainy Day", "Adventurous", "Sad/Comfort", "Celebration", 
                         "Stress Relief", "Cozy/Winter", "Appetite Boost", "Happy/Chill", "Excited", 
                         "Relaxed", "Stressed", "Happy", "Bored"])
    st.write("Your selected the choice is :",mood)
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.page = "Home"
    with col2:
        if st.button("➡️ Next"):
            st.warning("Please click 'Get My Dish' to see results.")
    with col3:
        if st.button("🎯 Get My Dish"):
            st.session_state.input_data = {
                "Craving Type": craving,
                "Cuisine": cuisine,
                "Mood Associated": mood
            }
            st.session_state.page = "Result"

elif st.session_state.page == "Result":
    st.title("🧞‍🪄🍽️ A Dish Chosen by the Genie")

    if not st.session_state.input_data:
        st.warning("⚠️ Please use the '🍲🔍 Dish Decoder' so the Genie can do its magic.")
    else:
        try:
            input_data = st.session_state.input_data
            encoded = [label_encoders[col].transform([input_data[col]])[0] for col in ['Craving Type', 'Cuisine', 'Mood Associated']]
            df = pd.DataFrame([encoded], columns=['Craving Type', 'Cuisine', 'Mood Associated'])
            prediction = model.predict(df)
            recommended_food = label_encoders['Food Name'].inverse_transform(prediction)
            st.success(f"🍱 Based on your mood and cravings, Genie suggests: **{recommended_food[0]}**")
            st.balloons()
        except Exception as e:
            st.error(f"⚠️ Oops! Something went wrong: {e}")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.page = "Input"
    with col2:
        if st.button("➡️ Next"):
            st.session_state.page = "About"

elif st.session_state.page == "About":
    st.title("📖✨ Our Story")
    st.write("""
    Welcome to **Your Personalized Food Genie!** – a project by **Pooja Rajaram** that blends **machine learning** and **culinary curiosity**.
    """)
    st.subheader("🔮 How Our Genie Grants Your Food Wish:")
    st.write("Just tell the Genie three things:")
    st.write("""
            - ✨ Your Mood
            - 😋 Your Craving Type
            - 🌍 Your Cuisine Choice
            """)
    st.write("And POOF! 💨")
    st.write("Our magical foodie Genie will reveal the perfect dish — chosen from the wisdom of tasty past data!")

    st.subheader("💻 How We Brought the Genie to Life:")
    st.write(" - 🧪 Brewed with Python + Pandas")
    st.write(" - 🧠 Trained with Scikit-learn")
    st.write(" - 📦 Deployed using Joblib + Streamlit")
    st.write(" - ⚡ Supercharged with Machine Learning Magic!")

    st.subheader("🍽️ Whether you're:")
    st.write("😭 Sad, 🥳 Celebrating, 😐 Bored, or 😠 Stressed —")
    st.write("Let our **Genie** do its magic **One wish, one dish—your perfect plate awaits!** ")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.page = "Result"
    with col2:
        if st.button("🔦 Sportlight"):
            st.session_state.page = "Home"
    st.success("NOTE:This Genie's magic is happens according to the Trained Dataset")
