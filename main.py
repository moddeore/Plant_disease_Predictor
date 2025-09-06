import streamlit as st

import tensorflow as tf
import numpy as np

#tesorflow model prediction
def model_prediction(test_image):
    model=tf.keras.models.load_model('train_model.keras')
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(256, 256))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])#convert the image to a batch
    prediction=model.predict(input_arr)
    result_index=np.argmax(prediction)
    return result_index


#UI/UX

st.sidebar.title("DASHBOARD")
app_mode=st.sidebar.selectbox("Choose Page :) ",["SELECT ONE","HOME","ABOUT","DISEASE PREDICTION"])

st.sidebar.title("📬 Contact Information")
st.sidebar.markdown("""
**Developed by:** Mod Pravinkumar Deore 
- ☎️ Contact No.: ********25
- 📧 Email: [moddeore2006@gmail.com](mailto:moddeore2006@email.com)  
- 💼 LinkedIn: [linkedin.com/in/moddeore](https://www.linkedin.com/in/mod-deore-836504345?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )  
- 🐙 GitHub: [github.com/moddeore](https://github.com/moddeore)  
""")

st.sidebar.markdown("---")  # horizontal line
st.sidebar.markdown(
    "<p style='text-align: center; font-size: 13px;'>© 2025 Plant Disease Prediction System<br>All Rights Reserved</p>", 
    unsafe_allow_html=True
)
#Home Page
if(app_mode=="HOME"):
    st.header("Plant Disease Prediction System")
    image_path="home_image.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown("""    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **DISEASE PREDICTION** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
                """)
    

    #=h1
    ##=h2
    ###=h3

    ##about pade

elif(app_mode=="ABOUT"):
    st.header("ABOUT")
    st.markdown("""
        ###About Dataset
        This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this github repo. This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 33 test images is created later for prediction purpose.        
        
        ###Content\n
            1.For Training Model 70295 Image are Used.\n
            2.For Validation 17572 Image are Study.\n
            3.For Testing 33 Image are Used. \n
                
        
                
                """)
    
elif(app_mode=="DISEASE PREDICTION"):
    st.header("DISEASE PREDICTION")
    test_image=st.file_uploader("Choose An Image",type=["JPG"])
    if (st.button('Show Image')):
        st.image(test_image,use_column_width=True)

    #predict button
    if( st.button("Predict the Disease")):
        with st.spinner("Please Wait......"):
            result_index=model_prediction(test_image)
        #define the class
            class_name=['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
            st.success("Model is Predicting it's a {}".format(class_name[result_index]))


elif(app_mode=="SELECT ONE"):
    

# Page Config
   

# Home Page Content
    st.title("🌿 Plant Disease Prediction System")
    st.subheader("AI-powered plant health detection in under 15 seconds ⚡")

    st.markdown("""
Welcome to the **Plant Disease Prediction System**!  
This tool is designed to help farmers, researchers, and plant lovers detect diseases from leaf images quickly and accurately.  

---

### 📖 How to Use the System:
1️⃣ On the **top-left corner**, click the **menu**  
2️⃣ Select **🧪 Disease Prediction**  
3️⃣ Upload a **clear photo of a plant leaf** in the browser  
4️⃣ Click **👀 Show Image** to confirm your upload  
5️⃣ Finally, click **🔍 Predict Disease** – our AI will analyze your image and return the **disease name within 15 seconds**  

---

✅ This Home Page is only for **instructions**.  
👉 Please go to the **Disease Prediction page** from the sidebar menu to start detecting diseases.
""")

    st.info("Tip: Make sure the photo is clear, focused, and the leaf is visible for best results.")
