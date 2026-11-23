# Customer Churn Prediction System

A comprehensive machine learning web application that predicts customer churn using XGBoost and provides AI-powered insights through a modern Flask web interface.

## 🚀 Features

- **Machine Learning Model**: XGBoost-based churn prediction with 21.5% accuracy improvement
- **Web Interface**: Modern, responsive Flask web application with beautiful UI
- **AI Integration**: Cohere AI-powered explanations for predictions
- **Real-time Predictions**: Instant customer churn risk assessment
- **Data Visualization**: Interactive charts and insights dashboard
- **Scalable Architecture**: Production-ready with proper model serialization

## 📊 Model Performance

- **Churn Rate**: 21.5% (↓ 3% this quarter)
- **Average Credit Score**: 650 (↑ 5% from last year)
- **Average Balance**: $76,000 (↑ 2% this month)
- **Prediction Threshold**: 30% probability threshold for churn classification

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: XGBoost, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **AI Integration**: Cohere API
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Plotly, Matplotlib
- **Data Balancing**: SMOTE (Synthetic Minority Oversampling)

## 📁 Project Structure

```
finalproject/
├── app.py                          # Main Flask application
├── main.py                         # Google AI integration test
├── test.py                         # API testing utilities
├── requirements.txt                # Python dependencies
├── Churn_Modelling.csv            # Training dataset
├── best_model.pkl                 # Trained XGBoost model
├── scaler.pkl                     # Feature scaler
├── feature_names.pkl              # Feature names for model input
├── churn-prediction-using-xgboost.ipynb  # Model training notebook
├── powerbi.pbix                   # Power BI dashboard
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── index.html                 # Homepage
│   ├── predict.html               # Prediction form
│   ├── result.html                # Results display
│   ├── about.html                 # About page
│   └── faq.html                   # FAQ page
├── screens/                       # Application screenshots
└── archives/                      # Backup model files
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd finalproject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys** (Optional - for AI explanations)
   - Get a Cohere API key from [Cohere](https://cohere.ai/)
   - Update the API key in `app.py` line 20

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 📈 Usage

### Making Predictions

1. Navigate to the **Predict** page
2. Fill in customer information:
   - **Credit Score**: Customer's credit score (300-850)
   - **Age**: Customer's age
   - **Tenure**: Years with the bank
   - **Balance**: Account balance
   - **Number of Products**: Products purchased
   - **Estimated Salary**: Annual salary
   - **Geography**: Country (France, Germany, Spain)
   - **Gender**: Male/Female
   - **Has Credit Card**: Yes/No
   - **Is Active Member**: Yes/No

3. Click **Predict Churn** to get:
   - Churn probability percentage
   - Retention probability
   - AI-powered explanation of the prediction

### Model Training

The model training process is documented in `churn-prediction-using-xgboost.ipynb`:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables
2. **Feature Engineering**: Creating relevant features for prediction
3. **Data Balancing**: Using SMOTE to handle class imbalance
4. **Model Training**: XGBoost with hyperparameter tuning
5. **Model Evaluation**: Cross-validation and performance metrics
6. **Model Serialization**: Saving trained model and scaler

## 🔧 Configuration

### Environment Variables

Create a `.env` file for sensitive configuration:

```env
COHERE_API_KEY=your_cohere_api_key_here
FLASK_ENV=production
```

### Model Parameters

- **Prediction Threshold**: 0.3 (configurable in `app.py`)
- **Scaling Variables**: CreditScore, Age, Tenure, Balance, NumOfProducts, EstimatedSalary
- **Categorical Variables**: Geography, Gender, HasCrCard, IsActiveMember

## 📊 Data Schema

The model uses the following features:

| Feature | Type | Description |
|---------|------|-------------|
| CreditScore | Numeric | Customer's credit score |
| Age | Numeric | Customer's age |
| Tenure | Numeric | Years with the bank |
| Balance | Numeric | Account balance |
| NumOfProducts | Numeric | Number of products purchased |
| EstimatedSalary | Numeric | Annual salary estimate |
| Geography | Categorical | Country (France, Germany, Spain) |
| Gender | Categorical | Male/Female |
| HasCrCard | Binary | Has credit card (0/1) |
| IsActiveMember | Binary | Active member status (0/1) |

## 🧪 Testing

Run the test suite:

```bash
python test.py
```

## 📱 Screenshots

Check the `screens/` directory for application screenshots showing:
- Homepage with customer insights
- Prediction form interface
- Results display with AI explanations
- Dashboard visualizations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset: Bank Customer Churn Dataset
- Machine Learning: XGBoost, Scikit-learn
- AI Integration: Cohere API
- Web Framework: Flask
- Visualization: Plotly, Matplotlib

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the FAQ page in the application
- Review the model training notebook for technical details

---

**Note**: This application is for educational and demonstration purposes. Ensure you have proper data privacy measures in place when handling real customer data.
