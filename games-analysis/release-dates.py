import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-release-dates.csv")

# Clean up fields
df ["first_release_date"] = pd.to_datetime(df["first_release_date"])

# Analyza data
plt.scatter(df["first_release_date"], df["critic_rating_value"], color = "blue", label = "Critic Rating")
plt.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "User Rating")

plt.legend(loc = "upper left")

plt.show()