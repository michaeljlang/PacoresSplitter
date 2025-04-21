# PacoresSplitter

## Overview
PacoresSplitter is aimed at providing fine-tuned text segmentaion in line with the needs of the [PaCorEs research group](https://www.pacores.eu/). It is designed for the five languages that make up the PaCorEs collection of parallel corpora: Spanish (primary), English, German, Chinese, and French.

For Spanish, English, German, and French, PacoresSplitter relies on the [sentence-splitter](https://pypi.org/project/sentence-splitter/) module for an initial split. Then additional segments are created based on soft punctuation such as colons and semi-colons, as well as language-specific markers for speech such as emdashes and different types of quoation marks.

For Chinese, segmentation is carried out using code developed for [Bertalign](https://github.com/bfsujason/bertalign/tree/main) by Lei Liu & Min Zhu (2022).

## Use
PacoresSplitter can be run directly in Google Colab. 

[This notebook](https://colab.research.google.com/drive/1xQh_8_cfKSgBEl_4ccALsTv4xMbsEFys?usp=sharing) provides examples using chapters from texts in different languages. The user can also load single files.

[This notebook](https://colab.research.google.com/drive/1iWqQQE9PuiGy4MmjLfV6KSEmLMafNZqM?usp=sharing) will split a single file or a batch of files. It is only necessary specify the routes to the input and output folders (**in_dir** and **out_dir**, respectively. Output is in the form of a txt file.

**Remember to create your own copy in Drive in order to save changes.**

## Credits and Funding
PacoresSplitter was developed by Michael Lang through the PaCorEs research group at the University of Santiago de Compostela in Galicia, Spain, and funded through the following grant: **Corpus paralelos online del español PID2021-125313OB-I00. Agencia Estatal de Investigación.**
