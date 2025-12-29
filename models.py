from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from enum import Enum


class RuneGrade(str, Enum):
    """룬 등급"""
    COMMON = "common"  # 일반
    RARE = "rare"      # 희귀
    EPIC = "epic"      # 영웅
    LEGENDARY = "legendary"  # 전설


class RuneProperty(str, Enum):
    """룬 속성"""
    FIRE = "fire"      # 화
    WATER = "water"    # 수
    WIND = "wind"      # 풍
    EARTH = "earth"    # 지
    LIGHT = "light"    # 광
    DARK = "dark"      # 암


class RunePart(str, Enum):
    """룬 부위"""
    HEAD = "head"      # 머리
    CHEST = "chest"    # 가슴
    GLOVES = "gloves"  # 장갑
    BOOTS = "boots"    # 신발
    WEAPON = "weapon"  # 무기
    ACCESSORY = "accessory"  # 장신구


class StatType(str, Enum):
    """스탯 타입"""
    HP = "hp"
    ATK = "atk"
    DEF = "def"
    CRIT_RATE = "crit_rate"
    CRIT_DMG = "crit_dmg"
    SPEED = "speed"
    ACCURACY = "accuracy"
    RESISTANCE = "resistance"


class BaseStat(BaseModel):
    """기본 스탯"""
    stat_type: StatType
    value: int | float


class SetEffect(BaseModel):
    """세트 효과 (시너지 조건)"""
    set_name: str = Field(description="세트 이름")
    required_count: int = Field(description="활성화에 필요한 룬 개수", ge=2)
    bonus_stats: List[BaseStat] = Field(description="보너스 스탯")
    description: str = Field(description="세트 효과 설명")


class Rune(BaseModel):
    """룬 데이터 모델"""
    id: str = Field(description="고유 ID")
    name: str = Field(description="룬 이름")
    grade: RuneGrade = Field(description="등급")
    property: RuneProperty = Field(description="속성")
    part: RunePart = Field(description="부위")
    set_name: str = Field(description="세트 이름")
    base_stats: List[BaseStat] = Field(description="기본 스탯")
    
    class Config:
        use_enum_values = True


class ActiveSetEffect(BaseModel):
    """활성화된 세트 효과"""
    set_name: str
    current_count: int
    required_count: int
    is_active: bool
    bonus_stats: List[BaseStat]
    description: str


class RuneCombinationStats(BaseModel):
    """룬 조합 통합 스탯"""
    total_stats: Dict[str, int | float] = Field(description="총합 스탯")
    active_set_effects: List[ActiveSetEffect] = Field(description="활성화된 세트 효과들")
    equipped_runes: List[Rune] = Field(description="장착된 룬들")
