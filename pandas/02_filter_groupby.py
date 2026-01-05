import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "dept": ["CS", "EE", "CS", "ME"],
    "score": [88, 92, 75, 90]
})

# filter
cs_df = df[df["dept"] == "CS"]
print(cs_df)

# groupby
dept_avg = df.groupby("dept")["score"].mean().sort_values(ascending=False)
print(dept_avg)
