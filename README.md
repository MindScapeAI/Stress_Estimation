# Stress_Estimation
### ETRI 휴먼이해 경진대회 참여

## 연구 목적
라이프로그 데이터를 기반으로 XAI를 활용한 개인 맞춤형 스트레스 요인 분석을 위한 연구이다.

## 실험 요약
- Kendall 상관 분석을 이용하여 스트레스와 관련된 변수를 추출하고 스트레스 지수를 3단계로 분류하였다.
- Logistic Regression(LR), Support Vector Machin(SVM), Decision Tree(DT), XGBoost(XGB)의 머신러닝 기반의 모델을 이용해 스트레스 지수를 예측하였다. 
- 여러 평가지수를 이용하여 가장 적합한 모델을 선정 후, 해당 모델을 이용해 개인별 스트레스 지수를 예측하였다. 
- XAI 기법(SHAP, f score)를 통해 개인별의 스트레스 예측 결과와 스트레스 요인을 분석하였으며 개인별로 스트레스 예측 결과에 영향을 주는 특성이 다르다는 것을 확인하였다.

## 연구 기대 효과
본 연구는 개인의 특성에 따라 스트레스를 분석할 수 있는 개인별 맞춤형 모델 연구에 기여할 것으로 기대된다.


### <코드>
preprocess_data.py : 라이프로그 데이터 전처리 방법
StressEstimation_2020users.ipynb : 2020년에 수집한 22명의 피실험자들의 라이프로그 데이터를 활용한 실험.
StressEstimation_fewusers.ipynb : 임의로 3명의 피실험자들의 데이터를 각각 활용해 개인별로 스트레스를 예측하고 그 결과를 분석한 실험. 

- 코드 실행 방법
sleep_survey = '../Data/user_survey_2020.csv'
sleep_data = '../Data/user_sleep_2020.csv'
dir2020_path = '../Data/2020_user'

✅ 필요 패키지 및 버전 설정

|package|version|
|------|---|
|python|3.9.16|
|xlwt|1.3.0|
|shap|0.41.0| 
|slicer|0.0.7|
|cloudpickle|2.2.1| 
|joblib|1.2.0| 
|llvmlite|0.39.1| 
|numba|0.56.4| 
|numpy|1.23.5| 
|pandas|2.0.0| 
|pytz|2023.3| 
|scikit-learn|1.2.2| 
|scipy|1.10.1| 
|threadpoolctl|3.1.0| 
|tqdm|4.65.0| 
|tzdata|2023.3|
|et-xmlfile|1.1.0| 
|openpyxl|3.1.2|
|matplotlib|3.7.1| 
|pillow|9.5.0| 
|pyparsing|3.0.9|
|imbalanced-learn|0.10.1| 
|imblearn|0.0|
|xgboost|1.7.5|
|seaborn|0.12.2|
