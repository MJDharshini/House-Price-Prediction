import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("dataset/kc_house_data.csv")

print("Dataset loaded successfully!")
print("Total records:", len(data))


# ==========================================
# 2. SELECT FEATURES
# ==========================================

features = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "grade",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
    "zipcode",
    "lat",
    "long",
    "sqft_living15",
    "sqft_lot15"
]

X = data[features]

# Target variable
y = data["price"]


# ==========================================
# 3. SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 4. CREATE MACHINE LEARNING MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# 5. TRAIN MODEL
# ==========================================

print("\nTraining the model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# 6. PREDICTION
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 7. MODEL EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)


print("\n================================")
print("MODEL PERFORMANCE")
print("================================")

print("MAE :", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)


# ==========================================
# 8. SAVE MODEL
# ==========================================

joblib.dump(model, "house_price_model.pkl")

print("\nModel saved successfully!")
print("Saved file: house_price_model.pkl")  