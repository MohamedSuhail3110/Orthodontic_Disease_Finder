import streamlit as st
import json 
from streamlit_lottie import st_lottie 
from streamlit_option_menu import option_menu
    
st.set_page_config(page_title="Orthodontic Disease Finder", layout="wide")

path = "Animation - 1703740317037.json"
with open(path,"r") as file: 
    url = json.load(file) 

# --- Heading Section ---
st.title("Orthodontic Disease Finder")
st.write("Orthodontics is a dental specialty that focuses on aligning the bite and straightening teeth.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Orthodontics is a dental specialty focused on aligning your bite and straightening your teeth. You might need to see an orthodontist if you have crooked, overlapped, twisted or gapped teeth. Common orthodontic treatments include traditional braces, clear aligners and removable retainers.
            
            - Orthodontics is the branch of dentistry that focuses on diagnosing and treating “bad bites” (malocclusion). Common orthodontic treatments include braces, clear aligners and retainers.
            
            - In most cases, orthodontists perform this type of treatment. An orthodontist is a doctor who receives two to three years of additional training after graduating from dental school. They focus on improving your bite. They don't perform general dentistry treatments like fillings, crowns or bridges.
            
            - According to the American Association of Orthodontists, children should have their first orthodontic visit no later than the age of 7. While many children won't need treatment at this age, it's a good time to find out if there are any issues to watch out for. Often, children who need early orthodontic treatment can reduce their need for extensive dental procedures in the future.
            
            - Almost everyone can gain some benefit from orthodontics. But some people need treatment more than others. Many people seek orthodontic treatment because they want to improve the appearance of their smile. But in addition to cosmetic benefits, orthodontics offers improved chewing function and better oral health.
            """
        )
        

        
    with right_column:
        st_lottie(url, 
            reverse=True, 
            height=550, 
            width=550, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='Car'
        )