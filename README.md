# Translation Project

This project focuses on translating Arabizi (Tunisian dialect written in Latin script) to English using a custom fine-tuned model.

## Project Overview

The model was fine-tuned on a dataset specifically curated for translating Arabizi to English. This dataset contains about 1300 lines of text, with columns for Arabizi (`tounsi`) and the corresponding English translation (`english`).

## Example Translation

![Screenshot of Translation](captures/Screenshot%202024-08-25%20122149.png)

The above screenshot shows the model in action, translating a sample sentence from Arabizi to English.


## Links

### Dataset
The dataset used for fine-tuning can be found [here](https://huggingface.co/datasets/IbrahimAL24/TNtoEng-By-Ibrahim-V1-Dataset).

### Fine-Tuned Model
The fine-tuned model repository can be accessed [here](https://huggingface.co/IbrahimAL24/TNtoEng-By-Ibrahim-V1).

## How to Use


## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/IbrahimAL22/translation_project.git


2. Enter to project directory and run Django server:
   ```bash
   cd translation_project
   python manage.py runserver


