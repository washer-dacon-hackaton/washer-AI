from keybert import KeyBERT
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

doc = """
         흥미상실했어. 지속적인 슬픔이 느껴져. 오늘 입맛이 없고 피로감이 커. 즐거움을 느꼈고 설렘이 가득해.
      """

# KeyBERT 모델로부터 키워드 추출
kw_model = KeyBERT()
keywords_with_scores = kw_model.extract_keywords(doc)

# 추출된 키워드 리스트
keyword_list = [keyword for keyword, score in keywords_with_scores]

# 감정/상태에 따른 분류 매핑
emotion_mapping = {
    '지속적인 슬픔': '-',
    '흥미상실': '-',
    '절망감': '-',
    '무기력감': '-',
    '죄책감': '-',
    '잠이 안와': '-',
    '입맛이 없어': '-',
    '피로감': '-',
    '신체통증': '-',
    '집중력저하': '-',
    '기억력 문제': '-',
    '부정적사고': '-',
    '사회적활동 감소': '-',
    '일상 업무가 어려움': '-',
    '위험행동 증가': '-',
    '자살생각': '-',
    '뿌듯함': '+',
    '성취감': '+',
    '만족감': '+',
    '즐거움': '+',
    '편안함': '+',
    '차분함': '+',
    '신남': '+',
    '설렘': '+',
    '기대': '+',
    '사랑': '+',
    '맛있음': '+',
    '개운함': '+',
    '시원함': '+',
    '따듯함': '+',
    '포근함': '+',
    '멋있음': '+'
}

# "-"와 "+"의 개수 카운트
count_minus = sum(1 for keyword in keyword_list if emotion_mapping.get(keyword, '') == '-')
count_plus = sum(1 for keyword in keyword_list if emotion_mapping.get(keyword, '') == '+')

# 색상 설정
colors_minus = ['lightcoral', 'indianred'] if count_minus >= 5 else ['lightgray', 'dimgray']
colors_plus = ['lightgreen', 'forestgreen'] if count_plus >= 5 else ['lightgray', 'dimgray']

# 원 그래프 설정
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# "-" 그래프 설정
ax1.pie([count_minus, len(keyword_list) - count_minus], labels=['-', '+'], colors=colors_minus, autopct='%1.1f%%', startangle=140)
ax1.set_title('Cluster 0 (-)')

# "+" 그래프 설정
ax2.pie([count_plus, len(keyword_list) - count_plus], labels=['-', '+'], colors=colors_plus, autopct='%1.1f%%', startangle=140)
ax2.set_title('Cluster 1 (+)')

plt.tight_layout()
plt.show()
