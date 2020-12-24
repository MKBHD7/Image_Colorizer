import streamlit as st
import os
import pandas as pd
import re
import urllib

#os.chdir(r'C:\Users\MOHAMMED MUZZAMMIL\Desktop\parking_hack')

db_file="data.db"

if not os.path.exists(db_file):
    urllib.request.urlretrieve("https://drive.google.com/u/0/uc?id=1BoL1yV-mlNUd0wMsdiRXrg98uzFpK2YO&export=download", "data.db")


details="details.csv"    

if not os.path.exists(details):
    urllib.request.urlretrieve("https://drive.google.com/u/0/uc?id=11zTYc2rtFPSvaNX2-nUO32MoU8VwWacx&export=download", "details.csv")

    


import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')
    
    
def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    conn.commit()
    
def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_user():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data


def main():
    
    st.markdown("<h1 style='text-align: center; color: Light gray;'>Welcome to XYZ Society</h1>", unsafe_allow_html=True)
    
    
    menu = ["Login","Signup"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Login":
        
        st.subheader("Login Section")
        
        username = st.sidebar.text_input("User Name")
        
        password = st.sidebar.text_input("Password",type='password')
        
        if st.sidebar.checkbox("Login"):
            create_table()
            result = login_user(username,password)
            if result:
                
                st.success("LOGGEDIN")
            
                task = st.selectbox("Search Details Using",["Vehicle Number","Tower No"])
                
                if task == "Vehicle Number":
                    
                    vehicle_number = st.text_input("Enter Vehicle Number")
                    if st.button("Search"):
                        df = pd.read_csv('details.csv')
                        temp = re.search('\d{% s}'% 4, vehicle_number) 
                        res = (temp.group(0) if temp else '') 
                        for i in df['Vehicle No']:
                            temp2 = re.search('\d{% s}'% 4, i) 
                            res2 = (temp2.group(0) if temp2 else '')
                            if res == res2:
                                df.loc[df['Vehicle No'] == i]
                if task == "Tower No":
                    
                    towerno=st.text_input("Enter Tower No")
                    if st.button("search"):
                        df = pd.read_csv('details.csv')
                        for i in df['Address']:
                            temp_tower = re.search('Tower No {}'.format(towerno),i)
                            res_tower = (temp_tower.group(0) if temp_tower else '')
                            if temp_tower != None:
                                st.write(df.loc[df['Address'] == i])
                  
                            
            else:
                st.warning('Wrong User Id or Password')
            

        
        
    elif choice == "Signup":
        st.subheader("Create New Account")
        
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        
        if st.button("Signup"):
            create_table()
            add_userdata(new_user,new_password)
            st.success("Successfully Created Account")
            st.info("Go  to Login Menu to login")
            
            
    elif choice == "QR":
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("NewPicture.jpg",frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
            
            
        
        
        
        
main()
