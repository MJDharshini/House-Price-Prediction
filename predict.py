import joblib
import pandas as pd


# Load trained model
model = joblib.load("house_price_model.pkl")

print("================================")
print(" HOUSE PRICE PREDICTION")
print("================================")


# Get house details from user

bedrooms = float(input("Enter number of bedrooms: "))

bathrooms = float(input("Enter number of bathrooms: "))

sqft_living = float(input("Enter living area (sqft): "))

sqft_lot = float(input("Enter lot area (sqft): "))

floors = float(input("Enter number of floors: "))

waterfront = int(
    input("Waterfront? (0 = No, 1 = Yes): ")
)

view = int(
    input("View rating (0-4): ")
)

condition = int(
    input("Condition (1-5): ")
)

grade = int(
    input("Grade (1-13): ")
)

sqft_above = float(
    input("Above ground area (sqft): ")
)

sqft_basement = float(
    input("Basement area (sqft): ")
)

yr_built = int(
    input("Year built: ")
)

yr_renovated = int(
    input("Year renovated (0 if never): ")
)

zipcode = int(
    input("ZIP code: ")
)

lat = float(
    input("Latitude: ")
)

long = float(
    input("Longitude: ")
)

sqft_living15 = float(
    input("Nearby living area (sqft): ")
)

sqft_lot15 = float(
    input("Nearby lot area (sqft): ")
)


# Create input DataFrame

house = pd.DataFrame([{

    "bedrooms": bedrooms,

    "bathrooms": bathrooms,

    "sqft_living": sqft_living,

    "sqft_lot": sqft_lot,

    "floors": floors,

    "waterfront": waterfront,

    "view": view,

    "condition": condition,

    "grade": grade,

    "sqft_above": sqft_above,

    "sqft_basement": sqft_basement,

    "yr_built": yr_built,

    "yr_renovated": yr_renovated,

    "zipcode": zipcode,

    "lat": lat,

    "long": long,

    "sqft_living15": sqft_living15,

    "sqft_lot15": sqft_lot15

}])


# Predict price

prediction = model.predict(house)


print("\n================================")
print(" PREDICTED HOUSE PRICE")
print("================================")

print(f"${prediction[0]:,.2f}")   