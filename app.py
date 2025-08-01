import streamlit as st
from streamlit import session_state as ss

# Define a session variable to store the state of the checkbox
# and assign it to the value parameter of the said checkbox.
if 'cam_on' not in ss:
    ss.cam_on = False

def main():
    pages = {
        "Chụp Ảnh": [
            st.Page("gemini_ai.py", title="Đặt câu hỏi cho bức ảnh của bạn"),           
        ],
        "Fix Camera": [
            st.Page("fix_camera.py", title="Thử nghiệm code"),            
        ],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    main()
