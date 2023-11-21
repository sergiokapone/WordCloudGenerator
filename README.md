# WordCloud Generator

This script generates a word cloud from a given text file. The generated word cloud can be customized based on frequency distribution, and it supports multiple languages for morphological analysis.

## Features

- Tokenizes and preprocesses text data.
- Utilizes a morphological analyzer for lemmatization.
- Generates a word cloud from the lemmatized tokens.
- Supports different languages for analysis (default is English).
- Allows customization of output file path and display options.

## Usage

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the script with the desired parameters:
bash
```
python generate_wordcloud.py input_file.txt --lang en --output output_wordcloud.png --show
```

- `input_file.txt`: Path to the text file for word cloud generation.
- `--lang`: Language for morphological analysis (default is 'en').
- `--output`: Output path for the generated word cloud image.
- `--show`: Display the generated word cloud on the screen instead of saving it to a file.

## Dependencies

- nltk
- requests
- wordcloud
- matplotlib
- pymorphy3

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

## Acknowledgments
Ukrainian stop words provided by [skupriienko](https://raw.githubusercontent.com/skupriienko/Ukrainian-Stopwords/master)
WordCloud library: https://github.com/amueller/word_cloud.
pymorphy3 library: https://github.com/kmike/pymorphy2.

Feel free to customize this template according to your specific project details. Let me know if you have any further requests or modifications.
