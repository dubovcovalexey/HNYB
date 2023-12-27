import streamlit as st
from streamlit_extras.let_it_rain import rain
from typing import Union
from PIL import Image
import time
from streamlit_player import st_player

import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
     background-image: url("data:image/png;base64,%s");
     background-size: cover;
     }
     </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('PHONE.jpg')
rain(
    emoji="🥳",
    font_size=30,
    falling_speed=5,
    animation_length="infinite",
)



def main(
    emoji: str,
    font_size: int = 30,
    falling_speed: int = 5,
    animation_length: Union[int, str] = "infinite",
):
    """
    Creates a CSS animation where input emoji falls from top to bottom of the screen.
    """

    if isinstance(animation_length, int):
        animation_length = f"{animation_length}"

    st.write(
        f"""
    <style>
    body {{
    background: gray;
    }}
    .emoji {{
    color: #777;
    font-size: {font_size}px;
    font-family: Arial;
    // text-shadow: 0 0 5px #000;
    }}
    ///*delete for no hover-effect*/
    //.emoji:hover {{
    //  font-size: 60px;
    //  text-shadow: 5px 5px 5px white;
    //}}
    @-webkit-keyframes emojis-fall {{
    0% {{
        top: -10%;
    }}
    100% {{
        top: 100%;
    }}
    }}
    @-webkit-keyframes emojis-shake {{
    0% {{
        -webkit-transform: translateX(0px);
        transform: translateX(0px);
    }}
    50% {{
        -webkit-transform: translateX(20px);
        transform: translateX(20px);
    }}
    100% {{
        -webkit-transform: translateX(0px);
        transform: translateX(0px);
    }}
    }}
    @keyframes emojis-fall {{
    0% {{
        top: -10%;
    }}
    100% {{
        top: 100%;
    }}
    }}
    @keyframes emojis-shake {{
    0% {{
        transform: translateX(0px);
    }}
    25% {{
        transform: translateX(15px);
    }}
    50% {{
        transform: translateX(-15px);
    }}
    100% {{
        transform: translateX(0px);
    }}
    }}
    .emoji {{
    position: fixed;
    top: -10%;
    z-index: 99999;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: default;
    -webkit-animation-name: emojis-fall, emojis-shake;
    -webkit-animation-duration: 5s, 3s;
    -webkit-animation-timing-function: linear, ease-in-out;
    -webkit-animation-iteration-count: {animation_length}, {animation_length}; // overall length
    -webkit-animation-play-state: running, running;
    animation-name: emojis-fall, emojis-shake;
    animation-duration: {falling_speed}s, 3s;  // fall speed
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: {animation_length}, {animation_length}; // overall length
    animation-play-state: running, running;
    }}
    .emoji:nth-of-type(0) {{
    left: 1%;
    -webkit-animation-delay: 0s, 0s;
    animation-delay: 0s, 0s;
    }}
    .emoji:nth-of-type(1) {{
    left: 10%;
    -webkit-animation-delay: 1s, 1s;
    animation-delay: 1s, 1s;
    }}
    .emoji:nth-of-type(2) {{
    left: 20%;
    -webkit-animation-delay: 6s, 0.5s;
    animation-delay: 6s, 0.5s;
    }}
    .emoji:nth-of-type(3) {{
    left: 30%;
    -webkit-animation-delay: 4s, 2s;
    animation-delay: 4s, 2s;
    }}
    .emoji:nth-of-type(4) {{
    left: 40%;
    -webkit-animation-delay: 2s, 2s;
    animation-delay: 2s, 2s;
    }}
    .emoji:nth-of-type(5) {{
    left: 50%;
    -webkit-animation-delay: 8s, 3s;
    animation-delay: 8s, 3s;
    }}
    .emoji:nth-of-type(6) {{
    left: 60%;
    -webkit-animation-delay: 6s, 2s;
    animation-delay: 6s, 2s;
    }}
    .emoji:nth-of-type(7) {{
    left: 70%;
    -webkit-animation-delay: 2.5s, 1s;
    animation-delay: 2.5s, 1s;
    }}
    .emoji:nth-of-type(8) {{
    left: 80%;
    -webkit-animation-delay: 1s, 0s;
    animation-delay: 1s, 0s;
    }}
    .emoji:nth-of-type(9) {{
    left: 90%;
    -webkit-animation-delay: 3s, 1.5s;
    animation-delay: 3s, 1.5s;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.write(
        f"""
    <!--get emojis from https://getemoji.com-->
    <div class="emojis">
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
        <div class="emoji">
            {emoji}
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


    #def example():
        #rain(
            #emoji="🎂",
            #font_size=30,
            #falling_speed=5,
            #animation_length="infinite",
        #)
    
    
    
    
    
    
    st.sidebar.title('Happy New Year!')
    photo = st.sidebar.selectbox('Тут все!:',  ['Тут все', 'Паша', 'Юля', 'Лана', 'Лёша', 'Наташа', 'Чубакка'])
    if photo == 'Тут все':
        st.sidebar.image('HB2.jpg')
    if photo == 'Паша':
        st.sidebar.image('1.png')
    if photo == 'Юля':
        st.sidebar.image('2.png')
    if photo == 'Лана':
        st.sidebar.image('3.png')
    if photo == 'Лёша':
        st.sidebar.image('4.png')
    if photo == 'Наташа':
        st.sidebar.image('5.png')
    if photo == 'Чубакка':
        st.sidebar.image('6.png')
   
    
    st.markdown("<h1 style='text-align: center; '>З Новым Годам!</h1>", unsafe_allow_html = True)
    st.markdown("<h1 style='text-align: center; '>Шчасця, здароўя!😁</h1>", unsafe_allow_html = True)

    video_file = open('1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    video_file2 = open('2.mp4', 'rb')
    video_bytes2 = video_file2.read()
    st.video(video_bytes2)
    

    
    if st.button("Нажми кнопку! Если семья для тебя самое главное 👫", key=1):       
        st.balloons()
        st.image('Family.jpg', width=700)
        time.sleep(2.5)



    if st.button("Нажми кнопку! Если что то уже хрустит в спине 😷",  key=4):     
        st.balloons()
        st.image('health.jpg', width=700)
        time.sleep(2.5)


if __name__ == '__main__':
    main(rain)
    
    #<i class="em em-rose" aria-role="presentation" aria-label="ROSE"></i>
