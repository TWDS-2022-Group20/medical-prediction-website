import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def st_website_setting():
    st.set_page_config(
        page_title="Mental Health Helper",
        page_icon="💙",
        layout="centered",
        initial_sidebar_state="auto",
    )


def st_sidebar_info():
    with st.sidebar:
        st.title("Introduction")
        st.info(
            """
            Depressive related disorder risk prediction。\n
            Data : [USA CDC BRFSS 2020 data](https://www.cdc.gov/brfss/annual_data/annual_2020.html)
            """
        )
        st.title("Contributors")
        st.info(
            """
            Contributors: [Sam Shen](),
            [Eli Chen](https://www.linkedin.com/in/jie-han-chen-325620a3/),
            [Martin Lee](),
            [Cobra Chen](),
            [Allen Shiah](),
            \n
            Adviser: [Adms Chung](https://www.linkedin.com/in/admsc/)
            """
        )
        st.title("Contact")
        st.info(
            """
                If any problem was found, please feel free to contact us!
                - Sam Shen: zoro6mihawk At gmail.com
                - Eli Chen: ita3051 At gmail.com
                """
        )
        st.write("""---""")


def st_title_info():
    st.title("Depressive Mood Disorder Predictor")
    st.subheader(
        """
    This application will help you to identifiy the risk stratification of depressive mood related disorders.
    """,
        anchor=None,
    )
    st.write("Thanks for using our product!")
    st.write("---")


def generate_user_input_df():
    basic_features = [
        "SEXVAR",
        "_AGEG5YR",
        "_AGE80",
        "HTM4_N",
        "HTM4_C",
        "WTKG3_C",
        "WTKG3_N",
        "_BMI5_C",
        "_BMI5_N",
    ]
    mental_features = [
        "MENTHLTH_C",
        "MENTHLTH_N",
        "POORHLTH_C",
        "POORHLTH_N",
        "_MENT14D",
        "DECIDE",
        "DIFFALON",
        "ACEDEPRS",
    ]
    other_features = [
        "PHYSHLTH_C",
        "PHYSHLTH_N",
        "FALL12MN_C",
        "FALL12MN_N",
        "SLEPTIM1_C",
        "SLEPTIM1_N",
        "ALCDAY5_C",
        "ALCDAY5_N",
        "EMPLOY1",
        "GENHLTH",
        "MARITAL",
        "_SMOKER3",
        "_DRDXAR2",
        "SOFEMALE",
        "RENTHOM1",
        "_TOTINDA",
        "EDUCA",
        "PERSDOC2",
        "INCOME2",
        "_URBSTAT",
    ]
    important_features = basic_features + mental_features + other_features
    df_user_answer = pd.DataFrame([], columns=important_features, index=[0])
    return df_user_answer


def draw_risk_bar(pred):
    fig, ax = plt.subplots(figsize=(0.2, 3))
    fig.subplots_adjust(bottom=0.5)
    cmap = mpl.cm.YlOrRd
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    cbar = fig.colorbar(
        mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax,
        orientation="vertical",
        ticks=[0.0, 0.231, 0.5, 0.734, 0.851, 0.898],
    )
    ax.set_title("Your risk stratification", fontsize=8)
    cbar.ax.set_yticklabels(
        ["No risk", "Low", "Medium", "High", "Very high", "Extreme high"],
        fontsize=5,
    )
    cbar.ax.plot([0, 1], [pred, pred], "black", linewidth=0.50)
    cbar.ax.plot([0], [pred], color="grey", marker=">", linewidth=0.05)
    cbar.ax.plot([1], [pred], color="grey", marker="<", linewidth=0.05)
    return fig


def get_data_from_testset(index):
    # TODOs: get data from testset
    data = pd.read_csv(
        "data/brfss_combine_test_v2_important_20220708.csv", index_col=[0]
    )
    data.drop(["ADDEPEV3"], axis=1, inplace=True)
    index_row = data.loc[[index]].to_numpy()
    return index_row
