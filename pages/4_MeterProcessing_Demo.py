# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import numpy as np
import streamlit as st

st.set_page_config(
  page_title="My YOLO App",
  page_icon="🚀"
)

st.title('My YOLO App')

st.markdown('This is an application for object detection using YOLO')

img_files = st.file_uploader(label="Choose an image files",
                 type=['png', 'jpg', 'jpeg'],
                 accept_multiple_files=True)

for n, img_file_buffer in enumerate(img_files):
  if img_file_buffer is not None:
    # we'll do this later
    # 1) image file buffer will converted to cv2 image
    # 2) pass image to the model to get the detection result
    # 3) show result image using st.image()
    pass

st.markdown("""
  <p style='text-align: center; font-size:16px; margin-top: 32px'>
    CMPE 295A
  </p>
""", unsafe_allow_html=True)


