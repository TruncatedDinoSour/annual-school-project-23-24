import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

df = pd.read_csv("a.csv")

text = " ".join(map(str, df["Kaip jautiesi šiandien?"])).replace("nan", "")
text1 = " ".join(map(str, df["Ką darai dėl savo emocinės gerovės?"])).replace("nan", "")

# Load your mask image (circle.png)
circle_mask = np.array(Image.open("circle.png"))

# Initialize the WordCloud object
wc = WordCloud(background_color=None, mode="RGBA", max_words=1000, mask=circle_mask, colormap='Paired')

# Generate a wordcloud
wc.generate(text)


# Plot function
def plot_cloud(wc):
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")


# Plot the wordcloud
plot_cloud(wc)

# Save the image in the img folder:
wc.to_file("a.png")


# Initialize the WordCloud object
wc = WordCloud(background_color=None, mode="RGBA", max_words=1000, mask=circle_mask, colormap='Paired')

# Generate a wordcloud
wc.generate(text1)


# Plot function
def plot_cloud(wc):
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")


# Plot the wordcloud
plot_cloud(wc)

# Save the image in the img folder:
wc.to_file("b.png")
