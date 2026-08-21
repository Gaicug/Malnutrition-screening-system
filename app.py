import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Malnutrition Screening",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 25px;
}

.section-header {
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 10px;
    margin-bottom: 15px;
}

.metric-box {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    color: #0f766e;
}

.metric-label {
    font-size: 14px;
    color: #64748b;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load(
        "malnutrition_model/malnutrition_model.pkl"
    )

    encoder = joblib.load(
        "malnutrition_model/label_encoder.pkl"
    )

    return model, encoder


try:

    model, encoder = load_model()

except Exception as e:

    st.error("❌ Unable to load the AI model.")
    st.exception(e)
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🏥 Malnutrition AI")

    st.divider()

    st.subheader("System Information")

    st.write(
        "AI-powered screening system for "
        "childhood malnutrition risk."
    )

    st.divider()

    st.subheader("Input Indicators")

    st.write("👶 Age")
    st.write("📏 Height")
    st.write("⚖️ Weight")
    st.write("⚥ Sex")
    st.write("🦠 Diarrhoea")
    st.write("🎓 Mother's education")
    st.write("💰 Wealth index")
    st.write("🏠 Area")

    st.divider()

    st.caption(
        "AI screening support tool — "
        "not a replacement for clinical assessment."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🏥 AI Malnutrition Screening System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning–based screening for childhood malnutrition risk'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TOP METRICS
# ============================================================

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">AI</div>
        <div class="metric-label">Screening System</div>
    </div>
    """, unsafe_allow_html=True)


with m2:

    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">8</div>
        <div class="metric-label">Input Indicators</div>
    </div>
    """, unsafe_allow_html=True)


with m3:

    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">ML</div>
        <div class="metric-label">Prediction Method</div>
    </div>
    """, unsafe_allow_html=True)


with m4:

    st.markdown("""
    <div class="metric-box">
        <div class="metric-value">2</div>
        <div class="metric-label">Prediction Classes</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# ============================================================
# INTRODUCTION
# ============================================================

with st.expander("🎯 About this system", expanded=True):

    st.write(
        """
        This system uses machine learning to estimate whether a
        child is likely to be **Malnourished** or
        **Not Malnourished** based on demographic,
        anthropometric, socioeconomic and health indicators.

        Enter the child's information and select
        **Predict Malnutrition Risk**.
        """
    )


# ============================================================
# MAIN COLUMNS
# ============================================================

input_col, result_col = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# INPUT SECTION
# ============================================================

with input_col:

    st.markdown(
        '<div class="section-header">'
        '👶 Child Assessment'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter the child's information below."
    )

    age = st.number_input(
        "Age (months)",
        min_value=0,
        max_value=59,
        value=24,
        step=1
    )

    height = st.number_input(
        "Height (cm)",
        min_value=40.0,
        max_value=130.0,
        value=84.0,
        step=0.1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=2.0,
        max_value=30.0,
        value=11.5,
        step=0.1
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    diarrhoea = st.selectbox(
        "Diarrhoea in the last 2 weeks",
        ["No", "Yes", "Unknown"]
    )

    mother_education = st.selectbox(
        "Mother's education",
        [
            "Primary",
            "Secondary+",
            "Unknown"
        ]
    )

    wealth_index = st.selectbox(
        "Wealth index",
        [
            "Poorest",
            "Second",
            "Middle",
            "Fourth",
            "Richest"
        ]
    )

    area = st.selectbox(
        "Area of residence",
        ["Rural", "Urban"]
    )

    st.write("")

    predict_button = st.button(
        "🔍 Predict Malnutrition Risk",
        type="primary",
        use_container_width=True
    )


# ============================================================
# RESULT SECTION
# ============================================================

with result_col:

    st.markdown(
        '<div class="section-header">'
        '📊 AI Prediction'
        '</div>',
        unsafe_allow_html=True
    )

    if not predict_button:

        st.info(
            """
            ### 🤖 Ready for Screening

            Enter the child's information on the left and
            click **Predict Malnutrition Risk**.
            """
        )

    else:

        try:

            # ==================================================
            # INPUT DATA
            # ==================================================

            input_data = pd.DataFrame({

                "age": [age],

                "height": [height],

                "weight": [weight],

                "sex": [sex],

                "diarrhoea": [diarrhoea],

                "mother_education": [mother_education],

                "wealth_index": [wealth_index],

                "area": [area]

            })


            # ==================================================
            # MODEL PREDICTION
            # ==================================================

            prediction = model.predict(
                input_data
            )

            probabilities = model.predict_proba(
                input_data
            )[0]


            predicted_class = encoder.inverse_transform(
                prediction
            )[0]


            # ==================================================
            # PROBABILITIES
            # ==================================================

            probability_dict = dict(
                zip(
                    encoder.classes_,
                    probabilities
                )
            )


            malnourished_probability = (
                probability_dict.get(
                    "Malnourished",
                    0
                ) * 100
            )


            not_malnourished_probability = (
                probability_dict.get(
                    "Not Malnourished",
                    0
                ) * 100
            )


            confidence = max(
                malnourished_probability,
                not_malnourished_probability
            )


            # ==================================================
            # SCREENING RESULT
            # ==================================================

            st.subheader("AI Screening Result")


            if predicted_class == "Malnourished":

                st.error(
                    "🔴 MALNUTRITION RISK"
                )

            else:

                st.success(
                    "🟢 NOT MALNOURISHED"
                )


            st.metric(
                "AI Confidence",
                f"{confidence:.2f}%"
            )


            # ==================================================
            # PROBABILITY METRICS
            # ==================================================

            st.subheader(
                "📈 Prediction Probabilities"
            )


            p1, p2 = st.columns(2)


            with p1:

                st.metric(
                    "🔴 Malnourished",
                    f"{malnourished_probability:.2f}%"
                )


            with p2:

                st.metric(
                    "🟢 Not Malnourished",
                    f"{not_malnourished_probability:.2f}%"
                )


            # ==================================================
            # PROBABILITY CHART
            # ==================================================

            chart_data = pd.DataFrame({

                "Probability": [

                    malnourished_probability,

                    not_malnourished_probability

                ]

            }, index=[

                "Malnourished",

                "Not Malnourished"

            ])


            st.bar_chart(
                chart_data
            )


            # ==================================================
            # INTERPRETATION
            # ==================================================

            st.subheader(
                "🩺 Screening Interpretation"
            )


            if predicted_class == "Malnourished":

                st.warning(
                    """
                    **Screening Alert**

                    The model has classified this child as
                    potentially **malnourished**.

                    Further nutritional assessment and
                    professional clinical evaluation should
                    be considered.
                    """
                )

            else:

                st.success(
                    """
                    **Screening Result**

                    The model classified this child as
                    **not malnourished** based on the
                    information provided.

                    Continue routine growth monitoring and
                    nutritional assessment as appropriate.
                    """
                )


            # ==================================================
            # ASSESSMENT SUMMARY
            # ==================================================

            st.subheader(
                "📋 Assessment Summary"
            )


            summary = pd.DataFrame({

                "Indicator": [

                    "Age",

                    "Height",

                    "Weight",

                    "Sex",

                    "Diarrhoea",

                    "Mother's Education",

                    "Wealth Index",

                    "Area"

                ],

                "Value": [

                    f"{age} months",

                    f"{height:.1f} cm",

                    f"{weight:.1f} kg",

                    sex,

                    diarrhoea,

                    mother_education,

                    wealth_index,

                    area

                ]

            })


            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )


        except Exception as e:

            st.error(
                "❌ Prediction failed."
            )

            st.exception(e)



# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.subheader("🤖 Model Performance")

st.write(
    """
    The malnutrition classification model was evaluated using
    Accuracy, Precision, Recall, F1 Score and ROC-AUC.
    """
)

performance = pd.DataFrame({
    "Model": [
        "Gradient Boosting",
        "Random Forest",
        "Logistic Regression"
    ],

    "Accuracy": [
        0.6753,
        0.6753,
        0.6104
    ],

    "Precision": [
        0.6953,
        0.7551,
        0.7273
    ],

    "Recall": [
        0.8900,
        0.7400,
        0.6400
    ],

    "F1 Score": [
        0.7807,
        0.7475,
        0.6809
    ],

    "ROC-AUC": [
        0.6160,
        0.6582,
        0.6258
    ]
})

st.dataframe(
    performance.style.format({
        "Accuracy": "{:.2%}",
        "Precision": "{:.2%}",
        "Recall": "{:.2%}",
        "F1 Score": "{:.2%}",
        "ROC-AUC": "{:.2%}"
    }),
    use_container_width=True,
    hide_index=True
)



# ============================================================
# DATASET SUMMARY
# ============================================================

st.subheader("📊 Dataset Summary")

d1, d2, d3 = st.columns(3)

with d1:
    st.metric(
        "Children",
        "799"
    )

with d2:
    st.metric(
        "Malnourished",
        "17.43%"
    )

with d3:
    st.metric(
        "Not Malnourished",
        "82.57%"
    )

# ============================================================
# EXPLAINABLE AI
# ============================================================

st.subheader("🔎 Explainable AI")

st.write(
    """
    Feature importance analysis identifies which variables
    contributed most strongly to the model's predictions.
    """
)

feature_importance = pd.DataFrame({
    "Feature": [
        "Age",
        "Wealth Index: Poorest",
        "Wealth Index: Richest",
        "Wealth Index: Middle",
        "Mother Education: Unknown",
        "Sex: Male",
        "Sex: Female",
        "Wealth Index: Second",
        "Wealth Index: Fourth",
        "Mother Education: Secondary+",
        "Area: Urban",
        "Diarrhoea: No",
        "Diarrhoea: Yes",
        "Area: Rural",
        "Mother Education: Primary"
    ],

    "Importance": [
        0.521673,
        0.125085,
        0.057516,
        0.040343,
        0.038861,
        0.038106,
        0.035163,
        0.029062,
        0.028876,
        0.018202,
        0.017896,
        0.014592,
        0.014538,
        0.011450,
        0.008638
    ]
})

st.bar_chart(
    feature_importance.set_index("Feature")
)

st.info(
    """
    **Key finding:** Age was the most influential feature in the
    model, followed by socioeconomic indicators such as wealth
    index. This suggests that both child age and household
    socioeconomic conditions are important predictors of
    malnutrition risk in this dataset.
    """
)
# ============================================================
# WHO GROWTH ASSESSMENT
# ============================================================

st.divider()

st.subheader("📏 WHO Growth Assessment")

who_data = pd.read_csv(
    "data/who_combined.csv"
)

st.write(
    """
    WHO growth indicators provide standardized measures of
    child growth and nutritional status.
    """
)

who1, who2, who3, who4 = st.columns(4)

with who1:
    st.metric(
        "HAZ",
        f"{who_data['haz'].mean():.2f}"
    )
    st.caption("Height-for-Age")

with who2:
    st.metric(
        "WAZ",
        f"{who_data['waz'].mean():.2f}"
    )
    st.caption("Weight-for-Age")

with who3:
    st.metric(
        "WHZ",
        f"{who_data['whz'].mean():.2f}"
    )
    st.caption("Weight-for-Height")

with who4:
    st.metric(
        "BAZ",
        f"{who_data['baz'].mean():.2f}"
    )
    st.caption("BMI-for-Age")


st.subheader("🩺 WHO Nutritional Indicators")

stunting = (who_data["haz"] < -2).sum()
underweight = (who_data["waz"] < -2).sum()
wasting = (who_data["whz"] < -2).sum()

total_children = len(who_data)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Stunting",
        f"{stunting} children"
    )
    st.caption(
        f"{stunting / total_children * 100:.2f}%"
    )

with c2:
    st.metric(
        "Underweight",
        f"{underweight} children"
    )
    st.caption(
        f"{underweight / total_children * 100:.2f}%"
    )

with c3:
    st.metric(
        "Wasting",
        f"{wasting} children"
    )
    st.caption(
        f"{wasting / total_children * 100:.2f}%"
    )
# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.warning(
    """
    **⚠️ Important:** This system is an AI-based screening
    and decision-support tool. It does not replace professional
    medical, nutritional or clinical assessment. Predictions
    should be interpreted by qualified health professionals
    alongside appropriate anthropometric and clinical measurements.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🏥 AI Malnutrition Screening System"
)

st.caption(
    "Machine Learning for Public Health Decision Support"
)

st.caption(
    "Developed by Joy Kaaria | "
    "BSc Information Technology | Karatina University"
)