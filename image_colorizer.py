import requests
import streamlit as st

st.markdown("<h1 style='text-align: center; color: Light Gray;'>Image Colorizer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Light Gray;'>Color any Black and white image using this AI</h3>", unsafe_allow_html=True)
    
st.set_option('deprecation.showfileUploaderEncoding', False)    


page_bg_img = '''
<style>
body {
background-image: url("https://www.netpremacy.com/wp-content/uploads/2018/09/Background-website-01.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
img_url=st.text_input("Enter the Image Url")

if img_url:
    if st.button('Colorize!'):

        r = requests.post(
            "https://api.deepai.org/api/colorizer",
                data={
                    'image': img_url,
                },
                headers={'api-key': '6d0a5321-5e74-4a0a-80e1-fc6a530846f5'}
        )
        output=r.json()
        url=output['output_url']
        st.image(url)
        st.info("Original Image")
        st.image(img_url)

    
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    if st.button('Colorize'):
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={
                'image': uploaded_file,
            },
            headers={'api-key': '6d0a5321-5e74-4a0a-80e1-fc6a530846f5'}
        )
        output=r.json()
        url=output['output_url']
        st.image(url)
        st.info("Original Image")
        st.image(uploaded_file)
