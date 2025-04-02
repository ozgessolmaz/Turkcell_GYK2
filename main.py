from fastapi import FastAPI
import joblib
from contextlib import asynccontextmanager
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/GYK2NorthWind"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    global session
    session = SessionLocal()
    yield
    session.close()

app = FastAPI(
    title="Product Sales Prediction API",
    description="Bu API, verilen ürün ID'sine göre tahmini satış miktarını döner.",
    version="1.0",
    lifespan=lifespan,
)

products_df = pd.read_sql("SELECT * FROM products", engine)
orders_df = pd.read_sql("SELECT * FROM orders", engine)
order_details_df = pd.read_sql("SELECT * FROM order_details", engine)

merge_df = order_details_df.merge(orders_df, on='order_id', how='left')
product_sales = merge_df.groupby('product_id')['quantity'].sum().reset_index()

product_sales = product_sales.merge(
    products_df[['product_id', 'unit_price', 'units_in_stock', 'reorder_level']],
    on='product_id',
    how='left'
)

product_sales.fillna(0, inplace=True)

X = product_sales[['product_id', 'unit_price', 'units_in_stock', 'reorder_level']]
y = product_sales['quantity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "sales_prediction_model.pkl")

y_prediction = model.predict(X_test)
mse = mean_squared_error(y_test, y_prediction, squared=False)  # RMSE hesaplama
r2 = r2_score(y_test, y_prediction)  # R2 skoru hesaplama

print(f"Root Mean Squared Error (RMSE): {mse}")
print(f"R-squared: {r2}")

class PredictionRequest(BaseModel):
    product_id: int
    unit_price: float
    units_in_stock: int
    reorder_level: int

@app.get("/")
async def root():
    return {"message": "Merhaba, bu API ürün satış tahmini yapar. /docs adresine giderek API'yi test edebilirsin."}

@app.post("/predict/", summary="Ürün satış tahmini", tags=["Prediction"])
async def predict(request: PredictionRequest):
    X_predict = np.array([[request.product_id, request.unit_price, request.units_in_stock, request.reorder_level]])
    y_predict = model.predict(X_predict)[0]
    return {
        "product_id": request.product_id,
        "predicted_quantity": float(y_predict)
    }

if __name__ == "__main__":
    app.run(debug=True)