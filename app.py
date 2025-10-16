import gradio as gr
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Inline dataset
data = pd.DataFrame({
    "sqft": [500, 750, 1000, 1250, 1500, 1750, 2000],
    "bedrooms": [1, 2, 2, 3, 3, 4, 4],
    "price": [100, 150, 200, 250, 300, 350, 400]
})

# Train model
X = data[["sqft", "bedrooms"]]
y = data["price"]
model = LinearRegression().fit(X, y)

# Prediction function
def predict_price(sqft, bedrooms):
    pred = model.predict([[sqft, bedrooms]])[0]
    return f"Estimated Price: ${pred:.2f}K"

# Gradio UI
demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Slider(300, 3000, value=1000, label="Square Footage"),
        gr.Slider(1, 5, value=3, label="Bedrooms")
    ],
    outputs="text",
    title="🏠 House Price Predictor",
    description="Enter house details to estimate price using Linear Regression"
)

if __name__ == "__main__":
    demo.launch()
