import streamlit as st

st.set_page_config(
    page_title="LivFit - Personal Diet Recommendation",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None,

)
st.markdown(
    """
<style>

    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Main title
st.title("Welcome to LivFit !!")


st.markdown(
    """
    The "Livfit" is a web app that offers personalized diet suggestions based on users' nutritional needs and preferences. By analyzing the content of various foods and considering factors like age and dietary restrictions, it generates customized meal plans to help users maintain a balanced diet and achieve their health goals. Through machine learning algorithms, the system matches users with suitable food options, aiming to facilitate healthier eating habits and improve overall well-being.
    """
)


def redirect(url):
    redirect_html = f"<meta http-equiv='refresh' content='0;URL={url}'>"
    st.write(redirect_html, unsafe_allow_html=True)

if st.button("Recommend Diets"):
    redirect("/Recommending_Diets")

# Redirect to Recommend Custom Food page
if st.button("Recommend Custom Food"):
    redirect("/Recommending_Custom_Foods")