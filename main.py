import os
import argparse
import requests
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pymorphy3 import MorphAnalyzer


stop_words = set(stopwords.words("ukrainian"))


def download_stopwords():
    # Перевіряємо наявність папки corpora/stopwords у каталозі nltk_data
    nltk_data_path = nltk.data.path[0]
    stopwords_path = os.path.join(nltk_data_path, "corpora", "stopwords")
    if not os.path.exists(stopwords_path):
        os.makedirs(stopwords_path)

    # Завантажуємо стоп-слова для української мови та зберігаємо у файл
    url = "https://raw.githubusercontent.com/skupriienko/Ukrainian-Stopwords/master/stopwords_ua.txt"
    r = requests.get(url)

    with open(os.path.join(stopwords_path, "ukrainian"), "wb") as f:
        f.write(r.content)


def read_text_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None


def preprocess_text(text, stop_words):
    tokens = word_tokenize(text)

    # Фільтрація токенів
    filtered_tokens = [
        word.lower()
        for word in tokens
        if word.lower() not in stop_words and word.isalnum()
    ]

    return filtered_tokens


def lemmatize_tokens(tokens, morph):
    # Лематизація слів
    lemmatized_tokens = [morph.parse(token)[0].normal_form for token in tokens]
    return lemmatized_tokens


def generate_wordcloud(freq_dist, output_file, show_image=False):
    # Створення хмари слів
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=100,
        colormap="viridis",
    ).generate_from_frequencies(freq_dist)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)

    if show_image:
        plt.show()
    else:
        plt.savefig(output_file)


def generate_wordcloud_from_file(input_file, output_file, lang="en", show_image=False):
    match lang:
        case "uk":
            download_stopwords()
            lang_wide = "ukrainian"
        case "ru":
            lang_wide = "russian"
        case _:
            lang_wide = "english"

    stop_words = set(stopwords.words(lang_wide))

    morph = MorphAnalyzer(lang=lang)

    text = read_text_from_file(input_file)

    if text:
        filtered_tokens = preprocess_text(text, stop_words)
        lemmatized_tokens = lemmatize_tokens(filtered_tokens, morph)
        freq_dist = FreqDist(lemmatized_tokens)

        generate_wordcloud(freq_dist, output_file, show_image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate WordCloud from text file.")

    parser.add_argument(
        "file", type=str, help="Path to the text file for WordCloud generation."
    )
    parser.add_argument(
        "--lang",
        "-l",
        type=str,
        default="en",
        help="Language for morphological analysis (default is 'en').",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="wordcloud.png",
        help="Output path for the generated WordCloud image.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        default=True,
        help="Display the generated WordCloud on the screen instead of saving it to a file.",
    )

    args = parser.parse_args()

    generate_wordcloud_from_file(args.file, args.output, args.lang, args.show)
