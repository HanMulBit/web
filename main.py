from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
import os

from models import Rune, RuneCombinationStats, RuneGrade, RuneProperty, RunePart
from data import get_all_runes, get_set_effects
from synergy_engine import calculate_synergy

app = FastAPI(
    title="룬 시너지 시스템",
    description="룬 조합 시너지 계산 및 최적화 시스템",
    version="1.0.0"
)

# 정적 파일 서빙
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    """메인 페이지"""
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>룬 시너지 시스템</h1><p>static/index.html 파일을 생성해주세요.</p>"


@app.get("/api/runes", response_model=List[Rune])
async def get_runes(
    grade: Optional[RuneGrade] = None,
    property: Optional[RuneProperty] = None,
    part: Optional[RunePart] = None,
    set_name: Optional[str] = None
):
    """
    모든 룬 조회 (필터링 가능)
    
    Query Parameters:
    - grade: 룬 등급 필터
    - property: 룬 속성 필터
    - part: 룬 부위 필터
    - set_name: 세트 이름 필터
    """
    runes = get_all_runes()
    
    # 필터링
    if grade:
        runes = [r for r in runes if r.grade == grade]
    if property:
        runes = [r for r in runes if r.property == property]
    if part:
        runes = [r for r in runes if r.part == part]
    if set_name:
        runes = [r for r in runes if r.set_name == set_name]
    
    return runes


@app.get("/api/sets")
async def get_sets():
    """모든 세트 효과 조회"""
    return get_set_effects()


@app.get("/api/calculate", response_model=RuneCombinationStats)
async def calculate_combination(
    rune_ids: List[str] = Query(
        ..., 
        description="선택된 룬 ID 리스트",
        example=["rune_001", "rune_002", "rune_003", "rune_004"]
    )
):
    """
    선택된 룬 조합의 시너지와 통합 스탯 계산
    
    Query Parameters:
    - rune_ids: 룬 ID들의 리스트 (예: ?rune_ids=rune_001&rune_ids=rune_002)
    """
    return calculate_synergy(rune_ids)


@app.get("/api/rune/{rune_id}", response_model=Rune)
async def get_rune(rune_id: str):
    """특정 룬 상세 정보 조회"""
    from data import get_rune_by_id
    
    rune = get_rune_by_id(rune_id)
    if not rune:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="룬을 찾을 수 없습니다")
    
    return rune


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
