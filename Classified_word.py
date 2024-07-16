## 원본 감정 단어 액셀 파일에서 라벨링이 어려운 감정 범주 제거 후 저장
import pandas as pd
from google.colab import drive

# Mount Google Drive (if not already mounted)
drive.mount('/content/drive')

# 엑셀 파일 경로 - Verify this path is correct!
file_path = '/content/drive/MyDrive/감정단어사전0603.xlsx'  # Adjust 'MyDrive' if needed

# 엑셀 파일 로드
df = pd.read_excel(file_path, sheet_name='Sheet1')

# '감정 범주' 열에서 '중성', '기타', '놀람' 값을 가지는 행 제거
filtered_df = df[~df['감정범주'].isin(['중성', '기타', '놀람'])]

# 필터링된 데이터프레임을 새로운 엑셀 파일로 저장
# CHANGED: 'Mydrive' to 'MyDrive'
filtered_file_path = '/content/drive/MyDrive/filtered_감정단어사전0603.xlsx' 
filtered_df.to_excel(filtered_file_path, index=False)

print(f"필터링된 파일이 '{filtered_file_path}'에 저장되었습니다.")

## 중복 없이 감정 범주 값 출력
unique_emotions = filtered_df['감정범주'].unique()
print(unique_emotions)

## 각 감정 범주에 해당하는 단어들 추출 및 출력
emotions = ['혐오', '슬픔', '기쁨', '흥미', '분노', '지루함', '공포', '통증']
emotion_word_dict = {}

for emotion in emotions:
    emotion_words = filtered_df[filtered_df['감정범주'] == emotion]['단어'].tolist()
    emotion_word_dict[emotion] = emotion_words
    print(f"{emotion} 감정 범주에 속한 단어들:")
    print(emotion_words)
    print("\n")

## '부정'과 '긍정'으로 분류할 감정 범주들
negative_emotions = ['혐오', '슬픔', '분노', '지루함', '공포', '통증']
positive_emotions = ['기쁨', '흥미']

# 부정 감정 범주에 속한 단어들 추출
negative_words = filtered_df[filtered_df['감정범주'].isin(negative_emotions)]['단어'].tolist()

# 긍정 감정 범주에 속한 단어들 추출
positive_words = filtered_df[filtered_df['감정범주'].isin(positive_emotions)]['단어'].tolist()

# 결과 출력
print("부정 감정 범주에 속한 단어들:")
print(negative_words)
print("\n")
print("긍정 감정 범주에 속한 단어들:")
print(positive_words)

## 추출된 감정 범주와 단어들을 리스트화한 후 액셀 파일로 저장
# 구글 드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')

# 필요한 라이브러리 임포트
import pandas as pd

# 엑셀 파일 경로
output_file_path = '/content/drive/MyDrive/감정단어_부정긍정.xlsx'  # 저장할 경로와 파일명 설정

# 엑셀 파일로 저장할 데이터 준비
# '부정' 감정 범주에 속하는 단어들 추출
negative_words_df = filtered_df[filtered_df['감정범주'].isin(negative_emotions)]
negative_words_df = negative_words_df.sort_values(by='빈도', ascending=False).head(20)

# '긍정' 감정 범주에 속하는 단어들 추출
positive_words_df = filtered_df[filtered_df['감정범주'].isin(positive_emotions)]
positive_words_df = positive_words_df.sort_values(by='빈도', ascending=False).head(20)

# 데이터 프레임 생성
df_to_save = pd.DataFrame({
    '단어': negative_words_df['단어'].tolist() + positive_words_df['단어'].tolist(),
    '감정범주': (['부정'] * len(negative_words_df)) + (['긍정'] * len(positive_words_df))
})

# 엑셀 파일로 저장
df_to_save.to_excel(output_file_path, index=False)

print(f"엑셀 파일이 저장되었습니다: {output_file_path}")
