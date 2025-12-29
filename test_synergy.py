"""
Simple tests for the rune synergy system
Run with: python test_synergy.py
"""

from synergy_engine import calculate_synergy
from data import get_all_runes, get_set_effects


def test_no_runes():
    """Test with no runes selected"""
    result = calculate_synergy([])
    assert result.total_stats == {}
    assert result.active_set_effects == []
    assert result.equipped_runes == []
    print("✅ Test no runes: PASSED")


def test_single_rune():
    """Test with a single rune"""
    result = calculate_synergy(["rune_001"])
    assert len(result.equipped_runes) == 1
    assert result.equipped_runes[0].id == "rune_001"
    assert result.total_stats["hp"] == 850
    assert result.total_stats["atk"] == 120
    # Should have inactive set effects
    assert len(result.active_set_effects) == 2  # 2 and 4 set requirements
    assert not result.active_set_effects[0].is_active
    print("✅ Test single rune: PASSED")


def test_two_set_bonus():
    """Test 2-set bonus activation"""
    # Select 2 warrior runes
    result = calculate_synergy(["rune_001", "rune_002"])
    
    # Check runes are equipped
    assert len(result.equipped_runes) == 2
    
    # Check base stats
    assert result.total_stats["hp"] == 2050  # 850 + 1200
    assert result.total_stats["atk"] == 220  # 120 + 85 + 15 (2-set bonus)
    
    # Check 2-set is active but not 4-set
    active_effects = [e for e in result.active_set_effects if e.is_active]
    assert len(active_effects) == 1
    assert active_effects[0].required_count == 2
    assert active_effects[0].set_name == "전사의 힘"
    
    print("✅ Test 2-set bonus: PASSED")


def test_four_set_bonus():
    """Test 4-set bonus activation"""
    # Select 4 warrior runes
    result = calculate_synergy(["rune_001", "rune_002", "rune_003", "rune_004"])
    
    # Check runes are equipped
    assert len(result.equipped_runes) == 4
    
    # Check base stats + 4-set bonus (only highest bonus applied)
    base_hp = 850 + 1200  # from rune_001 and rune_002
    base_atk = 120 + 85 + 95 + 75  # from all 4 runes
    base_crit = 8
    base_speed = 35
    
    assert result.total_stats["hp"] == base_hp
    # 4-set gives +35% ATK, but we apply it as absolute value addition
    assert result.total_stats["atk"] == base_atk + 35  # base + 4-set bonus
    assert result.total_stats["crit_rate"] == base_crit
    assert result.total_stats["speed"] == base_speed
    
    # Check both 2-set and 4-set are active
    active_effects = [e for e in result.active_set_effects if e.is_active]
    assert len(active_effects) == 2
    assert any(e.required_count == 2 for e in active_effects)
    assert any(e.required_count == 4 for e in active_effects)
    
    print("✅ Test 4-set bonus: PASSED")


def test_mixed_sets():
    """Test with runes from different sets"""
    # 2 warrior + 2 guardian runes
    result = calculate_synergy(["rune_001", "rune_002", "rune_005", "rune_006"])
    
    # Should have 2 active 2-set bonuses
    active_effects = [e for e in result.active_set_effects if e.is_active]
    assert len(active_effects) == 2
    
    # Check both sets are represented
    set_names = [e.set_name for e in active_effects]
    assert "전사의 힘" in set_names
    assert "수호자의 방벽" in set_names
    
    print("✅ Test mixed sets: PASSED")


def test_three_set_bonus():
    """Test 3-set bonus (원소의 조화)"""
    # Select 3 elemental harmony runes
    result = calculate_synergy(["rune_019", "rune_020", "rune_021"])
    
    # Check 3-set is active
    active_effects = [e for e in result.active_set_effects if e.is_active]
    assert len(active_effects) == 1
    assert active_effects[0].required_count == 3
    assert active_effects[0].set_name == "원소의 조화"
    
    # Should have both ATK and DEF bonuses
    assert len(active_effects[0].bonus_stats) == 2
    
    print("✅ Test 3-set bonus: PASSED")


def test_data_integrity():
    """Test that sample data is valid"""
    runes = get_all_runes()
    sets = get_set_effects()
    
    assert len(runes) == 24
    assert len(sets) == 10
    
    # Check all runes have valid data
    for rune in runes:
        assert rune.id
        assert rune.name
        assert rune.grade in ["common", "rare", "epic", "legendary"]
        assert rune.property in ["fire", "water", "wind", "earth", "light", "dark"]
        assert rune.part in ["head", "chest", "gloves", "boots", "weapon", "accessory"]
        assert len(rune.base_stats) > 0
    
    # Check all set effects have valid data
    for set_effect in sets:
        assert set_effect.set_name
        assert set_effect.required_count >= 2
        assert len(set_effect.bonus_stats) > 0
        assert set_effect.description
    
    print("✅ Test data integrity: PASSED")


if __name__ == "__main__":
    print("\n🧪 Running Rune Synergy System Tests...\n")
    
    try:
        test_no_runes()
        test_single_rune()
        test_two_set_bonus()
        test_four_set_bonus()
        test_mixed_sets()
        test_three_set_bonus()
        test_data_integrity()
        
        print("\n🎉 All tests passed!\n")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
        raise
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}\n")
        raise
