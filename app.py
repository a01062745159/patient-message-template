import streamlit as st
import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="환자 문자 템플릿 관리",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 데이터 저장 폴더 생성
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

TEMPLATES_FILE = DATA_DIR / "templates.json"
YOUTUBE_FILE = DATA_DIR / "youtube_links.json"

# 초기 데이터 로드 함수
def load_templates():
    if TEMPLATES_FILE.exists():
        with open(TEMPLATES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "기본형": "수려한치과입니다.\n지난 상담 후 치료 계획과 관련해 궁금하신 점은 없으실까요?\n치아 상태에 따라 치료 시기가 중요할 수 있어 편하실 때 문의 또는 예약 주시면 자세히 안내드리겠습니다. 감사합니다.",
        "공감형": "수려한치과입니다.\n치과 치료는 통증이나 비용 때문에 고민이 많으실 수 있습니다.\n혹시 치료 관련해 걱정되시는 부분이나 궁금한 점 있으시면 편하게 문의 주세요.\n환자분 상황에 맞춰 안내 도와드리겠습니다",
        "리마인드형": "수려한치과입니다.\n지난번 상담받으신 부위는 시간이 지나면 증상이 심해지거나 치료 범위가 커질 수 있어 안내드립니다.\n불편감이 있으시거나 예약 원하시면 편한 시간에 연락 주세요. 감사합니다.",
        "재예약 유도": "수려한치과입니다.\n지난 상담 이후 치료 일정이 잡혀 있지 않아 안내드립니다.\n원하시는 날짜 있으시면 예약 도와드리겠습니다.\n문의사항도 편하게 연락 주세요 :)",
        "임플란트/고액 치료용": "수려한치과입니다.\n지난 상담 이후 고민이 많으실 것 같아 연락드립니다.\n치료 방법·기간·비용 관련 추가 상담 원하시면 편하게 문의 주세요.\n환자분께 맞는 방향으로 충분히 상의 후 진행 도와드리겠습니다.",
        "이벤트/검진 연계형": "수려한치과입니다.\n지난 상담받으신 내용 관련해 추가 안내드립니다.\n현재 정기 검진 및 치료 상담 예약 가능하오니 불편함 없으시더라도 상태에 따라 치료 시기가 중요할 수 있어 원하시면 언제든 편하게 연락 주세요. 감사합니다."
    }

def save_templates(templates):
    with open(TEMPLATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(templates, f, ensure_ascii=False, indent=2)

def load_youtube_links():
    if YOUTUBE_FILE.exists():
        with open(YOUTUBE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_youtube_links(links):
    with open(YOUTUBE_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)

# 초기 세션 상태
if 'templates' not in st.session_state:
    st.session_state.templates = load_templates()

if 'youtube_links' not in st.session_state:
    st.session_state.youtube_links = load_youtube_links()

# 제목
st.title("📱 환자 문자 템플릿 관리 시스템")

# 탭 생성
tab1, tab2, tab3 = st.tabs(["📤 템플릿 선택 및 복사", "✍️ 템플릿 관리", "🎥 YouTube 링크 관리"])

# ===== TAB 1: 템플릿 선택 및 복사 =====
with tab1:
    st.header("템플릿 선택 및 복사")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("📝 설정")
        
        template_names = list(st.session_state.templates.keys())
        if template_names:
            # 환자 이름 입력
            patient_name = st.text_input(
                "환자 이름",
                placeholder="예: 김철수",
                max_chars=20
            )
            
            selected_template = st.selectbox(
                "템플릿 선택",
                template_names,
                label_visibility="collapsed"
            )
            
            add_video = st.checkbox("YouTube 링크 추가")
            video_link = ""
            video_title = ""
            
            if add_video and st.session_state.youtube_links:
                youtube_options = {f"{item['title']} ({item['url'][:20]}...)" : item['url'] 
                                  for item in st.session_state.youtube_links}
                selected_video = st.selectbox(
                    "YouTube 영상 선택",
                    list(youtube_options.keys()),
                    label_visibility="collapsed"
                )
                video_link = youtube_options[selected_video]
                video_title = st.session_state.youtube_links[[item['url'] for item in st.session_state.youtube_links].index(video_link)]['title']
            elif add_video:
                st.warning("⚠️ 등록된 YouTube 링크가 없습니다. YouTube 링크 관리 탭에서 추가해주세요.")
            
            address = st.text_area(
                "병원 정보 (주소/전화번호 등)",
                placeholder="예: 경기도 오산시 성호대로 81, 1층 서울수려한치과\n031-xxxx-xxxx",
                max_chars=200
            )
        else:
            st.error("❌ 등록된 템플릿이 없습니다. 템플릿 관리 탭에서 추가해주세요.")
    
    with col2:
        if template_names:
            st.subheader("👁️ 미리보기")
            
            message = st.session_state.templates[selected_template]
            
            # 환자 이름 추가
            if patient_name:
                message = f"{patient_name}님 안녕하세요.\n\n" + message
            
            if add_video and video_link:
                message += f"\n\n🎥 {video_title}\n{video_link}"
            
            if address:
                message += f"\n\n📍 {address}"
            
            st.text_area(
                "문자 내용",
                value=message,
                disabled=True,
                height=300,
                label_visibility="collapsed"
            )
            
            # 복사 버튼
            col_copy, col_reset = st.columns(2)
            with col_copy:
                if st.button("📋 클립보드에 복사", use_container_width=True, key="tab1_copy"):
                    st.write(message)
                    st.success("✅ 복사했습니다! 문자 앱에 붙여넣기 하세요.")
            
            with col_reset:
                if st.button("🔄 초기화", use_container_width=True, key="tab1_reset"):
                    st.rerun()

# ===== TAB 2: 템플릿 관리 =====
with tab2:
    st.header("템플릿 추가 및 수정")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("작업 선택")
        action = st.radio(
            "작업을 선택하세요",
            ["새 템플릿 추가", "기존 템플릿 수정", "템플릿 삭제"],
            label_visibility="collapsed"
        )
    
    with col2:
        if action == "새 템플릿 추가":
            st.subheader("➕ 새 템플릿 추가")
            
            new_name = st.text_input(
                "템플릿 이름",
                placeholder="예: 치석 제거 후 안내",
                key="new_template_name"
            )
            
            new_content = st.text_area(
                "템플릿 내용",
                placeholder="[🏥 제목]\n\n내용을 입력하세요...",
                height=300,
                key="new_template_content"
            )
            
            col_add, col_cancel = st.columns(2)
            with col_add:
                if st.button("✅ 새 템플릿 저장", use_container_width=True, key="btn_add_template"):
                    if new_name and new_content:
                        if new_name in st.session_state.templates:
                            st.error("❌ 이미 있는 이름입니다.")
                        else:
                            st.session_state.templates[new_name] = new_content
                            save_templates(st.session_state.templates)
                            st.success(f"✅ '{new_name}' 템플릿이 저장되었습니다!")
                            st.rerun()
                    else:
                        st.error("❌ 이름과 내용을 모두 입력해주세요.")
            
            with col_cancel:
                if st.button("취소", use_container_width=True, key="btn_cancel_add"):
                    st.rerun()
        
        elif action == "기존 템플릿 수정":
            st.subheader("✏️ 기존 템플릿 수정")
            
            template_names = list(st.session_state.templates.keys())
            if template_names:
                selected = st.selectbox(
                    "수정할 템플릿 선택",
                    template_names,
                    label_visibility="collapsed",
                    key="select_edit_template"
                )
                
                # 선택된 템플릿의 기존 내용 표시
                st.info(f"📝 선택한 템플릿: **{selected}**")
                
                edited_content = st.text_area(
                    "템플릿 내용",
                    value=st.session_state.templates[selected],
                    height=300,
                    label_visibility="collapsed",
                    key=f"edit_template_content_{selected}"
                )
                
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.button("💾 수정 저장", use_container_width=True, key="btn_save_edit"):
                        st.session_state.templates[selected] = edited_content
                        save_templates(st.session_state.templates)
                        st.success(f"✅ '{selected}' 템플릿이 수정되었습니다!")
                        st.rerun()
                
                with col_cancel:
                    if st.button("취소", use_container_width=True, key="btn_cancel_edit"):
                        st.rerun()
            else:
                st.warning("⚠️ 수정할 템플릿이 없습니다.")
        
        elif action == "템플릿 삭제":
            st.subheader("🗑️ 템플릿 삭제")
            
            template_names = list(st.session_state.templates.keys())
            if template_names:
                selected = st.selectbox(
                    "삭제할 템플릿 선택",
                    template_names,
                    label_visibility="collapsed",
                    key="select_delete_template"
                )
                
                st.warning(f"⚠️ '{selected}' 템플릿을 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")
                
                col_delete, col_cancel = st.columns(2)
                with col_delete:
                    if st.button("🗑️ 삭제 확인", use_container_width=True, key="btn_delete_confirm"):
                        del st.session_state.templates[selected]
                        save_templates(st.session_state.templates)
                        st.success(f"✅ '{selected}' 템플릿이 삭제되었습니다!")
                        st.rerun()
                
                with col_cancel:
                    if st.button("취소", use_container_width=True, key="btn_cancel_delete"):
                        st.rerun()
            else:
                st.warning("⚠️ 삭제할 템플릿이 없습니다.")
    
    # 현재 저장된 템플릿 목록
    st.divider()
    st.subheader("📚 저장된 템플릿 목록")
    
    if st.session_state.templates:
        for idx, (name, content) in enumerate(st.session_state.templates.items(), 1):
            with st.expander(f"{idx}. {name}"):
                st.text(content)
    else:
        st.info("등록된 템플릿이 없습니다.")

# ===== TAB 3: YouTube 링크 관리 =====
with tab3:
    st.header("YouTube 링크 관리")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("작업 선택")
        yt_action = st.radio(
            "작업을 선택하세요",
            ["새 링크 추가", "링크 삭제"],
            label_visibility="collapsed",
            key="yt_action_radio"
        )
    
    with col2:
        if yt_action == "새 링크 추가":
            st.subheader("➕ YouTube 링크 추가")
            
            yt_title = st.text_input(
                "영상 제목",
                placeholder="예: 올바른 칫솔질 방법",
                key="yt_title_input"
            )
            
            yt_url = st.text_input(
                "YouTube 링크",
                placeholder="https://youtu.be/... 또는 https://www.youtube.com/watch?v=...",
                key="yt_url_input"
            )
            
            col_add, col_cancel = st.columns(2)
            with col_add:
                if st.button("✅ 링크 저장", use_container_width=True, key="btn_add_yt"):
                    if yt_title and yt_url:
                        # 중복 확인
                        if any(item['url'] == yt_url for item in st.session_state.youtube_links):
                            st.error("❌ 이미 등록된 링크입니다.")
                        else:
                            st.session_state.youtube_links.append({
                                "title": yt_title,
                                "url": yt_url,
                                "added_at": datetime.now().isoformat()
                            })
                            save_youtube_links(st.session_state.youtube_links)
                            st.success(f"✅ '{yt_title}' 링크가 저장되었습니다!")
                            st.rerun()
                    else:
                        st.error("❌ 제목과 링크를 모두 입력해주세요.")
            
            with col_cancel:
                if st.button("취소", use_container_width=True, key="btn_cancel_add_yt"):
                    st.rerun()
        
        elif yt_action == "링크 삭제":
            st.subheader("🗑️ YouTube 링크 삭제")
            
            if st.session_state.youtube_links:
                yt_options = [item['title'] for item in st.session_state.youtube_links]
                selected_yt = st.selectbox(
                    "삭제할 링크 선택",
                    yt_options,
                    label_visibility="collapsed",
                    key="select_delete_yt"
                )
                
                selected_idx = yt_options.index(selected_yt)
                selected_item = st.session_state.youtube_links[selected_idx]
                
                st.warning(f"⚠️ 다음 링크를 삭제하시겠습니까?\n\n**{selected_item['title']}**\n{selected_item['url']}")
                
                col_delete, col_cancel = st.columns(2)
                with col_delete:
                    if st.button("🗑️ 삭제 확인", use_container_width=True, key="btn_delete_yt"):
                        st.session_state.youtube_links.pop(selected_idx)
                        save_youtube_links(st.session_state.youtube_links)
                        st.success("✅ 링크가 삭제되었습니다!")
                        st.rerun()
                
                with col_cancel:
                    if st.button("취소", use_container_width=True, key="btn_cancel_delete_yt"):
                        st.rerun()
            else:
                st.warning("⚠️ 삭제할 링크가 없습니다.")
    
    # 현재 저장된 YouTube 링크 목록
    st.divider()
    st.subheader("📺 저장된 YouTube 링크 목록")
    
    if st.session_state.youtube_links:
        for idx, item in enumerate(st.session_state.youtube_links, 1):
            with st.expander(f"{idx}. {item['title']}"):
                st.write(f"**링크:** {item['url']}")
                st.write(f"*등록일: {item['added_at'][:10]}*")
    else:
        st.info("등록된 YouTube 링크가 없습니다.")

# 사이드바
with st.sidebar:
    st.title("📊 통계")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("템플릿", len(st.session_state.templates))
    with col2:
        st.metric("YouTube 링크", len(st.session_state.youtube_links))
    
    st.divider()
    st.markdown("""
    ### 💡 사용 설명서
    
    **Tab 1: 템플릿 선택**
    - 기존 템플릿을 선택해서 복사합니다
    - YouTube 링크와 병원 정보를 추가할 수 있습니다
    
    **Tab 2: 템플릿 관리**
    - 새로운 템플릿을 추가합니다
    - 기존 템플릿을 수정합니다
    - 불필요한 템플릿을 삭제합니다
    
    **Tab 3: YouTube 관리**
    - 유튜브 영상 링크를 등록합니다
    - 등록된 링크를 삭제합니다
    """)
