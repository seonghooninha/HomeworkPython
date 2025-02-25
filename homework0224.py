# from sklearn.linear_model import LinearRegression # 선형 회귀 모델
# import tglearn as tg # tglearn이라는 커스텀 라이브러리를 tg라는 이름으로 사용
# from tglearn import LinearRegression # tglearn에서 선형 회귀 모델 가져옴
from tglearn import KNeighborsRegressor # tglearn에서 k-최근접 이웃 회귀 모델 가져옴
# from sklearn.neighbors import KNeighborsRegressor # sklearn의 k-이웃을 가져오려 함
import pandas as pd # 데이터를 불러오기 위해 pandas
import matplotlib.pyplot as plt # 데이터를 시각화하기 위해 matplotlib

# 인터넷에서 lifesat.csv 파일을 불러와서 pandas 데이터프레임(ls)으로 저장
ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = ls[["GDP per capita (USD)"]].values # gdp를 x에 numpy 배열로 변환
y = ls[["Life satisfaction"]].values # 삶의 만족도를 y에 numpy 배열로 변환

# x와 y의 관계를 산점도(scatter plot)로 그려서 데이터의 분포를 확인
ls.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 62500, 4, 9]) # 그래프의 축 범위 설정
plt.show() # 그래프 출력
#model = LinearRegression() # 선형 회귀 모델 생성
model = KNeighborsRegressor(3) # 최근접 이웃 회귀 모델을 생성, 이웃 3명
model.fit(X, y) # knn 모델을 학습

X_new = [[31721.3]]  # ROK 2020 # x에 새로운 값 입력
print(model.predict(X_new)) # 새로운 값에 대한 예상치를 출력
# LinearRegression 5.90
# KNeighborsRegressor 5.70

