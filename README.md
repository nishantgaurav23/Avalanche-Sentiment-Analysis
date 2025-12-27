# Avalanche Sentiment Analysis Dashboard

A GenAI-powered sentiment analysis dashboard built with Streamlit that analyzes customer reviews using OpenAI's GPT-4o model.

## Features

- **AI-Powered Sentiment Analysis**: Uses GPT-4o to classify customer reviews as Positive, Negative, or Neutral
- **Interactive Dashboard**: Built with Streamlit for an intuitive user experience
- **Product Filtering**: Filter reviews by specific products
- **Visual Analytics**: Interactive charts showing sentiment distribution using Plotly
- **Real-time Analysis**: Instant sentiment classification of customer feedback

## Demo

The dashboard allows you to:
1. Load customer review data
2. Analyze sentiment using AI
3. Filter reviews by product
4. Visualize sentiment distribution with interactive charts

## Technologies Used

- **Streamlit**: Web application framework
- **OpenAI API (GPT-4o)**: AI-powered sentiment classification
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualizations
- **Python-dotenv**: Environment variable management

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Avalanche-Sentiment-Analysis.git
cd Avalanche-Sentiment-Analysis
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to `http://localhost:8501`

4. Use the dashboard:
   - Click **"Load Dataset"** to load customer reviews
   - Click **"Analyze Sentiment"** to run AI-powered sentiment analysis
   - Use the product filter to view specific product reviews
   - View the interactive sentiment distribution chart

## Project Structure

```
Avalanche-Sentiment-Analysis/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not tracked)
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
└── data/
    └── customer_reviews.csv   # Customer review dataset
```

## Dataset

The `customer_reviews.csv` contains customer feedback with the following columns:
- **PRODUCT**: Product name
- **DATE**: Review date
- **SUMMARY**: Review text
- **SENTIMENT_SCORE**: Pre-existing sentiment score
- **Order ID**: Order identifier

## Configuration

### Environment Variables

Create a `.env` file with the following:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Streamlit Cloud Deployment

To deploy on Streamlit Cloud:
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `OPENAI_API_KEY` in the Secrets management section

## Security Notes

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude sensitive files
- When deploying to Streamlit Cloud, use the Secrets management feature for API keys

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for providing the GPT-4o API
- Streamlit for the excellent web framework
- Plotly for interactive visualizations

## Contact

For questions or feedback, please open an issue in the GitHub repository.
