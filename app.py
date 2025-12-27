import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import os
import plotly.express as px
import openai

# Load environment variables from .env file (for local development)
load_dotenv()

# Get API key from environment or Streamlit secrets
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and hasattr(st, 'secrets'):
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except:
        pass

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Helper function to get dataset path
def get_dataset_path():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the dataset
    csv_path = os.path.join(current_dir, 'data', "customer_reviews.csv")
    return csv_path

# Function to get sentiment using GenAI
@st.cache_data
def get_sentiment(text):
    if not text or pd.isna(text):
        return "Neutral"
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": "Classify the sentiment of the following review as exactly one word: Positive, Negative, or Neutral."
                }
                ,
                {
                    "role": "user",
                    "content": f"What's the sentiment of this review?{text}"
                }
            ],
            temperature=0.0,
            max_output_tokens=100
        )
        return response.output[0].content[0].text.strip()
    except Exception as e:
        st.error(f"API error: {e}")
        return "Neutral"
    

st.title("🔍 GenAI Sentiment Analysis Dashboard")
st.write("This is your GenAI-powered data processing app.")

# Layout two buttons side by side
col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Load Dataset"):
        try:
            csv_path = get_dataset_path()
            df = pd.read_csv(csv_path)
            st.session_state['df'] = df.head(10)
            st.success("Dataset loaded successfully!")
        except FileNotFoundError:
            st.error(f"Dataset not found. Please check the file path")

with col2:
    if st.button("🤖 Analyze Sentiment"):
        if 'df' in st.session_state:
            try:
                with st.spinner("Analyzing sentiment..."):
                    st.session_state["df"].loc[:, "Sentiment"] = st.session_state["df"]["SUMMARY"].apply(get_sentiment)
                    st.success("Sentiment analysis completed!")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
        else:
            st.warning("Please ingest the dataset first")


# Display the dataframe if it exists in session state
if 'df' in st.session_state:
    # Product filter dropdown
    st.subheader("🔍 Filter by Product")
    product = st.selectbox("Choose a product", ["All Products"] + list(st.session_state["df"]["PRODUCT"].unique()))
    st.subheader(f"📁 Reviews for {product}")

    if product != "All Products":
        filtered_df = st.session_state["df"][st.session_state["df"]["PRODUCT"] == product]
    else:
        filtered_df = st.session_state["df"]
    st.dataframe(filtered_df)

    # Visualization using plotly if sentiment analysis has been performed
    if "Sentiment" in st.session_state["df"].columns:
        st.subheader(f"📊 Sentiment Breakdown for {product}")

        # Create Ploty bar chart for sentiments analysis has been perfomed
        sentiment_counts = filtered_df["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]
        
        # Define cusotm order and colors
        sentiment_order = ["Positive", "Neutral", "Negative"]
        sentiment_colors = {"Positive": "green", "Neutral": "gray", "Negative": "red"}

        # Only inlcude sentiments categories that actually exisit in the data
        exisitng_sentiments = sentiment_counts["Sentiment"].unique()
        filtered_order = [s for s in sentiment_order if s in exisitng_sentiments]
        filtered_colours = {s: sentiment_colors[s] for s in filtered_order}

        fig = px.bar(
            sentiment_counts,
            x="Sentiment",
            y="Count",
            labels={"Sentiment": "Sentiment Category", "Count": "Number of Reviews"},
            color="Sentiment",
            title=f"Distribution of Sentiments  Classification - {product}",
            color_discrete_map=filtered_colours,
        )
        fig.update_layout(
            xaxis_title="Sentiment Category",
            yaxis_title="Number of Reviews",
            showlegend=False        
        )
        st.plotly_chart(fig, use_container_width=True)