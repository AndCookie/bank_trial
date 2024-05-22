import json
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))

# 더미 데이터 생성
dummy_data = []

# user_id와 deposit_id를 1부터 10000까지와 1부터 37까지의 값으로 설정하여 더미 데이터 생성
for user_id in range(1, 10001):
    num_deposits = random.randint(1, 5)  # 각 사용자에게 연결할 금융 상품의 수를 1부터 5까지 랜덤하게 선택
    user_deposits = random.sample(range(1, 38), num_deposits)  # 1부터 37까지의 숫자 중에서 num_deposits 개만큼 랜덤하게 선택
    for deposit_id in user_deposits:
        dummy_data.append({
            "model": "accounts.user_deposit", 
            "fields": {
                "user": user_id,
                "deposit": deposit_id
            }
        })

# JSON 파일로 덤프
save_path = os.path.join(current_dir, 'accounts/fixtures/accounts/user_deposits.json')
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(dummy_data, f, indent=4)
