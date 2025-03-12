from transformers import BertTokenizer, BertForSequenceClassification, pipeline# tested in transformers==4.18.0
import transformers
print(transformers.__version__)

# loading model
finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)

#test
results = nlp(['growth is strong and we have plenty of liquidity.',
               'there is a shortage of capital, and we need extra financing.',
              'formulation patents might protect Vasotec to a limited extent.'])
print(results)