def analyze_emotions_using_words_df(user_input, negative_words_df, positive_words_df):
    # 사용자 입력을 리스트로 변환
    selected_emotions = [emotion.strip() for emotion in user_input.split(',')]

    # 각 키워드의 긍정/부정 여부 확인 및 개수 세기
    negative_emotions = negative_words_df['단어'].tolist()
    positive_emotions = positive_words_df['단어'].tolist()

    num_negative_selected = sum(1 for emotion in selected_emotions if emotion in negative_emotions)
    num_positive_selected = sum(1 for emotion in selected_emotions if emotion in positive_emotions)

    # 각 키워드의 긍정/부정 여부 출력
    print("\n각 키워드의 긍정/부정 여부:")
    for emotion in selected_emotions:
        if emotion in negative_emotions:
            print(f"{emotion}: 부정")
        elif emotion in positive_emotions:
            print(f"{emotion}: 긍정")
        else:
            print(f"{emotion}: 해당하는 감정 키워드가 없습니다.")

    # 사용자가 고른 키워드 개수 출력
    total_selected = len(selected_emotions)
    total_negative_ratio = (num_negative_selected / total_selected) * 100 if total_selected > 0 else 0
    total_positive_ratio = (num_positive_selected / total_selected) * 100 if total_selected > 0 else 0

    # 최종 점수 계산
    overall_score = (total_positive_ratio - total_negative_ratio + 100) / 2

    print(f"\n내가 입력한 키워드 개수: {total_selected}개")
    print(f"사용자가 고른 긍정 감정 키워드 개수: {num_positive_selected}개")
    print(f"사용자가 고른 부정 감정 키워드 개수: {num_negative_selected}개")
    print(f"사용자가 고른 키워드 중 부정 비율: {total_negative_ratio:.2f} %")
    print(f"사용자가 고른 키워드 중 긍정 비율: {total_positive_ratio:.2f} %")
    print(f"전체 감정 점수: {overall_score:.2f} % (0%: 가장 부정적, 100%: 가장 긍정적)")

    return overall_score
def score_to_color(score):
    """
    Converts a score (0 to 100) to a grayscale color.
    0% -> black (0, 0, 0)
    100% -> white (255, 255, 255)
    """
    gray_value = int((score / 100) * 255)
    return (gray_value, gray_value, gray_value)

def visualize_color(color):
    """
    Visualizes the color using matplotlib.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    # Create an image with the given color
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:, :] = color

    # Display the image
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# 사용자에게 입력 받기
user_input = input("선택할 감정 키워드를 입력하세요. (예: 울다, 울상, 기쁘다, 뿌듯하다): ")

# 함수 호출
overall_score = analyze_emotions_using_words_df(user_input, negative_words_df, positive_words_df)

# 색상 변환 및 시각화
color = score_to_color(overall_score)
visualize_color(color)
