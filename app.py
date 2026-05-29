"""세법개정 AI 어시스턴트 — 메인 앱."""
import base64
import os
import streamlit as st
from config import LAW_API_KEY, OPENAI_API_KEY
from ui import stage1_draft, stage2_crossref, stage3_output
from ui.styles import inject_global_css

st.set_page_config(
    page_title="세법개정 AI 어시스턴트",
    page_icon="📋",
    layout="wide",
)

inject_global_css()

# ── 앱 헤더 ──────────────────────────────────────────────────────────────────
_logo_html = ""
if os.path.exists("logo.png"):
    with open("logo.png", "rb") as _f:
        _b64 = base64.b64encode(_f.read()).decode()
    _logo_html = f'<img src="data:image/png;base64,{_b64}" class="mofe-header-logo" />'

st.markdown(f"""
<div class="mofe-header-card">
  {_logo_html}
  <div class="mofe-app-title">
    <h1>세법개정 AI 어시스턴트</h1>
  </div>
</div>
""", unsafe_allow_html=True)

law_api_key = LAW_API_KEY
openai_api_key = OPENAI_API_KEY

if not law_api_key or not openai_api_key:
    st.warning(".env 파일에 LAW_API_KEY, OPENAI_API_KEY를 설정하세요.")

# ── 탭 ────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["1️⃣ 초안 작성", "2️⃣ 인용·준용 확인", "3️⃣ HWPX 출력"])

with tab1:
    stage1_draft.render(law_api_key, openai_api_key)

with tab2:
    stage2_crossref.render(law_api_key, openai_api_key)

with tab3:
    stage3_output.render(law_api_key, openai_api_key)
