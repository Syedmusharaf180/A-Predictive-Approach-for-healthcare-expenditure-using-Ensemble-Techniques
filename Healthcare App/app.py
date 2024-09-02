import streamlit as st
import joblib
import math

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;">Healthcare Expenditure</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    model = joblib.load('model_joblib_xgb')
    
    p1 = st.slider("Enter Your Age", 18, 100)
    p2 = st.number_input("Enter Your BMI Value")
    p3 = st.slider("Enter Number of Children", 0, 5)
    s1 = st.selectbox("Sex", ("Male", "Female"))
    p4 = 1 if s1 == "Female" else 0

    p5 = 1 if s1 == "Male" else 0
    
    
    
    
    s2 = st.selectbox("Smoker", ("Yes", "No"))
    p6 = 1 if s2 == "No" else 0

    p7 = 1 if s2 == "Yes" else 0
    
    sm = st.slider("Enter Your Region [1-4]", 1, 4)

    if sm == 1:
        p8 = 1
        p9 = 0
        p10 = 0
        p11 = 0
    elif sm == 2:
        p9 = 1
        p8 = 0
        p10 = 0
        p11 = 0
    elif sm == 3:
        p10 = 1
        p8 = 0
        p9 = 0
        p11 = 0
    else:
        p11 = 1
        p8 = 0
        p9 = 0
        p10 = 0
    
    
   
    
    if st.button('Predict'):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]])
        rounded_prediction = math.ceil(prediction[0])//10
        st.balloons()
        st.success(f' Your Healthcare Expenditure Expected Amount is ${rounded_prediction}')

if __name__ == '__main__':
    main()
