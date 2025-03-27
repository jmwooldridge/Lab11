# Print the original input values
st.write(f"Original input values: {input_data}")

# Print the scaled values
scaled_values = scaler.transform(input_data[numerical_features])
st.write(f"Scaled values: {scaled_values}")

# Predict load capacity
prediction = model.predict(input_data)

st.write(f"Predicted Load Capacity: {prediction[0][0]}")
