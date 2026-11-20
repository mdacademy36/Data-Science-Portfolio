
import streamlit as st
import pandas as pd
import numpy as np
import joblib

from pathlib import Path


# ==========================================
# CONFIGURATION
# ==========================================

DATA_PATH = Path("dataset/car_price_prediction.csv")
MODEL_PATH = Path("model/rf_model.pkl")
FEATURE_PATH = Path("model/feature_columns.pkl")
IMPUTER_PATH = Path("model/imputer.pkl")
SCALER_PATH = Path("model/scaler.pkl")

CURRENT_YEAR = 2025

NUM_COLS = [
    "Mileage",
    "Levy",
    "Engine volume",
    "car_age",
    "Cylinders",
    "Airbags"
]

CATEGORICAL_COLS = [
    "Manufacturer",
    "Category",
    "Fuel type",
    "Gear box type",
    "Drive wheels"
]

BASE_CATEGORIES = {
    "Manufacturer": "ACURA",
    "Category": "Cabriolet",
    "Fuel type": "CNG",
    "Gear box type": "Automatic",
    "Drive wheels": "4x4"
}


# ==========================================
# DATA LOADING
# ==========================================

@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        return pd.DataFrame()

    return pd.read_csv(DATA_PATH)
    df = pd.read_csv(DATA_PATH)

    print("Dataset Shape:", df.shape)
    print("Average Price:", df["Price"].mean())

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_feature_columns():
    return joblib.load(FEATURE_PATH)


@st.cache_resource
def load_imputer():
    return joblib.load(IMPUTER_PATH)


@st.cache_resource
def load_scaler():
    return joblib.load(SCALER_PATH)


# ==========================================
# FEATURE DESCRIPTION
# ==========================================

def get_feature_description():

    data = {
        "Column Name": [
            "ID", "Price", "Levy", "Manufacturer",
            "Model", "Prod. year", "Category",
            "Leather interior", "Fuel type",
            "Engine volume", "Mileage", "Cylinders",
            "Gear box type", "Drive wheels", "Doors",
            "Wheel", "Color", "Airbags"
        ],

        "Description": [
            "Unique identifier for each vehicle",
            "Target variable: selling price",
            "Additional vehicle fees or tax",
            "Vehicle manufacturer brand",
            "Vehicle model name",
            "Production year",
            "Vehicle category type",
            "Leather interior availability",
            "Fuel type used",
            "Engine capacity",
            "Vehicle mileage",
            "Number of cylinders",
            "Transmission type",
            "Drive wheel system",
            "Number of doors",
            "Steering wheel position",
            "Vehicle color",
            "Number of airbags"
        ],

        "Data Type": [
            "Numeric", "Numeric", "Numeric",
            "Categorical", "Categorical", "Numeric",
            "Categorical", "Categorical", "Categorical",
            "Numeric", "Numeric", "Numeric",
            "Categorical", "Categorical", "Categorical",
            "Categorical", "Categorical", "Numeric"
        ]
    }

    return pd.DataFrame(data)


# ==========================================
# PRICE PREDICTION
# ==========================================

def predict_price(model, input_data):

    features = load_feature_columns()
    imputer = load_imputer()
    scaler = load_scaler()

    if len(features) != 94:
        raise ValueError(
            f"Model membutuhkan 94 fitur, tetapi ditemukan {len(features)}."
        )

    X = pd.DataFrame(
        0.0,
        index=[0],
        columns=features
    )

    # Numeric and binary features
    X["Levy"] = input_data["Levy"]
    X["Levy_available"] = input_data["Levy_available"]
    X["Leather interior"] = input_data["Leather interior"]
    X["Mileage"] = input_data["Mileage"]
    X["Engine volume"] = input_data["Engine volume"]
    X["Turbo"] = input_data["Turbo"]
    X["car_age"] = CURRENT_YEAR - input_data["Prod. year"]
    X["Cylinders"] = input_data["Cylinders"]
    X["Airbags"] = input_data["Airbags"]

    
    # One-hot encoding
    for col in CATEGORICAL_COLS:

        value = input_data[col]
        dummy_column = f"{col}_{value}"

        if dummy_column in X.columns:
            X.loc[0, dummy_column] = 1

        elif value != BASE_CATEGORIES[col]:
            raise ValueError(
                f"Kategori {value} pada {col} tidak ditemukan "
                "dalam fitur training."
            )

    # Imputation
    X[NUM_COLS] = imputer.transform(X[NUM_COLS])

    # Scaling
    X[NUM_COLS] = scaler.transform(X[NUM_COLS])

    # Prediction
    prediction_log = model.predict(X)
    prediction = np.expm1(prediction_log[0])

    return prediction, X


# ==========================================
# MAIN APP
# ==========================================

def app():

    # CSS
    st.markdown("""
        <style>
        [data-testid="stWidgetLabel"] p,
        [data-testid="stWidgetLabel"] label {
            color: #45566f !important;
            font-weight: 600 !important;
        }

        .stTextInput input,
        .stNumberInput input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            background-color: #263238 !important;
        }

        [data-testid="stFormSubmitButton"] button {
            background-color: #1677A5 !important;
            color: #FFFFFF !important;
            border: 2px solid #1677A5 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }

        [data-testid="stFormSubmitButton"] button:hover {
            background-color: #125F85 !important;
            border-color: #125F85 !important;
        }
        /* DATASET PREVIEW & FEATURE DESCRIPTION */
        .st-key-dataset-preview [data-testid="stExpander"] {
            border: none !important;
            background: transparent !important;
        }

        .st-key-dataset-preview [data-testid="stExpander"] summary {
            background-color: #FFFFFF !important;
            border: 1px solid #D5DEE5 !important;
            border-radius: 10px !important;
            padding: 14px 18px !important;
        }

        .st-key-feature-description [data-testid="stExpander"] {
            border: none !important;
            background: transparent !important;
        }

        .st-key-feature-description [data-testid="stExpander"] summary {
            background-color: #FFFFFF !important;
            border: 1px solid #D5DEE5 !important;
            border-radius: 10px !important;
            padding: 14px 18px !important;
        }

        .st-key-dataset-preview [data-testid="stExpander"] summary p,
        .st-key-feature-description [data-testid="stExpander"] summary p {
            font-weight: 600 !important;
            color: #263C4A !important;
        }
        </style>
    """, unsafe_allow_html=True)

    df = load_data()

    # ======================================
    # HEADER
    # ======================================

    st.html("""
    <div style="
        background: linear-gradient(120deg, #123C43, #1B6570);
        padding: 30px;
        border-radius: 14px;
        margin-bottom: 25px;
    ">
        <p style="
            color: #80CBC4;
            font-size: 13px;
            letter-spacing: 2px;
        ">
            MACHINE LEARNING · REGRESSION
        </p>

        <h1 style="
            color: #FFFFFF !important;
            margin: 0;
            font-size: 35px;
        ">
            Used Car Price Prediction
        </h1>

        <p style="
            color: #E0EEEE;
            font-size: 15px;
            margin-top: 10px;
        ">
            Predicting vehicle prices using machine learning
            based on vehicle specifications.
        </p>
    </div>
    """)

    if df.empty:
        st.error("Dataset not found. Check dataset/car_price_prediction.csv.")
        return

    # ======================================
    # DATASET OVERVIEW
    # ======================================

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Original Records", f"{len(df):,}")

    col2.metric("Original Features", len(df.columns))

    col3.metric(
        "Average Price",
        f"${pd.to_numeric(df['Price'], errors='coerce').mean():,.0f}"
    )

    col4.metric(
        "Manufacturers",
        df["Manufacturer"].nunique()
    )

    st.caption(
        "Original Dataset: Car Price Prediction | "
        "Target Variable: Price"
    )

    st.divider()

    # ======================================
    # DATASET PREVIEW
    # ======================================

    st.subheader("Dataset Preview")

    with st.container(key="dataset-preview"):
        with st.expander("View Dataset", expanded=False):
            st.dataframe(
                df.head(10),
                use_container_width=True,
                hide_index=True
            )

    st.divider()

    # ======================================
    # FEATURE DESCRIPTION
    # ======================================

    st.subheader("Feature Description")

    with st.container(key="feature-description"):
        with st.expander("Explore Dataset Features", expanded=False):
            st.dataframe(
                get_feature_description(),
                use_container_width=True,
                hide_index=True
            )
    st.divider()

    # ======================================
    # DATA EXPLORATION
    # ======================================

    st.subheader("Data Exploration")

    st.write(
        "Explore the distribution of vehicle prices "
        "and the characteristics of the dataset."
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        st.markdown("**Price Distribution**")

        price_data = pd.to_numeric(
            df["Price"], errors="coerce"
        ).dropna()

        if not price_data.empty:

            price_bins = pd.cut(
                price_data,
                bins=10
            ).value_counts().sort_index()

            price_chart = pd.DataFrame({
                "Price Range": price_bins.index.astype(str),
                "Number of Cars": price_bins.values
            }).set_index("Price Range")

            st.bar_chart(price_chart)

    with chart_col2:

        st.markdown("**Top 10 Manufacturers**")

        manufacturer_data = (
            df["Manufacturer"]
            .value_counts()
            .head(10)
        )

        st.bar_chart(manufacturer_data)

    st.divider()

    # ======================================
    
    st.divider()

    # ======================================
    # MODELING INFORMATION
    # ======================================

    st.subheader("Modeling Information")

    st.write(
        "The Random Forest Regressor model was trained "
        "using the cleaned dataset after data preprocessing."
    )

    model_col1, model_col2, model_col3, model_col4 = st.columns(4)

    model_col1.metric("Training Records", "18,906")
    model_col2.metric("Encoded Features", "94")
    model_col3.metric("Train-Test Split", "80:20")
    model_col4.metric("R² Score", "0.605")

    st.markdown("#### Model Evaluation")

    eval_col1, eval_col2, eval_col3 = st.columns(3)

    eval_col1.metric("MAE", "$5,128")
    eval_col2.metric("RMSE", "$11,545")
    eval_col3.metric("R²", "60.45%")

    st.caption(
        "Selected Model: Random Forest Regressor | "
        "Baseline Model"
    )

    st.divider()

    # ======================================
    # PRICE PREDICTION
    # ======================================

    st.subheader("Vehicle Price Prediction")


    # Check model files
    required_files = [
        MODEL_PATH,
        FEATURE_PATH,
        IMPUTER_PATH,
        SCALER_PATH
    ]

    missing_files = [
        str(path) for path in required_files
        if not path.exists()
    ]

    if missing_files:
        st.error(
            "Model files not found: "
            + ", ".join(missing_files)
        )
        return

    # ======================================
    # INPUT FORM
    # ======================================

    with st.form("prediction_form"):

        st.markdown("#### Vehicle Specifications")

        col1, col2 = st.columns(2)

        with col1:

            manufacturer = st.selectbox(
                "Manufacturer",
                sorted(df["Manufacturer"].dropna().unique())
            )

            category = st.selectbox(
                "Category",
                sorted(df["Category"].dropna().unique())
            )

            fuel_type = st.selectbox(
                "Fuel Type",
                sorted(df["Fuel type"].dropna().unique())
            )

            gearbox = st.selectbox(
                "Gear Box Type",
                sorted(df["Gear box type"].dropna().unique())
            )

            drive = st.selectbox(
                "Drive Wheels",
                sorted(df["Drive wheels"].dropna().unique())
            )

            leather = st.selectbox(
                "Leather Interior",
                ["Yes", "No"]
            )

            prod_year = st.number_input(
                "Production Year",
                min_value=1990,
                max_value=CURRENT_YEAR,
                value=2015
            )

        with col2:

            mileage = st.number_input(
                "Mileage (km)",
                min_value=0,
                value=50000
            )

            levy = st.selectbox(
                "Levy Available?",
                ["Yes", "No"]
            )

            levy_amount = st.number_input(
                "Levy Amount",
                min_value=0,
                value=0
            )

            engine_volume = st.number_input(
                "Engine Volume (L)",
                min_value=0.1,
                max_value=10.0,
                value=2.0,
                step=0.1
            )

            turbo = st.selectbox(
                "Turbo",
                ["No", "Yes"]
            )

            cylinders = st.number_input(
                "Cylinders",
                min_value=1,
                value=4
            )

            airbags = st.number_input(
                "Airbags",
                min_value=0,
                value=4
            )

        submit = st.form_submit_button(
            "Predict Car Price",
            use_container_width=True
        )

    # ======================================
    
    # ======================================
    # PREDICTION RESULT
    # ======================================

    if submit:

        if levy == "Yes" and levy_amount <= 0:
            st.error("Levy amount must be greater than zero.")

        elif engine_volume <= 0:
            st.error("Engine volume must be greater than zero.")

        else:
            try:

                model = load_model()

                # Same cleaning rules as training
                mileage_value = (
                    np.nan
                    if mileage == 0 or mileage >= 99999
                    else mileage
                )

                input_data = {
                    "Manufacturer": manufacturer,
                    "Category": category,
                    "Fuel type": fuel_type,
                    "Gear box type": gearbox,
                    "Drive wheels": drive,

                    "Leather interior": (
                        1 if leather == "Yes" else 0
                    ),

                    "Prod. year": prod_year,
                    "Mileage": mileage_value,

                    "Levy": (
                        levy_amount if levy == "Yes" else np.nan
                    ),

                    "Levy_available": (
                        1 if levy == "Yes" else 0
                    ),

                    "Engine volume": engine_volume,

                    "Turbo": (
                        1 if turbo == "Yes" else 0
                    ),

                    "Cylinders": cylinders,
                    "Airbags": airbags
                }

                predicted_price, processed_input = predict_price(
                    model,
                    input_data
                )

                # Prediction success notification
                st.markdown("""
                <div style="
                    background-color: #D1F0DC;
                    border: 1px solid #A8DDBB;
                    border-radius: 8px;
                    padding: 16px;
                    margin: 12px 0;
                ">
                    <p style="
                        color: #123C43 !important;
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        font-weight: 600;
                        margin: 0;
                    ">
                        Prediction completed successfully!
                    </p>
                </div>
                """, unsafe_allow_html=True)

                st.metric(
                    label="Estimated Vehicle Price",
                    value=f"${predicted_price:,.0f}"
                )

                st.caption(
                    "Estimated price generated by the "
                    "Random Forest regression model."
                )

                with st.expander("View Processed Input"):
                    st.dataframe(
                        processed_input,
                        use_container_width=True
                    )

            except Exception as error:
                st.error(f"Prediction failed: {error}")

    st.divider()

    # ======================================
    # FEATURE IMPORTANCE
    # ======================================

    st.subheader("Model Feature Importance")

    try:

        model = load_model()

        if hasattr(model, "feature_importances_"):

            importance_df = pd.DataFrame({
                "Feature": model.feature_names_in_,
                "Importance": model.feature_importances_
            }).sort_values(
                "Importance",
                ascending=False
            ).head(10)

            importance_df = importance_df.set_index("Feature")

            st.bar_chart(
                importance_df,
                horizontal=True
            )
            st.caption(
            "Feature importance represents the relative contribution "
            "of each feature to the model's predictions. "
            "It does not indicate the direction of the relationship."
        )
        else:

            st.info("Feature importance is unavailable.")

    except Exception as error:

        st.warning(
            f"Could not load feature importance: {error}"
        )
