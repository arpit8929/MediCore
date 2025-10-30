# MediCore - AI-Powered Healthcare Prediction Platform

![MediCore Logo](website/static/images/logo.png)

## 🏥 Overview

**MediCore** is an intelligent healthcare web application that leverages advanced machine learning algorithms to predict heart disease risk. Built with modern web technologies and AI, it provides users with an intuitive interface to assess their cardiovascular health based on clinical parameters and medical data.

## ✨ Key Features

### 🫀 **Heart Disease Prediction**
- **Comprehensive Risk Assessment**: Analyzes 11 critical cardiovascular parameters
- **Real-time Predictions**: Instant results with detailed risk analysis
- **Smart Risk Scoring**: Advanced algorithm that considers multiple risk factors
- **Personalized Recommendations**: Tailored health advice based on prediction results

### 📊 **Clinical Parameters Analyzed**
1. **Age** - Patient's age in years
2. **Gender** - Biological sex (Male/Female)
3. **Chest Pain Type** - Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic
4. **Resting Blood Pressure** - Systolic pressure in mm Hg
5. **Serum Cholesterol** - Cholesterol level in mg/dl
6. **Fasting Blood Sugar** - Blood glucose levels
7. **Resting ECG** - Electrocardiographic results
8. **Maximum Heart Rate** - Peak heart rate achieved
9. **Exercise Induced Angina** - Chest pain during exercise
10. **ST Depression** - Exercise-induced ST segment depression
11. **Slope** - Peak exercise ST segment slope

### 🎯 **Smart Prediction System**
- **Conservative Approach**: Only predicts disease for high-risk cases (5+ risk factors)
- **Clinical Validation**: Based on established medical risk factors
- **Balanced Algorithm**: Prevents false positives while maintaining sensitivity

## 🛠️ Technology Stack

### **Backend & AI**
- **Framework**: Flask 2.0.1 (Python web framework)
- **Machine Learning**: Scikit-learn 0.24.2, TensorFlow 2.6.0, XGBoost 1.4.2
- **Database**: SQLite with SQLAlchemy ORM
- **Server**: Gunicorn 20.1.0 (Production WSGI server)

### **Frontend**
- **HTML5**: Semantic markup with responsive design
- **CSS3**: Bootstrap framework with custom styling
- **JavaScript**: jQuery, smooth scrolling, animations
- **UI/UX**: Modern, medical-themed interface

### **Deployment & DevOps**
- **Containerization**: Docker with Python 3.9-slim
- **Cloud Platform**: Vercel (Serverless deployment)
- **Version Control**: Git with comprehensive .gitignore
- **CI/CD**: Automated deployment pipeline

## 📁 Project Structure

```
MediCore/
├── 📄 app.py                    # Main Flask application entry point
├── 📄 requirements.txt          # Python dependencies with specific versions
├── 🐳 Dockerfile               # Docker containerization configuration
├── ⚙️ vercel.json              # Vercel serverless deployment config
├── 📄 .dockerignore            # Docker build optimization
├── 📄 .gitignore               # Git version control exclusions
├── 📁 website/                 # Core application package
│   ├── 📄 __init__.py          # Flask app factory
│   ├── 📄 models.py            # Database models (SQLAlchemy)
│   ├── 📄 views.py             # Flask routes and endpoints
│   ├── 📄 prediction.py        # ML prediction API endpoints
│   ├── 📄 app_functions.py     # Core ML prediction logic
│   ├── 📄 messages.py          # Contact form handling
│   ├── 📁 app_models/          # Trained ML models
│   │   └── 🧠 heart_model.pkl  # Heart disease prediction model
│   ├── 📁 static/              # Static assets
│   │   ├── 📁 css/             # Stylesheets (Bootstrap, custom)
│   │   ├── 📁 js/              # JavaScript libraries
│   │   ├── 📁 images/          # Images and icons
│   │   │   ├── 📁 recom/       # Recommendation images
│   │   │   └── 📁 model_img/   # Model showcase images
│   │   └── 📁 fonts/           # Web fonts
│   ├── 📁 templates/           # Jinja2 HTML templates
│   │   ├── 📄 base.html        # Base template
│   │   ├── 📄 disease_page.html # Disease page layout
│   │   ├── 📄 heart_index.html # Heart disease info page
│   │   ├── 📄 heart.html       # Heart prediction form
│   │   ├── 📄 result.html      # Prediction results
│   │   └── 📄 recommendations.html # Health recommendations
│   └── 📁 uploads/             # User uploaded files
└── 📄 README.md                # Project documentation
```

## 🚀 Installation & Setup

### **Prerequisites**
- **Python 3.9+** (Recommended: Python 3.9)
- **pip** (Python package installer)
- **Docker** (Optional, for containerized deployment)
- **Git** (For version control)

### **Local Development**

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd MediCore
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv_39
   # Windows
   venv_39\Scripts\activate
   # Linux/Mac
   source venv_39/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and go to `http://localhost:5000`

### **Docker Deployment**

1. **Build the Docker image:**
   ```bash
   docker build -t medicore .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 medicore
   ```

3. **Access the application:**
   Open your browser and go to `http://localhost:5000`

## 📱 How to Use MediCore

### **Step-by-Step Guide**

1. **🏠 Homepage Navigation**
   - Visit the application homepage
   - Explore the "Our Services" section
   - Click on "Heart Disease" model

2. **📋 Data Input**
   - Navigate to the heart disease prediction form
   - Fill in all 11 required clinical parameters:
     - Personal info (Age, Gender)
     - Medical history (Chest pain, Blood pressure, Cholesterol)
     - Test results (ECG, Heart rate, Exercise response)
   - Ensure all fields are completed accurately

3. **🔮 Prediction Process**
   - Click the "Predict" button
   - Wait for the AI model to analyze your data
   - Receive instant risk assessment results

4. **📊 Results & Recommendations**
   - **Low Risk**: Green happy image with "No dangerous symptoms" message
   - **High Risk**: Red sad image with "Risk of heart disease" warning
   - Access personalized health recommendations
   - Get specific dietary and exercise advice

### **🧠 AI Model Architecture**

- **Algorithm**: Ensemble method combining multiple ML approaches
- **Training Data**: Clinical cardiovascular datasets
- **Features**: 11 critical heart disease risk factors
- **Accuracy**: Optimized for clinical relevance and user safety
- **Approach**: Conservative prediction to minimize false positives

## 🌐 Deployment Options

### **Vercel Deployment (Recommended)**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy to Vercel
vercel --prod
```

### **Docker Production**
```bash
# Build production image
docker build -t medicore:latest .

# Run with environment variables
docker run -d -p 5000:5000 \
  -e FLASK_ENV=production \
  --name medicore-app \
  medicore:latest
```

## 🔧 Configuration

### **Environment Variables**
- `FLASK_ENV`: Set to `production` for production deployment
- `FLASK_APP`: Points to `app.py`
- `PYTHONPATH`: Set to `/var/task` for Vercel deployment

### **Database**
- **Development**: SQLite database (auto-created)
- **Production**: SQLite with proper file permissions
- **Models**: SQLAlchemy ORM for data management

## 🛡️ Security Features

- **Input Validation**: All form inputs are validated
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **XSS Protection**: Jinja2 auto-escaping enabled
- **CSRF Protection**: Flask-WTF integration
- **Secure Headers**: Production-ready security headers

## 📈 Performance Optimizations

- **Static File Caching**: 1-year cache headers for static assets
- **Gzip Compression**: Enabled for all text-based files
- **Database Indexing**: Optimized queries with proper indexing
- **ML Model Caching**: Pre-loaded models for faster predictions
- **CDN Ready**: Optimized for content delivery networks

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### **Development Guidelines**
- Follow PEP 8 Python style guidelines
- Add comprehensive docstrings to functions
- Include unit tests for new features
- Update documentation for API changes

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Medical Datasets**: Cardiovascular datasets from Kaggle and medical repositories
- **ML Libraries**: Scikit-learn, TensorFlow, and XGBoost communities
- **Web Framework**: Flask community for excellent documentation
- **UI Framework**: Bootstrap for responsive design components
- **Deployment**: Vercel for seamless serverless deployment

## 📞 Support & Contact

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Documentation**: Comprehensive docs in the `/docs` directory
- **Community**: Join our discussions in GitHub Discussions

---

**⚠️ Medical Disclaimer**: This application is for educational and informational purposes only. It is not intended to replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.
