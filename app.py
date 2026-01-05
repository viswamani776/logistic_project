import streamlit as st
import pickle

model = pickle.load(open("titanic_model.pkl","rb"))

st.title("🚢 Titanic Survival Prediction")

P = st.number_input("Passenger Class (1–3)",1,3)
S = st.selectbox("Sex",["male","female"])
A = st.number_input("Age",1,100)

S = 0 if S=="male" else 1

if st.button("Predict"):
    pred = model.predict([[P,S,A]])[0]
    st.success("Survived" if pred==1 else "Did Not Survive")
