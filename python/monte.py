import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 예: 맑은 고딕 폰트를 설정
plt.rcParams['font.family'] = 'AppleGothic'

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 시뮬레이션 횟수
num_simulations = 10000

# 월별 지급 예산 (억 원)
monthly_budget = 1000

# 소비 승수 (정규분포: 평균 0.8, 표준편차 0.1)
mpc_samples = np.random.normal(loc=0.8, scale=0.1, size=num_simulations)

# 이상치 제거 (0~1.2 범위 제한)
mpc_samples = np.clip(mpc_samples, 0, 1.2)

# 월별 소비 증가액 계산
monthly_consumption_increase = monthly_budget * mpc_samples

# 시각화
plt.figure(figsize=(10, 6))
plt.hist(monthly_consumption_increase, bins=40, color='skyblue', edgecolor='black')
plt.axvline(np.mean(monthly_consumption_increase), color='red', linestyle='--', label='평균 소비 증가')

plt.title("월별 지역화폐 정책으로 인한 소비 증가 효과 (억 원 단위)", fontsize=14)
plt.xlabel("총 소비 증가액 (억 원)", fontsize=12)
plt.ylabel("시뮬레이션 횟수", fontsize=12)
plt.legend()
plt.grid(True)

# 텍스트 출력
mean_val = np.mean(monthly_consumption_increase)
upper_5 = np.percentile(monthly_consumption_increase, 95)
lower_5 = np.percentile(monthly_consumption_increase, 5)

print(f"📌 평균 소비 증가액: {mean_val:,.2f}억 원")
print(f"🔼 상위 5% 소비 증가: {upper_5:,.2f}억 원")
print(f"🔽 하위 5% 소비 증가: {lower_5:,.2f}억 원")

plt.tight_layout()
plt.show()
