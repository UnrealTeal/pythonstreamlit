import streamlit as st
import pandas as pd
import plotly.express as px
import webbrowser

st.set_page_config(page_title="Video Hub", page_icon= "📻")
menu = st.sidebar.selectbox("Menu",["Video Categories","Video Ratings"])
csvlink = "videoclicks.csv"

try:
    videocsv = pd.read_csv(csvlink)
except:
    videocsv = pd.DataFrame()
    videocsv.to_csv(csvlink, index=False)

if menu == "Video Ratings":
    st.subheader("Video Ratings")

if menu == "Video Categories":
    AllVideos = st.sidebar.pills("Select Videos",["All","Education","Animals","Space","Sport","Food"],default="All")
    st.sidebar.write("**:blue[Developed By: Teal_G4m3s]**  📻")

    if AllVideos == "All" or AllVideos == "Education":
        st.subheader("Learning Category")

        a,b,c,d = st.columns(4)

        with a:
            st.image("https://th.bing.com/th/id/OIP.Xfu7Ep9nu1qZSspLlwCPswHaD4?w=203&h=106&c=7&r=0&o=5&pid=1.7")
            st.write("Letters for children")
            if st.button(label="Play Video", key="1"):
                webbrowser.open("https://www.youtube.com/watch?v=RiYzD1h-YVQ&pp=ygUUTGV0dGVycyBmb3IgY2hpbGRyZW4%3D")
                try:
                    videocsv.loc[0,"Letters for children"] += 1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,"Letters for children"] = 1
                    videocsv.to_csv(csvlink, index=False)
    
            with b:
                st.image("https://th.bing.com/th/id/OIP.6O2umQ8VtqUnyVJt2pIGCwHaEK?w=305&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Numbers for children")
                if st.button(label="Play Video", key="1.1"):
                    webbrowser.open("https://www.youtube.com/watch?v=D0Ajq682yrA&pp=ygUUTnVtYmVycyBmb3IgY2hpbGRyZW4%3D")
                    try:
                        videocsv.loc[0,"Numbers for children"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Numbers for children"] = 1
                        videocsv.to_csv(csvlink, index=False)
           
            with c:
                st.image("https://th.bing.com/th/id/OIP.L5qlh_ofogNeDASbCZu_-AHaE7?w=274&h=183&c=7&r=0&o=5&pid=1.7")
                st.write("Learning with teachers")
                if st.button(label="Play Video", key="1.2"):
                    webbrowser.open("https://www.youtube.com/shorts/Iu1maGPhVro")
                    try:
                        videocsv.loc[0,"Learning with teachers"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Learning with teachers"] = 1
                        videocsv.to_csv(csvlink, index=False)
           
            with d:
                st.image("https://th.bing.com/th/id/OIP.o3yj0K1v0IlREgTcc_RYegHaEI?w=303&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Don't forget to count")
                if st.button(label="Play Video", key="1.3"):
                    webbrowser.open("https://www.youtube.com/watch?v=ZJEIKkPXirg&pp=ygUdRG9uJ3QgZm9yZ2V0IHRvIGNvdW50IG51bWJlcnM%3D")
                    try:
                        videocsv.loc[0,"Don't forget to count"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Don't forget to count"] = 1
                        videocsv.to_csv(csvlink, index=False)

    if AllVideos == "All" or AllVideos == "Animals":
        st.subheader("Animals Category")

        e,f,g,h = st.columns(4)

        with e:
            st.image("https://th.bing.com/th/id/OIP.x0ov8f9bc9XFNKnFAuI3qAHaFj?w=230&h=180&c=7&r=0&o=5&pid=1.7")
            st.write("Domestic animals")
            if st.button(label="Play Video", key="2"):
                    webbrowser.open("https://www.youtube.com/watch?v=RVJbKPW3Crs&pp=ygUQRG9tZXN0aWMgQW5pbWFscw%3D%3D")
                    try:
                        videocsv.loc[0,"Domestic animals"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Domestic animals"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with f:
                st.image("https://th.bing.com/th/id/OIP.7bal_3M4TZpuQLwynKzZ1wHaEK?w=208&h=181&c=7&r=0&o=5&pid=1.7")
                st.write("Wild animals")
                if st.button(label="Play Video", key="2.1"):
                    webbrowser.open("https://www.youtube.com/watch?v=OlbOOzX_fDs&pp=ygUMV2lsZCBBbmltYWxz")
                    try:
                        videocsv.loc[0,"Wild animals"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Wild animals"] = 1
                        videocsv.to_csv(csvlink, index=False)
           
            with g:
                st.image("https://th.bing.com/th/id/OIP.HGsbyI2ct_S60G86xB0PTgHaFj?w=237&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("All types of biomes for animals")
                if st.button(label="Play Video", key="2.2"):
                    webbrowser.open("https://www.youtube.com/watch?v=QrBpvELdbSo")
                    try:
                        videocsv.loc[0,"All types of biomes for animals"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"All types of biomes for animals"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with h:
                st.image("https://th.bing.com/th/id/OIP.CVo7uNpqKSMpxiVZG_p9TQHaGP?w=181&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Food chain")
                if st.button(label="Play Video", key="2.3"):
                    webbrowser.open("https://www.youtube.com/watch?v=YuO4WB4SwCg&pp=ygUKRm9vZCBDaGFpbg%3D%3D")
                    try:
                        videocsv.loc[0,"Food chain"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Food chain"] = 1
                        videocsv.to_csv(csvlink, index=False)


    if AllVideos == "All" or AllVideos == "Space":
        st.subheader("Space Category")

        i,j,k,l = st.columns(4)

        with i:
            st.image("https://th.bing.com/th/id/OIP.ZqxFobmreEd4zRBU8J_jFAHaFu?w=240&h=185&c=7&r=0&o=5&pid=1.7")
            st.write("Our solar system")
            if st.button(label="Play Video", key="3"):
                    webbrowser.open("https://www.youtube.com/watch?v=lcZTcfdZ3Ow&pp=ygUQT3VyIFNvbGFyIFN5c3RlbQ%3D%3D")
                    try:
                        videocsv.loc[0,"Our solar system"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Our solar system"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with j:
                st.image("https://th.bing.com/th/id/OIP.4R7TSn4gx2KdrtA_SOg96gHaJi?w=229&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Gas giants")
                if st.button(label="Play Video", key="3.1"):
                    webbrowser.open("https://www.youtube.com/watch?v=P9OG4stArmo")
                    try:
                        videocsv.loc[0,"Gas giants"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Gas giants"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with k:
                st.image("https://th.bing.com/th/id/OIP.YDNmVwkdhr9HVffIiOYU7QHaEH?w=285&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("The galaxy")
                if st.button(label="Play Video", key="3.2"):
                    webbrowser.open("https://www.youtube.com/watch?v=937stSQMr64")
                    try:
                        videocsv.loc[0,"The galaxy"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"The galaxy"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with l:
                st.image("https://th.bing.com/th/id/OIP.rIA824ZZShoLfeqLds4SqQAAAA?w=260&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Travelling through space")
                if st.button(label="Play Video", key="3.3"):
                    webbrowser.open("https://www.youtube.com/watch?v=nGnX6GkrOgk")
                    try:
                        videocsv.loc[0,"Travelling through space"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Travelling through space"] = 1
                        videocsv.to_csv(csvlink, index=False)

    if AllVideos == "All" or AllVideos == "Sport":
        st.subheader("Sports Category")

        m,n,o,p = st.columns(4)

        with m:
            st.image("https://th.bing.com/th/id/OIP.akaXngvfsFkKQ0P-h47L_gHaEK?rs=1&pid=ImgDetMain")
            st.write("Popular sports in different countries")
            if st.button(label="Play Video", key="4"):
                    webbrowser.open("https://www.youtube.com/watch?v=XFue0GRVTts")
                    try:
                        videocsv.loc[0,"Popular sports in different countries"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Popular sports in different countries"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with n:
                st.image("https://th.bing.com/th/id/OIP.47_EFA1Xjb78aD4JXbA14QHaFx?w=247&h=193&c=7&r=0&o=5&pid=1.7")
                st.write("NHL referees")
                if st.button(label="Play Video", key="4.1"):
                    webbrowser.open("https://www.youtube.com/watch?v=uC4pffDeljI")
                    try:
                        videocsv.loc[0,"NHL referees"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"NHL referees"] = 1
                        videocsv.to_csv(csvlink, index=False)
           
            with o:
                st.image("https://th.bing.com/th/id/OIP.EtWuBL0QtqzeCLG-VnYL2wHaEK?w=314&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("The olympics")
                if st.button(label="Play Video", key="4.2"):
                    webbrowser.open("https://www.youtube.com/watch?v=2-7U1vKJy2s")
                    try:
                        videocsv.loc[0,"The olympics"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"The olympics"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with p:
                st.image("https://th.bing.com/th/id/OIP.K6_UmHTNqNBWMwXVidqW8AHaEs?rs=1&pid=ImgDetMain")
                st.write("Safety and injuries")
                if st.button(label="Play Video", key="4.3"):
                    webbrowser.open("https://www.youtube.com/watch?v=I5Xe1Wt4b08")
                    try:
                        videocsv.loc[0,"Safety and injuries"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Safety and injuries"] = 1
                        videocsv.to_csv(csvlink, index=False)
               
    if AllVideos == "All" or AllVideos == "Food":
        st.subheader("Food Category")

        q,r,s,t = st.columns(4)

        with q:
            st.image("https://th.bing.com/th/id/OIP.YhGkrl3qS6w5A1M0QbBBawHaD4?w=336&h=180&c=7&r=0&o=5&pid=1.7")
            st.write("Different foods from countries")
            if st.button(label="Play Video", key="5"):
                    webbrowser.open("https://www.youtube.com/watch?v=FD8X8p9SynI")
                    try:
                        videocsv.loc[0,"Different foods from countries"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Different foods from countries"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with r:
                st.image("https://th.bing.com/th/id/OIP.H5I_B0EUkwuRrt-aTTlSLQHaE8?w=257&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Chefs")
                if st.button(label="Play Video", key="5.1"):
                    webbrowser.open("https://www.youtube.com/watch?v=rsMsPMTkRAA")
                    try:
                        videocsv.loc[0,"Chefs"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Chefs"] = 1
                        videocsv.to_csv(csvlink, index=False)
           
            with s:
                st.image("https://th.bing.com/th/id/OIP.vej54PpEdIF1usVa9yvSqQHaEH?w=320&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Different kinds of seasoning")
                if st.button(label="Play Video", key="5.2"):
                    webbrowser.open("https://www.youtube.com/watch?v=KYEssBzcTA8")
                    try:
                        videocsv.loc[0,"Different kinds of seasoning"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Different kinds of seasoning"] = 1
                        videocsv.to_csv(csvlink, index=False)

            with t:
                st.image("https://th.bing.com/th/id/OIP.fn-3CRMuAs6BUN0vf5_isQHaEK?w=321&h=180&c=7&r=0&o=5&pid=1.7")
                st.write("Cook-offs")
                if st.button(label="Play Video", key="5.3"):
                    webbrowser.open("https://www.youtube.com/watch?v=gauyUvRIPzs")
                    try:
                        videocsv.loc[0,"Cook-offs"] += 1
                        videocsv.to_csv(csvlink,index=False)
                    except KeyError:
                        videocsv.loc[0,"Cook-offs"] = 1
                        videocsv.to_csv(csvlink, index=False)