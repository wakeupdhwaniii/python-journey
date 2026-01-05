import pandas as pd

# Series
s = pd.Series([10, 20, 30], name="scores")
print(s)

# DataFrame
df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [21, 22, 23]
})
print(df)
print(df["age"].mean())
