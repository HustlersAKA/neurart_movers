# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:34:19 2021

@author: Kumar
"""

import streamlit as st
from PIL import Image
import os
from complete_working_pipeline import run_stylization_pipeline

st.title("NEURART MOVERS")

st.write("""
          fast video stylization by the HUSTLERS
         """)
   
st.sidebar.write("""
                 MEET THE HUSTLERS:
                     \n\n Aman Sami - 19113024 
                     \n\n Aiswarya Santhosh - 19113006
                     \n\n Kumar Selvakumaran - 19113049 
                 """)

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def main():
    
    image_file = None
    video_file = None
    st.subheader("STYLE IMAGE")
    image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
    if image_file is not None:       
 			# st.write(type(image_file))        # to See Details
			# st.write(dir(image_file))         # to See Details
        file_details_image = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
 			# st.write(file_details_image)      # to See Details

        img = load_image(image_file)
        style_image_path = "./style_images/style.jpg"
        if os.path.isfile(style_image_path):   # deleting previously existing style image if present
           os.remove(style_image_path)
        img.save(style_image_path)
        st.image(img,width=400)

    st.subheader("CONTENT VIDEO")
    video_file = st.file_uploader("Upload the video",type=['mp4','avi'])
    if video_file is not None: 
        file_details_video = {"Filename":video_file.name,"FileType":video_file.type,"FileSize":video_file.size}
        st.write(file_details_video)
       
        """downloading the uploaded video as sample_video.mp4"""
        bytes_data = video_file.read()    # 'video_file' is an object of UploadedFile class which is a subclass of BytesIO , it is converted to bytes data in this line
        FILE_OUTPUT = 'sample_video.mp4'  #output path
        if os.path.isfile(FILE_OUTPUT):
            os.remove(FILE_OUTPUT)
        with open(FILE_OUTPUT, "wb") as out_file:  # open for [w]riting as [b]inary  (the bytes data is written as binary using 'wb' mode into a mp4 file)
            out_file.write(bytes_data) 
        st.video(bytes_data)    
                     
    if st.button('Stylize'):
        st.write('styling uploaded video using custom style image')
        status = run_stylization_pipeline()
    else:
        st.write('press above button to stylize')
            

    st.subheader("STYLIZED VIDEO")
    stylized_video_path = './result_videos//HustlersFSS-style-content_frames.mp4'
    video_file = open(stylized_video_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
   

   



if __name__ == '__main__':
	main()


