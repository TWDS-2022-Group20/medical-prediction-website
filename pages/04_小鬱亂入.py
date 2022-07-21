import os

import streamlit as st
from PIL import Image

from utils import st_website_setting

st_website_setting(page_title="小鬱亂入")
st.title("小鬱亂入")
st.write(
    """
         小鬱亂入是2015年由台科大設計系學生白琳與妤恒製作的畢業專題。以插畫的方式讓人了解憂鬱症。
         此外，他們也與專業醫師進行討論，最後製作了小鬱亂入的網站。如果你想要了解更多關於憂鬱症的資訊，歡迎參考小鬱亂入。
         """
)

st.markdown(
    """
            小鬱亂入: https://depressytrouble.tw/
            """
)

landing_img = Image.open(os.path.dirname(__file__) + "/depressytrouble/landing.jpeg")
st.image(landing_img, caption="")

