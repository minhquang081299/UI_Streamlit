import cv2
import numpy as np
import streamlit as st


st.sidebar

uploaded_file_image = st.file_uploader("Chọn một tệp ảnh", type=["jpg", "png"])
uploaded_file_video = st.file_uploader("Chọn một tệp video", type=["mp4", "mov", "mpeg"])

if uploaded_file_image:
    # Chuyển đổi tệp thành ảnh OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file_image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    # Hiển thị ảnh
    st.image(opencv_image, channels="BGR")
    st.text("export response")


@st.cache(allow_output_mutation=True)
def get_cap(uploaded_file):
    return cv2.VideoCapture(uploaded_file)

if uploaded_file_video:
    while True:
        image = get_cap(uploaded_file_video).read()
        try:
            # Xử lý video ở đây
            image = cv2.resize(image, None, fx=scaling_factorx, fy=scaling_factory, interpolation=cv2.INTER_AREA)
            file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
            image=cv2.imdecode(file_bytes, 1)
            st.video(image)
            # Thực hiện các thao tác khác trên video
        except:
            break

from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# Cấu hình WebRTC
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)



def process_image(frame):
    # Xử lý hình ảnh ở đây (ví dụ: hiển thị hình ảnh, phát hiện khuôn mặt, v.v.)
    processed_frame = frame
    return processed_frame

# Sử dụng hàm process_image trong webrtc_streamer
webrtc_ctx = webrtc_streamer(
    key="WebcamDemo",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=process_image,
    async_processing=True,
)
