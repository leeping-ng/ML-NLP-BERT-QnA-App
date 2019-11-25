# Q&A App
A question and answer app built on a BERT model pre-trained from SQuAD dataset.


### How to Run the App

1. Open a terminal
```
cd <working_directory>
```
2. Clone this repository
```
git clone https://github.com/leeping-ng/ML-NLP-BERT-QnA-App.git
```
3. Download pre-trained model from https://www.dropbox.com/s/8jnulb2l4v7ikir/model.zip and extract to *<working_directory>*. For example, the path of `bert_config.json` should be *<working_directory>/model/bert_config.json*
4. Ensure that your environment contains the packages listed in `requirements.txt`
5. Run the app with the following command
```
streamlit run app.py
```

### App Interface

The following screenshot from the app shows a Q&A about a wiki page for the movie Pulp Fiction.

<img src='/img/TLDR.png'>
