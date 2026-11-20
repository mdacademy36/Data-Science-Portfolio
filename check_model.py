
import joblib
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parent / "model"

model = joblib.load(MODEL_DIR / "rf_model.pkl")
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
imputer = joblib.load(MODEL_DIR / "imputer.pkl")

print("=== MODEL CHECK ===")
print("Model:", type(model).__name__)
print("Jumlah fitur model:", len(model.feature_names_in_))

print("\n=== FEATURE COLUMNS ===")
print("Jumlah feature columns:", len(feature_columns))
print("Sama dengan fitur model:",
      list(model.feature_names_in_) == list(feature_columns))

print("\n=== IMPUTER ===")
print("Fitur imputer:", list(imputer.feature_names_in_))

print("\n=== SCALER ===")
print("Fitur scaler:", list(scaler.feature_names_in_))
