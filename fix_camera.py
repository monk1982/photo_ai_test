import streamlit as st
import cv2 as cv

def main():
    st.set_page_config(page_title="Streamlit WebCam App")
    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")    
    my_container = st.container(border=True)
    with my_container:
        cap = cv.VideoCapture(0)
        frame_placeholder = st.empty()           
        stop_button_pressed = st.button("Stop")    
        while cap.isOpened() and not stop_button_pressed:
            ret, frame = cap.read()
            if not ret:
                st.write("Video Capture Ended")
                break
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame_placeholder.image(frame,channels="RGB")        
            if cv.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                break
        cap.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()
