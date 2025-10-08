# MediCore - Healthcare AI Web Application

![MediCore Logo](website/static/images/logo.png)

## Overview

MediCore is an intelligent healthcare web application that uses machine learning and deep learning algorithms to predict various diseases. The application provides users with an easy-to-use interface to check their chances of having specific diseases based on their symptoms and medical data.

## Features

The application can predict the following diseases:

- **Diabetes Disease** - Forecasts diabetes based on patient data
- **Stroke Disease** - Predicts stroke risk using medical parameters
- **Heart Disease** - Analyzes heart disease risk factors

## Technology Stack

- **Backend:** Flask (Python web framework)
- **Machine Learning:** Scikit-learn, TensorFlow, Keras
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Deployment:** Docker, Vercel

## Project Structure

```
MediCore/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile           # Docker configuration
├── vercel.json          # Vercel deployment config
├── website/
│   ├── models.py        # Database models
│   ├── views.py         # Flask routes
│   ├── prediction.py    # ML prediction logic
│   ├── app_models/      # Trained ML models
│   ├── static/          # CSS, JS, images
│   ├── templates/        # HTML templates
│   └── uploads/          # User uploaded files
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd MediCore
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and go to `http://localhost:5000`

### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t medicore .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 medicore
   ```

## Usage

1. Navigate to the disease prediction page you're interested in
2. Fill in the required parameters (symptoms, test results, etc.)
3. For pneumonia prediction, upload a chest X-ray image
4. Click "Predict" to get your disease risk assessment
5. View detailed results and recommendations

## Model Information

- **Diabetes:** Gradient boosting with patient health data
- **Stroke:** Logistic regression with risk factors
- **Heart Disease:** Support Vector Machine with cardiovascular parameters

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Datasets used for training are available on Kaggle
- Medical imaging datasets from various healthcare repositories
- Flask community for excellent documentation
