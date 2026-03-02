import pandas as pd

df = pd.read_csv("movies_dataset.csv")

print("MOVIES DATASET ANALYSIS")
print("-" * 40)

print("\nAll Movies:")
print(df[["title", "genre", "year", "rating"]])

print("\nTotal Movies:", len(df))

print("\nHighest Rated Movie:")
print(df.loc[df["rating"].idxmax(), ["title", "rating"]])

print("\nLowest Rated Movie:")
print(df.loc[df["rating"].idxmin(), ["title", "rating"]])

print("\nAverage Rating:", round(df["rating"].mean(), 2))

print("\nMovies by Genre:")
print(df["genre"].value_counts())

print("\nTop 5 Highest Rated Movies:")
print(df.nlargest(5, "rating")[["title", "rating", "year"]])

print("\nMovies After 2015:")
print(df[df["year"] > 2015][["title", "year", "rating"]])

print("\nHighest Box Office Movie:")
print(df.loc[df["box_office_million"].idxmax(), ["title", "box_office_million"]])

print("\nAction Movies:")
print(df[df["genre"] == "Action"][["title", "year", "rating"]])