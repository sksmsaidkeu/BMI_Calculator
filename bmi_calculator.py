def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("0보다 큰 값을 입력해주세요.")
                continue
            return value
        except ValueError:
            print("숫자만 입력해주세요.")


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    elif bmi < 30:
        return "비만"
    else:
        return "고도비만"


ADVICE = {
    "저체중": [
        "1. 하루 세 끼를 규칙적으로 챙겨 먹는다.",
        "2. 단백질(계란, 고기, 콩류)과 건강한 지방 섭취를 늘린다.",
        "3. 근력 운동을 병행해 체중을 근육으로 늘린다.",
        "4. 체중이 계속 늘지 않으면 병원에서 원인을 확인한다.",
    ],
    "정상": [
        "1. 현재의 식습관과 운동 습관을 꾸준히 유지한다.",
        "2. 주 3회 이상 규칙적인 운동을 지속한다.",
        "3. 균형 잡힌 식단과 충분한 수면을 유지한다.",
        "4. 정기적인 건강검진으로 상태를 확인한다.",
    ],
    "과체중": [
        "1. 하루 섭취 칼로리를 조금씩 줄여나간다.",
        "2. 걷기, 조깅 등 유산소 운동을 주 3~4회 실시한다.",
        "3. 단 음료와 고칼로리 간식 섭취를 줄인다.",
        "4. 체중 변화를 주기적으로 기록하고 관리한다.",
    ],
    "비만": [
        "1. 전문가(의사, 영양사)와 상담해 체중 감량 계획을 세운다.",
        "2. 유산소 운동과 근력 운동을 병행한다.",
        "3. 식단에서 탄수화물과 지방 섭취를 조절한다.",
        "4. 혈압, 혈당 등 관련 건강 지표를 함께 확인한다.",
    ],
    "고도비만": [
        "1. 반드시 병원을 방문해 정밀 검진과 상담을 받는다.",
        "2. 의료진의 지도 아래 체계적인 체중 감량 프로그램을 진행한다.",
        "3. 무리한 운동보다는 저강도 운동부터 서서히 시작한다.",
        "4. 동반 질환(당뇨, 고혈압 등) 여부를 반드시 확인한다.",
    ],
}


def main():
    print("=== BMI 계산기 ===")
    height_cm = get_positive_float("키를 입력하세요 (cm): ")
    weight_kg = get_positive_float("몸무게를 입력하세요 (kg): ")

    bmi = calculate_bmi(height_cm, weight_kg)
    category = classify_bmi(bmi)

    print("\n결과")
    print(f"BMI 지수: {bmi:.2f}")
    print(f"체중 상태: {category}")

    print(f"\n[{category}]을 위한 건강 관리 조언")
    for tip in ADVICE[category]:
        print(tip)


if __name__ == "__main__":
    main()
