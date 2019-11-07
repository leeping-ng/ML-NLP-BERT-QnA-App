# Q&A App
A question and answer app based on a BERT model pre-trained from SQuAD dataset.


### How to Run the App

1. Clone BERT-SQuAD repository
```
https://github.com/leeping-ng/ML-NLP-BERT-QnA-App.git
```
2. Download pre-trained model from https://www.dropbox.com/s/8jnulb2l4v7ikir/model.zip and extract to <working_directory>. For example, the path of `bert_config.json` should be *<working_directory>/model/bert_config.json*
3. Ensure that your environment contains the packages listed in `requirements.txt`
4. Run the app with the following command
```
streamlit run app.py
```
