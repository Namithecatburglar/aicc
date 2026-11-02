# import streamlit as st 
# import joblib

# model = joblib.load("iris_model.pkl") 
# st.title("Iris Flower Prediction")
# sl = st.number_input("Sepal Length")
# sw = st.number_input("Sepal Width")

# pl = st.number_input("Petal Length")

# pw = st.number_input("Petal Width") 

# if st.button("Predict"):
#     pred = model.predict([[sl, sw, pl, pw]])
#     flowers = ["Setosa", "Versicolor", "Virginica"]
#     st.success(flowers[pred[0]])






import streamlit as st
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

model = joblib.load("iris_model.pkl")
iris = load_iris()

X = iris.data
y = iris.target

st.title("Iris Flower Prediction")

sl = st.number_input("Sepal Length", value=6.0, step=0.1)
sw = st.number_input("Sepal Width", value=3.0, step=0.1)
pl = st.number_input("Petal Length", value=4.0, step=0.1)
pw = st.number_input("Petal Width", value=1.0, step=0.1)

if st.button("Predict"):
    pred = model.predict([[sl, sw, pl, pw]])[0]
    flowers = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"Predicted Flower: {flowers[pred]}")

    # Train regression line using the Iris dataset
    reg_model = LinearRegression()
    reg_model.fit(X[:, [0]], X[:, 2])

    x_line = np.linspace(
        X[:, 0].min(), X[:, 0].max(), 100
    ).reshape(-1, 1)

    y_line = reg_model.predict(x_line)

    # Create graph
    fig, ax = plt.subplots()

    ax.scatter(
        X[:, 0], X[:, 2],
        color="steelblue",
        label="Actual Iris Data"
    )

    ax.plot(
        x_line, y_line,
        color="orange",
        label="Regression Line"
    )

    # Plot the user's input as a red point
    ax.scatter(
        sl, pl,
        color="red",
        s=150,
        label=f"Prediction: {flowers[pred]}",
        zorder=5
    )

    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Petal Length")
    ax.set_title("Iris Prediction Graph")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)