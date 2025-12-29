from typing import List, Dict
from collections import Counter
from models import (
    Rune, RuneCombinationStats, ActiveSetEffect,
    BaseStat, StatType
)
from data import get_set_effects


class SynergyEngine:
    """룬 시너지 계산 엔진"""
    
    def __init__(self):
        self.set_effects = get_set_effects()
        # 세트별로 효과를 그룹화
        self.set_effects_map: Dict[str, List[ActiveSetEffect]] = {}
        for effect in self.set_effects:
            if effect.set_name not in self.set_effects_map:
                self.set_effects_map[effect.set_name] = []
            self.set_effects_map[effect.set_name].append(effect)
        
        # 각 세트의 효과를 필요 개수 내림차순으로 정렬 (큰 효과부터 체크)
        for set_name in self.set_effects_map:
            self.set_effects_map[set_name].sort(
                key=lambda x: x.required_count, 
                reverse=True
            )
    
    def calculate_combination_stats(self, runes: List[Rune]) -> RuneCombinationStats:
        """
        선택된 룬 조합의 통합 스탯과 활성화된 시너지를 계산
        
        Args:
            runes: 선택된 룬 리스트
            
        Returns:
            RuneCombinationStats: 총합 스탯과 활성화된 세트 효과
        """
        # 1. 세트별 룬 개수 카운트
        set_counter = Counter([rune.set_name for rune in runes])
        
        # 2. 활성화된 세트 효과 찾기
        active_set_effects = []
        for set_name, count in set_counter.items():
            if set_name == "독립":  # 독립 세트는 시너지 없음
                continue
            
            if set_name in self.set_effects_map:
                # 해당 세트의 활성화 가능한 효과들 확인
                for effect in self.set_effects_map[set_name]:
                    is_active = count >= effect.required_count
                    
                    active_effect = ActiveSetEffect(
                        set_name=effect.set_name,
                        current_count=count,
                        required_count=effect.required_count,
                        is_active=is_active,
                        bonus_stats=effect.bonus_stats if is_active else [],
                        description=effect.description
                    )
                    active_set_effects.append(active_effect)
        
        # 3. 기본 스탯 합산
        total_stats: Dict[str, int | float] = {}
        
        # 룬의 기본 스탯 합산
        for rune in runes:
            for stat in rune.base_stats:
                stat_key = stat.stat_type.value
                if stat_key not in total_stats:
                    total_stats[stat_key] = 0
                total_stats[stat_key] += stat.value
        
        # 4. 활성화된 세트 효과 보너스 스탯 적용
        # 가장 높은 레벨의 세트 효과만 적용 (중복 방지)
        applied_sets = set()
        for effect in active_set_effects:
            if effect.is_active:
                # 같은 세트의 더 낮은 레벨 효과가 이미 적용되었는지 확인
                if effect.set_name not in applied_sets:
                    applied_sets.add(effect.set_name)
                    for bonus_stat in effect.bonus_stats:
                        stat_key = bonus_stat.stat_type.value
                        if stat_key not in total_stats:
                            total_stats[stat_key] = bonus_stat.value
                        else:
                            # 퍼센트 기반 보너스 적용
                            total_stats[stat_key] += bonus_stat.value
        
        return RuneCombinationStats(
            total_stats=total_stats,
            active_set_effects=active_set_effects,
            equipped_runes=runes
        )
    
    def get_partial_set_effects(self, runes: List[Rune]) -> List[ActiveSetEffect]:
        """
        부분적으로 달성된 세트 효과도 포함하여 반환
        (진행도 표시용)
        """
        set_counter = Counter([rune.set_name for rune in runes])
        all_effects = []
        
        for set_name, count in set_counter.items():
            if set_name == "독립":
                continue
            
            if set_name in self.set_effects_map:
                for effect in self.set_effects_map[set_name]:
                    is_active = count >= effect.required_count
                    all_effects.append(ActiveSetEffect(
                        set_name=effect.set_name,
                        current_count=count,
                        required_count=effect.required_count,
                        is_active=is_active,
                        bonus_stats=effect.bonus_stats if is_active else [],
                        description=effect.description
                    ))
        
        return all_effects


# 전역 싱글톤 인스턴스
synergy_engine = SynergyEngine()


def calculate_synergy(rune_ids: List[str]) -> RuneCombinationStats:
    """
    룬 ID 리스트로부터 시너지 계산
    
    Args:
        rune_ids: 선택된 룬들의 ID 리스트
        
    Returns:
        RuneCombinationStats: 계산된 통합 스탯
    """
    from data import get_rune_by_id
    
    runes = []
    for rune_id in rune_ids:
        rune = get_rune_by_id(rune_id)
        if rune:
            runes.append(rune)
    
    return synergy_engine.calculate_combination_stats(runes)
