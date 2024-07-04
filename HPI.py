#행복지수 구하기
from collections import Counter

## 카테고리 별 개수 세기
category_counts = Counter(classified_categories)

## P, E, H의 개수 가져오기
count_P = category_counts.get('P', 0)
count_E = category_counts.get('E', 0)
count_H = category_counts.get('H', 0)

## 결과값 계산
result = count_P + (5 * count_E) + (3 * count_H)

print(f"당신의 행복지수는 만점 45점 만점에 : {result} 점입니다")

if result <= 15:
    print("내일 더 행복하시길 바랍니다")
elif result <= 30:
    print("오늘 꽤 행복한 하루를 보내셨군요!")
else:
    print("당신은 오늘 행복한 사람입니다")
