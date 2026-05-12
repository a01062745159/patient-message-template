# 📱 환자 문자 템플릿 관리 시스템

의료기관에서 환자들에게 보낼 문자 템플릿을 쉽게 관리하고 복사할 수 있는 Streamlit 기반 웹 애플리케이션입니다.

## ✨ 주요 기능

### 📤 Tab 1: 템플릿 선택 및 복사
- 저장된 템플릿 중 선택
- YouTube 영상 링크 추가
- 병원 주소/연락처 정보 추가
- 실시간 미리보기
- 한 번에 클립보드로 복사

### ✍️ Tab 2: 템플릿 관리
- **새 템플릿 추가** - 새로운 문자 템플릿 작성
- **기존 템플릿 수정** - 저장된 템플릿 편집
- **템플릿 삭제** - 불필요한 템플릿 삭제
- 모든 템플릿 목록 확인

### 🎥 Tab 3: YouTube 링크 관리
- YouTube 영상 제목과 링크 등록
- 등록된 링크 삭제
- 링크 목록 확인
- Tab 1에서 선택해서 사용 가능

## 🚀 설치 및 실행

### 로컬 환경에서 실행

1. **저장소 클론**
```bash
git clone https://github.com/your-username/patient-message-template.git
cd patient-message-template
```

2. **가상 환경 생성 (선택사항이지만 권장)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **필수 패키지 설치**
```bash
pip install -r requirements.txt
```

4. **Streamlit 앱 실행**
```bash
streamlit run app.py
```

5. **브라우저에서 열기**
```
http://localhost:8501
```

## 🌐 Streamlit Cloud로 배포

### 1단계: GitHub에 업로드
- GitHub 계정에 로그인
- 새 리포지토리 생성 (`patient-message-template`)
- 파일 업로드

### 2단계: Streamlit Cloud 연결
1. [Streamlit Cloud](https://share.streamlit.io)에 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 다음 정보 입력:
   - **Repository**: your-username/patient-message-template
   - **Branch**: main
   - **Main file path**: app.py

### 3단계: 배포
"Deploy" 클릭하면 자동으로 배포됩니다!

배포 완료 후 URL: `https://share.streamlit.io/your-username/patient-message-template`

## 📁 프로젝트 구조

```
patient-message-template/
├── app.py                 # 메인 Streamlit 앱
├── requirements.txt       # 필수 패키지
├── README.md             # 설명서
└── data/                 # 데이터 저장 폴더 (자동 생성)
    ├── templates.json    # 저장된 템플릿
    └── youtube_links.json # YouTube 링크 목록
```

## 💾 데이터 저장

모든 데이터는 JSON 파일로 저장됩니다:
- **templates.json**: 저장된 문자 템플릿
- **youtube_links.json**: 등록된 YouTube 링크

> ⚠️ **Streamlit Cloud에서 주의**
> Streamlit Cloud의 `/data` 폴더는 앱이 재시작되면 초기화됩니다.
> 영구 저장이 필요하면 추후 데이터베이스(SQLite 등) 연동이 필요합니다.

## 🎯 사용 예시

### 1. 초진 환자에게 보낼 문자
1. Tab 1에서 "초진 환자" 템플릿 선택
2. YouTube 링크 추가 체크
3. 진료 안내 영상 선택
4. 병원 주소/전화번호 입력
5. "클립보드에 복사" 클릭
6. 문자 앱에 붙여넣기

### 2. 새로운 템플릿 추가
1. Tab 2로 이동
2. "새 템플릿 추가" 선택
3. 템플릿 이름과 내용 입력
4. "저장" 클릭

### 3. YouTube 영상 등록
1. Tab 3로 이동
2. "새 링크 추가" 선택
3. 영상 제목 입력
4. YouTube URL 입력 (youtu.be 또는 youtube.com 형식)
5. "저장" 클릭

## 🔧 기본 템플릿

앱 실행 시 다음 6가지 기본 템플릿이 자동으로 생성됩니다:

1. **초진 환자** - 첫 방문 환자 안내
2. **재진 환자** - 정기 방문 상기
3. **시술 후 관리** - 시술 후 주의사항
4. **검진 결과** - 검진 결과 안내
5. **예방 검진** - 검진 권유
6. **예약 확인** - 예약 확정 안내

## 📱 호환성

- **운영체제**: Windows, macOS, Linux
- **브라우저**: Chrome, Safari, Edge, Firefox (최신 버전)
- **모바일**: 반응형 디자인으로 스마트폰에서도 사용 가능

## 🐛 트러블슈팅

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### 데이터가 저장되지 않는 경우
- `data` 폴더가 생성되었는지 확인
- 폴더 쓰기 권한 확인

### Streamlit Cloud에서 이전 데이터가 보이지 않음
- Streamlit Cloud는 매번 새로운 환경에서 실행되므로 로컬 파일 저장이 영구적이지 않습니다
- 정기적으로 데이터를 백업하세요

## 📚 추가 기능 (향후 업데이트)

- [ ] SQLite 데이터베이스 연동 (영구 저장)
- [ ] 여러 사용자 계정 지원
- [ ] 템플릿 별 통계
- [ ] 엑셀 내보내기
- [ ] 다국어 지원
- [ ] 템플릿 공유 기능

## 📝 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

## 🤝 기여

개선 사항이나 버그 리포트는 GitHub Issues를 통해 등록해주세요.

## 📧 연락처

문제가 있거나 피드백이 있으시면 이슈를 등록해주세요.

---

**마지막 업데이트**: 2024년 1월
**버전**: 1.0.0
