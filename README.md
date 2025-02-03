

# Salary Prediction Using Simple Linear Regression

This project demonstrates how to build a simple linear regression model to predict salary based on years of experience. The model is saved using the `pickle` library for future use. Additionally, a user interface (UI) is developed using HTML, CSS, and JavaScript, while the backend is powered by Django.

## Project Overview

- **Machine Learning Model:** 
  - We built a Simple Linear Regression model using scikit-learn to predict salary based on years of experience with datasets downloaded from kaggle.com
  - The trained model was serialized using `pickle` to save it for later use.
  
- **Web Interface:**
  - The front-end was developed using **HTML**, **CSS**, and **JavaScript** to create an interactive form for users to input data.
  - The backend is built with **Django** to handle requests, load the saved pickle model, and predict salary.

## Installation

To set up this project locally, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/rillhancho/salary_prediction
cd salary-prediction
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Django Server

```bash
python manage.py runserver
```

After running the server, navigate to `http://127.0.0.1:8000/` in your browser to use the salary prediction app.

## Usage

1. Input the number of years of experience in the provided text box.
2. Click the "Predict Salary" button.
3. The predicted salary will be displayed.


## Dependencies

- Django
- scikit-learn
- numpy
- pandas

## License

This project is not licensed.

---

