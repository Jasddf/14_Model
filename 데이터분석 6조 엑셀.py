import random
import pandas as pd
from datetime import datetime, timedelta

# 각 유해가스의 농도 범위 설정 (단위: ppm 또는 %)
RANGES = {
    'Hydrocarbons': (0, 100),  # 탄화수소 농도 범위
    'Oxygen': (19.0, 23.0),     # 산소 농도 범위 (%)
    'Carbon Dioxide': (0, 5000),# 이산화탄소 농도 범위 (ppm)
    'Carbon Monoxide': (0, 1000),# 일산화탄소 농도 범위 (ppm)
    'Hydrogen Sulfide': (0, 100) # 황화수소 농도 범위 (ppm)
}

# 측정 시작 시간 및 종료 시간 설정
start_time = datetime.now()
end_time = start_time + timedelta(hours=5)

# 5분 간격의 시간 생성
time_intervals = []
current_time = start_time

while current_time <= end_time:
    time_intervals.append(current_time)
    current_time += timedelta(minutes=5)

# 임의의 유해가스 농도 값을 생성
data = {
    'Timestamp': time_intervals
}

# 각 가스에 대해 임의의 농도 값을 생성
for gas, (min_val, max_val) in RANGES.items():
    data[gas] = [random.uniform(min_val, max_val) for _ in time_intervals]

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터 출력 또는 CSV 파일로 저장
print(df)
df.to_csv('./6조/gas_concentration_measurements.csv', index=False)
