import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기 (cp949 인코딩)
df = pd.read_csv("연도별예산서.csv", encoding='cp949')

# 2025년 기준, 사회복지 예산 항목 중 일부 추출 (기초생활보장, 취약계층지원 등)
labels = df['Unnamed: 0'][3:5]  # 항목명
values = df['2025'][3:5].str.replace(',', '').astype(int)  # 예산액

# 파이그래프 시각화
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, counterclock=False)
plt.title('2025년 사회복지 예산 구성 비율')
plt.axis('equal')  # 원형 비율 유지
plt.show()