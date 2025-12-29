from models import (
    Rune, SetEffect, RuneGrade, RuneProperty, RunePart,
    BaseStat, StatType
)
from typing import List


# 세트 효과 정의
SET_EFFECTS: List[SetEffect] = [
    SetEffect(
        set_name="전사의 힘",
        required_count=2,
        bonus_stats=[
            BaseStat(stat_type=StatType.ATK, value=15)
        ],
        description="공격력 +15%"
    ),
    SetEffect(
        set_name="전사의 힘",
        required_count=4,
        bonus_stats=[
            BaseStat(stat_type=StatType.ATK, value=35)
        ],
        description="공격력 +35%"
    ),
    SetEffect(
        set_name="수호자의 방벽",
        required_count=2,
        bonus_stats=[
            BaseStat(stat_type=StatType.DEF, value=15)
        ],
        description="방어력 +15%"
    ),
    SetEffect(
        set_name="수호자의 방벽",
        required_count=4,
        bonus_stats=[
            BaseStat(stat_type=StatType.DEF, value=35)
        ],
        description="방어력 +35%"
    ),
    SetEffect(
        set_name="질풍의 속도",
        required_count=2,
        bonus_stats=[
            BaseStat(stat_type=StatType.SPEED, value=25)
        ],
        description="속도 +25"
    ),
    SetEffect(
        set_name="질풍의 속도",
        required_count=4,
        bonus_stats=[
            BaseStat(stat_type=StatType.SPEED, value=50)
        ],
        description="속도 +50"
    ),
    SetEffect(
        set_name="치명타 마스터",
        required_count=2,
        bonus_stats=[
            BaseStat(stat_type=StatType.CRIT_RATE, value=12)
        ],
        description="치명타 확률 +12%"
    ),
    SetEffect(
        set_name="치명타 마스터",
        required_count=4,
        bonus_stats=[
            BaseStat(stat_type=StatType.CRIT_RATE, value=20),
            BaseStat(stat_type=StatType.CRIT_DMG, value=30)
        ],
        description="치명타 확률 +20%, 치명타 피해 +30%"
    ),
    SetEffect(
        set_name="생명의 축복",
        required_count=2,
        bonus_stats=[
            BaseStat(stat_type=StatType.HP, value=15)
        ],
        description="HP +15%"
    ),
    SetEffect(
        set_name="원소의 조화",
        required_count=3,
        bonus_stats=[
            BaseStat(stat_type=StatType.ATK, value=20),
            BaseStat(stat_type=StatType.DEF, value=20)
        ],
        description="공격력 +20%, 방어력 +20%"
    ),
]


# 샘플 룬 데이터
SAMPLE_RUNES: List[Rune] = [
    # 전사의 힘 세트
    Rune(
        id="rune_001",
        name="화염의 투구",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.FIRE,
        part=RunePart.HEAD,
        set_name="전사의 힘",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=850),
            BaseStat(stat_type=StatType.ATK, value=120)
        ]
    ),
    Rune(
        id="rune_002",
        name="화염의 갑옷",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.FIRE,
        part=RunePart.CHEST,
        set_name="전사의 힘",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1200),
            BaseStat(stat_type=StatType.ATK, value=85)
        ]
    ),
    Rune(
        id="rune_003",
        name="화염의 장갑",
        grade=RuneGrade.EPIC,
        property=RuneProperty.FIRE,
        part=RunePart.GLOVES,
        set_name="전사의 힘",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=95),
            BaseStat(stat_type=StatType.CRIT_RATE, value=8)
        ]
    ),
    Rune(
        id="rune_004",
        name="화염의 신발",
        grade=RuneGrade.EPIC,
        property=RuneProperty.FIRE,
        part=RunePart.BOOTS,
        set_name="전사의 힘",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=75),
            BaseStat(stat_type=StatType.SPEED, value=35)
        ]
    ),
    
    # 수호자의 방벽 세트
    Rune(
        id="rune_005",
        name="대지의 투구",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.EARTH,
        part=RunePart.HEAD,
        set_name="수호자의 방벽",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=950),
            BaseStat(stat_type=StatType.DEF, value=110)
        ]
    ),
    Rune(
        id="rune_006",
        name="대지의 갑옷",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.EARTH,
        part=RunePart.CHEST,
        set_name="수호자의 방벽",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1350),
            BaseStat(stat_type=StatType.DEF, value=95)
        ]
    ),
    Rune(
        id="rune_007",
        name="대지의 장갑",
        grade=RuneGrade.EPIC,
        property=RuneProperty.EARTH,
        part=RunePart.GLOVES,
        set_name="수호자의 방벽",
        base_stats=[
            BaseStat(stat_type=StatType.DEF, value=85),
            BaseStat(stat_type=StatType.HP, value=650)
        ]
    ),
    Rune(
        id="rune_008",
        name="대지의 신발",
        grade=RuneGrade.EPIC,
        property=RuneProperty.EARTH,
        part=RunePart.BOOTS,
        set_name="수호자의 방벽",
        base_stats=[
            BaseStat(stat_type=StatType.DEF, value=75),
            BaseStat(stat_type=StatType.SPEED, value=30)
        ]
    ),
    
    # 질풍의 속도 세트
    Rune(
        id="rune_009",
        name="바람의 투구",
        grade=RuneGrade.EPIC,
        property=RuneProperty.WIND,
        part=RunePart.HEAD,
        set_name="질풍의 속도",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=720),
            BaseStat(stat_type=StatType.SPEED, value=40)
        ]
    ),
    Rune(
        id="rune_010",
        name="바람의 갑옷",
        grade=RuneGrade.EPIC,
        property=RuneProperty.WIND,
        part=RunePart.CHEST,
        set_name="질풍의 속도",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=980),
            BaseStat(stat_type=StatType.SPEED, value=45)
        ]
    ),
    Rune(
        id="rune_011",
        name="바람의 장갑",
        grade=RuneGrade.RARE,
        property=RuneProperty.WIND,
        part=RunePart.GLOVES,
        set_name="질풍의 속도",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=68),
            BaseStat(stat_type=StatType.SPEED, value=38)
        ]
    ),
    Rune(
        id="rune_012",
        name="바람의 신발",
        grade=RuneGrade.RARE,
        property=RuneProperty.WIND,
        part=RunePart.BOOTS,
        set_name="질풍의 속도",
        base_stats=[
            BaseStat(stat_type=StatType.SPEED, value=55),
            BaseStat(stat_type=StatType.ATK, value=55)
        ]
    ),
    
    # 치명타 마스터 세트
    Rune(
        id="rune_013",
        name="암흑의 투구",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.DARK,
        part=RunePart.HEAD,
        set_name="치명타 마스터",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=800),
            BaseStat(stat_type=StatType.CRIT_RATE, value=10)
        ]
    ),
    Rune(
        id="rune_014",
        name="암흑의 갑옷",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.DARK,
        part=RunePart.CHEST,
        set_name="치명타 마스터",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1100),
            BaseStat(stat_type=StatType.CRIT_DMG, value=40)
        ]
    ),
    Rune(
        id="rune_015",
        name="암흑의 무기",
        grade=RuneGrade.EPIC,
        property=RuneProperty.DARK,
        part=RunePart.WEAPON,
        set_name="치명타 마스터",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=150),
            BaseStat(stat_type=StatType.CRIT_RATE, value=8)
        ]
    ),
    Rune(
        id="rune_016",
        name="암흑의 장신구",
        grade=RuneGrade.EPIC,
        property=RuneProperty.DARK,
        part=RunePart.ACCESSORY,
        set_name="치명타 마스터",
        base_stats=[
            BaseStat(stat_type=StatType.CRIT_DMG, value=35),
            BaseStat(stat_type=StatType.ATK, value=75)
        ]
    ),
    
    # 생명의 축복 세트
    Rune(
        id="rune_017",
        name="성수의 투구",
        grade=RuneGrade.EPIC,
        property=RuneProperty.WATER,
        part=RunePart.HEAD,
        set_name="생명의 축복",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1050),
            BaseStat(stat_type=StatType.DEF, value=60)
        ]
    ),
    Rune(
        id="rune_018",
        name="성수의 갑옷",
        grade=RuneGrade.EPIC,
        property=RuneProperty.WATER,
        part=RunePart.CHEST,
        set_name="생명의 축복",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1400),
            BaseStat(stat_type=StatType.DEF, value=55)
        ]
    ),
    
    # 원소의 조화 세트
    Rune(
        id="rune_019",
        name="빛의 투구",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.LIGHT,
        part=RunePart.HEAD,
        set_name="원소의 조화",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=900),
            BaseStat(stat_type=StatType.ATK, value=100),
            BaseStat(stat_type=StatType.DEF, value=80)
        ]
    ),
    Rune(
        id="rune_020",
        name="빛의 갑옷",
        grade=RuneGrade.LEGENDARY,
        property=RuneProperty.LIGHT,
        part=RunePart.CHEST,
        set_name="원소의 조화",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=1250),
            BaseStat(stat_type=StatType.ATK, value=80),
            BaseStat(stat_type=StatType.DEF, value=90)
        ]
    ),
    Rune(
        id="rune_021",
        name="빛의 무기",
        grade=RuneGrade.EPIC,
        property=RuneProperty.LIGHT,
        part=RunePart.WEAPON,
        set_name="원소의 조화",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=130),
            BaseStat(stat_type=StatType.DEF, value=70)
        ]
    ),
    
    # 독립 룬들 (세트 없음, 믹스 매치용)
    Rune(
        id="rune_022",
        name="고독한 전사의 투구",
        grade=RuneGrade.RARE,
        property=RuneProperty.FIRE,
        part=RunePart.HEAD,
        set_name="독립",
        base_stats=[
            BaseStat(stat_type=StatType.HP, value=600),
            BaseStat(stat_type=StatType.ATK, value=90)
        ]
    ),
    Rune(
        id="rune_023",
        name="방랑자의 장갑",
        grade=RuneGrade.RARE,
        property=RuneProperty.WIND,
        part=RunePart.GLOVES,
        set_name="독립",
        base_stats=[
            BaseStat(stat_type=StatType.ATK, value=75),
            BaseStat(stat_type=StatType.SPEED, value=25)
        ]
    ),
    Rune(
        id="rune_024",
        name="균형의 신발",
        grade=RuneGrade.COMMON,
        property=RuneProperty.EARTH,
        part=RunePart.BOOTS,
        set_name="독립",
        base_stats=[
            BaseStat(stat_type=StatType.SPEED, value=40),
            BaseStat(stat_type=StatType.HP, value=450)
        ]
    ),
]


def get_all_runes() -> List[Rune]:
    """모든 룬 반환"""
    return SAMPLE_RUNES


def get_set_effects() -> List[SetEffect]:
    """모든 세트 효과 반환"""
    return SET_EFFECTS


def get_rune_by_id(rune_id: str) -> Rune | None:
    """ID로 룬 검색"""
    for rune in SAMPLE_RUNES:
        if rune.id == rune_id:
            return rune
    return None
