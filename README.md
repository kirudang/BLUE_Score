# Comparison of NLTK's BLEU and SacreBLEU

## Overview
This repository contains implementations and examples of using both NLTK's BLEU score and SacreBLEU for evaluating machine translation quality. 

## Introduction to BLEU
BLEU (Bilingual Evaluation Understudy) is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another. Quality is considered to be the correspondence between a machine's output and that of a human: "the closer a machine translation is to a professional human translation, the better it is" – this is the central idea behind BLEU.

## NLTK's BLEU Score
[NLTK (Natural Language Toolkit)](https://www.nltk.org/) provides a BLEU score implementation that is widely used in academic and research settings for the purpose of benchmarking machine translation algorithms against human translations.

### Key Features:
- Implements standard BLEU scoring as initially proposed.
- Flexible with various customization options including different n-gram lengths.
- Primarily used in educational and experimental applications.

## SacreBLEU
[SacreBLEU](https://github.com/mjpost/sacrebleu) provides a standard BLEU score implementation that aims to provide comparable and reproducible BLEU scores across different studies and papers.

### Key Features:
- Offers a standardized version of BLEU scoring to ensure consistency across studies.
- Automatically handles pre-processing like tokenization, which makes it more robust and reliable for consistent evaluation.
- Introduced enhancements such as smoothing techniques and support for multiple reference translations.

**Note**: Use this to assess outputs from LLMs, where tokenizers are leveraged. 

## Differences Between NLTK's BLEU and SacreBLEU
The key differences between NLTK's BLEU score and SacreBLEU can be summarized in terms of their design goals, usage, and output consistency:

1. **Standardization**: SacreBLEU aims for standardized scores that facilitate comparison across different research works, while NLTK's BLEU is more flexible and configurable.
2. **Pre-processing**: SacreBLEU handles pre-processing internally to ensure consistency, unlike NLTK which requires manual pre-processing.
3. **Reproducibility**: SacreBLEU scores are reproducible given the same datasets and settings, making it preferred for scientific publications where reproducibility is crucial.
4. **Use Cases**: NLTK is generally more suited for educational purposes and initial experiments, whereas SacreBLEU is used in research of LLMs.

## Contributing
Guidelines for how to contribute to this repository.

## License
Specify the license under which this code is shared.

## References
- [NLTK Documentation](https://www.nltk.org/)
- [SacreBLEU Repository](https://github.com/mjpost/sacrebleu)

Feel free to explore each implementation and contribute to enhancing the tools!
