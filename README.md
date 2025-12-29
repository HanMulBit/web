# 룬 시너지 시스템 (Rune Synergy System)

담벼엇 스타일의 룬 조합 시너지 계산 및 최적화 시스템입니다.

## 🌟 주요 기능

### 1. 데이터 모델 (Pydantic)
- **룬 속성**: 이름, 등급(전설/영웅/희귀/일반), 속성(화/수/풍/지/광/암), 부위(머리/가슴/장갑/신발/무기/장신구)
- **세트 효과**: 시너지 조건(2세트, 4세트 등) 및 보너스 스탯
- **샘플 데이터**: 24개의 다양한 룬과 10개의 세트 효과 포함

### 2. 시너지 엔진 (Synergy Engine)
- 실시간 룬 조합 분석
- 세트 효과 자동 계산 (2세트, 4세트 조건)
- 보너스 스탯 자동 적용
- 활성화/비활성화 시너지 표시

### 3. UI/UX (담벼엇 스타일)
- 🎴 **카드 기반 그리드 레이아웃**: 반응형 룬 카드 디자인
- 🔍 **고급 필터링**: 등급, 속성, 부위, 세트별 필터
- 📊 **실시간 대시보드**: 활성화된 시너지와 총합 스탯 표시
- 🎨 **다크 테마**: 눈이 편안한 담벼엇 스타일 컬러 팔레트
- 📱 **반응형 디자인**: 모바일 친화적 레이아웃

### 4. 공유 기능
- 🔗 **URL 파라미터 저장**: 선택된 룬 조합을 URL에 자동 저장
- 📋 **간편 공유**: 원클릭으로 URL 복사하여 공유
- 🔄 **자동 로드**: URL 접근 시 자동으로 룬 조합 복원

## 🚀 빠른 시작

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
python main.py
```

또는

```bash
uvicorn main:app --reload
```

### 3. 웹 브라우저 접속

```
http://localhost:8000
```

## 📁 프로젝트 구조

```
web/
├── main.py              # FastAPI 애플리케이션 및 API 엔드포인트
├── models.py            # Pydantic 데이터 모델 정의
├── data.py              # 샘플 룬 데이터 및 세트 효과
├── synergy_engine.py    # 시너지 계산 엔진
├── requirements.txt     # Python 의존성
├── static/
│   ├── index.html       # 메인 HTML 페이지
│   ├── style.css        # 담벼엇 스타일 CSS
│   └── app.js           # 프론트엔드 로직
└── README.md           # 프로젝트 문서
```

## 🎮 사용 방법

### 룬 선택
1. 룬 목록에서 원하는 룬 카드를 클릭
2. 선택된 룬은 상단 "선택된 룬" 섹션에 표시
3. 다시 클릭하면 선택 해제

### 필터 사용
- **등급**: 전설, 영웅, 희귀, 일반
- **속성**: 화, 수, 풍, 지, 광, 암
- **부위**: 머리, 가슴, 장갑, 신발, 무기, 장신구
- **세트**: 특정 세트로 필터링

### 시너지 확인
- 대시보드에서 활성화된 시너지 자동 표시
- 활성화된 시너지는 초록색으로 하이라이트
- 진행 중인 시너지는 회색으로 표시 (예: 2/4)

### 조합 공유
1. "조합 공유" 버튼 클릭
2. 생성된 URL 복사
3. 다른 사용자와 공유

## 🔧 API 엔드포인트

### GET `/api/runes`
모든 룬 조회 (필터링 가능)

**Query Parameters:**
- `grade`: 등급 필터 (legendary, epic, rare, common)
- `property`: 속성 필터 (fire, water, wind, earth, light, dark)
- `part`: 부위 필터 (head, chest, gloves, boots, weapon, accessory)
- `set_name`: 세트 이름 필터

**Example:**
```
GET /api/runes?grade=legendary&property=fire
```

### GET `/api/sets`
모든 세트 효과 조회

### GET `/api/calculate`
선택된 룬 조합의 시너지 계산

**Query Parameters:**
- `rune_ids`: 룬 ID 리스트 (다중 값)

**Example:**
```
GET /api/calculate?rune_ids=rune_001&rune_ids=rune_002&rune_ids=rune_003&rune_ids=rune_004
```

### GET `/api/rune/{rune_id}`
특정 룬 상세 정보 조회

## 📊 세트 효과 예시

### 전사의 힘
- **2세트**: 공격력 +15%
- **4세트**: 공격력 +35%

### 수호자의 방벽
- **2세트**: 방어력 +15%
- **4세트**: 방어력 +35%

### 치명타 마스터
- **2세트**: 치명타 확률 +12%
- **4세트**: 치명타 확률 +20%, 치명타 피해 +30%

### 원소의 조화
- **3세트**: 공격력 +20%, 방어력 +20%

## 🎨 스타일 가이드

### 컬러 팔레트
- **Primary**: #6366f1 (인디고)
- **Secondary**: #8b5cf6 (보라)
- **Accent**: #ec4899 (핑크)
- **Success**: #10b981 (초록)
- **Background**: #0f172a (다크 블루)

### 등급별 색상
- **전설**: 황금색 그라디언트
- **영웅**: 보라색 그라디언트
- **희귀**: 파란색 그라디언트
- **일반**: 회색 그라디언트

## 🛠️ 개발

### 새로운 룬 추가
`data.py`의 `SAMPLE_RUNES` 리스트에 새로운 `Rune` 객체 추가

```python
Rune(
    id="rune_025",
    name="새로운 룬",
    grade=RuneGrade.LEGENDARY,
    property=RuneProperty.FIRE,
    part=RunePart.HEAD,
    set_name="전사의 힘",
    base_stats=[
        BaseStat(stat_type=StatType.HP, value=1000),
        BaseStat(stat_type=StatType.ATK, value=150)
    ]
)
```

### 새로운 세트 효과 추가
`data.py`의 `SET_EFFECTS` 리스트에 새로운 `SetEffect` 객체 추가

```python
SetEffect(
    set_name="새로운 세트",
    required_count=2,
    bonus_stats=[
        BaseStat(stat_type=StatType.SPEED, value=30)
    ],
    description="속도 +30"
)
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🤝 기여

버그 리포트, 기능 제안, Pull Request를 환영합니다!
