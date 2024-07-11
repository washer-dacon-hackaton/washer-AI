#사용자가 쓴 글을 doc로 변환해 데이터 입력 받음
#doc에서 키워드를 추출

!pip install keybert

from keybert import KeyBERT
from collections import Counter
from transformers import BertTokenizer, BertModel
from sklearn.cluster import KMeans
import torch

# BERT 토크나이저와 모델 초기화
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
bert_model = BertModel.from_pretrained('bert-base-multilingual-cased')

# BERT 임베딩 계산 함수 정의
def calculate_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
        pooled_output = outputs.pooler_output  # [CLS] 토큰의 임베딩
    return pooled_output.numpy().flatten()

# 행복 지수 계산 함수 정의
def calculate_happiness_score(doc):
    # KeyBERT를 사용하여 문서에서 키워드 추출
    kw_model = KeyBERT()
    keywords_with_scores = kw_model.extract_keywords(doc)

    # 추출된 키워드와 점수들을 리스트로 변환
    keyword_list = [keyword for keyword, score in keywords_with_scores]

    # 각 키워드에 대한 BERT 임베딩 계산
    embeddings = [calculate_embedding(keyword) for keyword in keyword_list]

    # K-means 클러스터링을 사용하여 키워드를 'P', 'E', 'H' 카테고리로 분류
    kmeans = KMeans(n_clusters=3, random_state=42)
    cluster_labels = kmeans.fit_predict(embeddings)

    classified_categories = []

    # 클러스터 레이블에 따라 카테고리 지정
    for keyword, cluster_label in zip(keyword_list, cluster_labels):
        if cluster_label == 0:
            category = 'P'  # Positive (긍정적)
        elif cluster_label == 1:
            category = 'E'  # Educational (교육적)
        else:
            category = 'H'  # Health-related (건강적)

        classified_categories.append(category)

    # 각 카테고리 별 개수 계산
    category_counts = Counter(classified_categories)

    # 행복 지수 계산
    count_P = category_counts.get('P', 0)
    count_E = category_counts.get('E', 0)
    count_H = category_counts.get('H', 0)

    result = count_P + (5 * count_E) + (3 * count_H)

    return result

# 주어진 문서
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

# 행복 지수 계산
happiness_score = calculate_happiness_score(doc)
print(happiness_score)

[짧은 코멘트 함수3]
def get_happiness_message(happiness_score):
    if happiness_score <= 15:
        return "내일 더 행복하시길 바랍니다"
    elif happiness_score <= 30:
        return "오늘 꽤 행복한 하루를 보내셨군요!"
    else:
        return "당신은 오늘 행복한 사람입니다"

happiness_message = get_happiness_message(happiness_score)
print(happiness_message)
