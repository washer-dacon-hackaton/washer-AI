#사용자가 쓴 글을 doc로 변환해 데이터 입력 받음
#doc에서 키워드를 추출

!pip install keybert

from keybert import KeyBERT

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal). 
         A supervised learning algorithm analyzes the training data and produces an inferred function, 
         which can be used for mapping new examples. An optimal scenario will allow for the 
         algorithm to correctly determine the class labels for unseen instances. This requires 
         the learning algorithm to generalize from the training data to unseen situations in a 
         'reasonable' way (see inductive bias).
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)

print(keywords)

## 키워드만 추출
keyword_list = [keyword for keyword, score in keywords]

## 결과 출력
print(keyword_list)

# 키워드들을 인생관, 건강, 야망으로 분류하기 위해 키워드와 분류키워드간의 유사성을 계산 → bert 임베딩
import torch
from transformers import BertModel, BertTokenizer
import numpy as np
from sklearn.cluster import KMeans

## 키워드 리스트
keyword_list = ['supervised', 'labeled', 'learning', 'training', 'labels']

## BERT 모델 및 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

## 임베딩 계산 함수 정의
def calculate_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
        pooled_output = outputs.pooler_output  # [CLS] 토큰의 임베딩
    return pooled_output.numpy().flatten()

## 각 키워드에 대응하는 카테고리 -> 있어도되고 없어도
 category_mapping = {
    'supervised': 'H',   # higher order
    'labeled': 'H',      # higher order
    'learning': 'H',     # higher order
    'training': 'H',     # higher order
    'labels': 'E'        # existence
}

## 각 키워드에 대해 임베딩 벡터 계산
embeddings = [calculate_embedding(keyword) for keyword in keyword_list]

## K-means 클러스터링을 사용하여 분류
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans.fit_predict(embeddings)

classified_categories = []

## 각 키워드의 예측된 카테고리 출력
for keyword, cluster_label in zip(keyword_list, cluster_labels):
    if cluster_label == 0:
        category = 'P'
    elif cluster_label == 1:
        category = 'E'
    else:
        category = 'H'
    classified_categories.append(category)
    print(f'{keyword}: Predicted Category - {category}')

## classified_categories 출력
print("classified_categories:", classified_categories)
