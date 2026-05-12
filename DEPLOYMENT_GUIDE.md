# 🚀 GitHub와 Streamlit Cloud 배포 가이드

## 📋 준비 사항

- GitHub 계정 ([github.com](https://github.com) 가입)
- Streamlit Cloud 계정 (GitHub 계정으로 로그인 가능)

---

## 1️⃣ GitHub 저장소 생성 및 파일 업로드

### 방법 A: GitHub 웹사이트에서 (가장 쉬움)

1. **GitHub 로그인**
   - https://github.com 접속
   - 오른쪽 상단의 프로필 아이콘 클릭

2. **새 저장소 생성**
   - "Your repositories" → "New" 클릭
   - 또는 "+" 아이콘 → "New repository" 클릭

3. **저장소 설정**
   - **Repository name**: `patient-message-template`
   - **Description**: 환자 문자 템플릿 관리 시스템
   - **Public** 선택 (모두가 볼 수 있음)
   - "Add a README file" 체크 해제 (우리가 이미 만들었음)
   - **Create repository** 클릭

4. **파일 업로드**
   - 새로 만든 저장소 페이지 접속
   - "Add file" → "Upload files" 클릭
   - 다음 파일들을 드래그&드롭 또는 선택해서 업로드:
     ```
     app.py
     requirements.txt
     README.md
     .gitignore
     .streamlit/config.toml
     ```
   - 하단 "Commit changes" 클릭

### 방법 B: 명령어로 업로드 (GitHub Desktop 또는 터미널)

**Windows/Mac/Linux 터미널 사용:**

```bash
# 1. 디렉토리 이동
cd /home/claude

# 2. git 초기화
git init

# 3. GitHub 설정
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 4. 모든 파일 추가
git add .

# 5. 커밋
git commit -m "Initial commit: Patient message template management system"

# 6. 브랜치 이름 변경 (main으로)
git branch -M main

# 7. 원격 저장소 추가
git remote add origin https://github.com/YOUR_USERNAME/patient-message-template.git

# 8. 푸시
git push -u origin main
```

> **YOUR_USERNAME**을 본인의 GitHub 사용자명으로 바꾸세요!

---

## 2️⃣ Streamlit Cloud로 배포

### 단계별 가이드

#### 1단계: Streamlit Cloud에 접속
1. https://share.streamlit.io 접속
2. "Sign in with GitHub" 클릭
3. GitHub 로그인

#### 2단계: 새 앱 배포
1. "New app" 버튼 클릭
2. 다음 정보 입력:
   - **Repository**: `YOUR_USERNAME/patient-message-template`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. **Deploy** 클릭

#### 3단계: 배포 대기
- "Building..." 상태에서 대기
- 2-3분 후 자동으로 배포 완료
- 배포 완료 URL 받음!

### 배포 완료 후 URL 형식
```
https://share.streamlit.io/YOUR_USERNAME/patient-message-template
```

---

## 📱 배포 후 사용 방법

### 웹에서 접속
- 배포된 URL을 주소창에 입력
- 또는 모바일에서도 접속 가능

### 공유
- 배포 URL을 동료들에게 공유
- 누구나 웹브라우저에서 사용 가능

### 데이터 업데이트
- GitHub에 파일 업로드 후 자동으로 반영됨
- 약 1-2분 후 Streamlit Cloud에서 다시 빌드

---

## 🔧 수정 사항 적용

코드를 수정하고 싶을 때:

### 1. 로컬에서 수정
```bash
# 예: app.py 수정
# ...코드 수정...

# GitHub에 업로드
git add app.py
git commit -m "Fix: 버그 수정"
git push
```

### 2. Streamlit Cloud에서 자동 반영
- GitHub에 푸시되면 자동으로 재배포
- 약 1-2분 후 변경사항 반영

---

## 🆘 트러블슈팅

### "Repository not found" 에러
```
해결: 
1. GitHub 저장소가 Public인지 확인
2. 저장소명 정확한지 확인 (대소문자 구분)
3. YOUR_USERNAME을 정확히 입력했는지 확인
```

### Streamlit Cloud 배포 실패
```
해결:
1. requirements.txt 파일이 있는지 확인
2. app.py 파일이 있는지 확인
3. GitHub 저장소 공개 여부 확인
4. Streamlit 로그 확인:
   - Streamlit Cloud 대시보드에서 "Logs" 탭 확인
```

### 변경사항이 반영되지 않음
```
해결:
1. GitHub에 제대로 push 되었는지 확인
2. GitHub에서 파일 업로드 확인
3. 5분 정도 기다렸다가 새로고침
4. Streamlit Cloud의 "Reboot" 버튼 클릭
```

---

## 📊 배포 후 관리

### Streamlit Cloud 대시보시보드
- https://share.streamlit.io/admin 접속
- 배포된 앱 목록 확인
- 앱 설정, 로그, 통계 확인 가능

### 앱 설정
- **Settings** → "Advanced settings"에서:
  - 맞춤 도메인 설정
  - 비밀번호 보호 (필요시)
  - 앱 description 수정

---

## 💡 팁

### 1. README 수정
- GitHub에서 README.md 직접 수정 가능
- "Edit this file" 펜 아이콘 클릭

### 2. 정기적 백업
```bash
# 로컬 백업 (주기적으로)
git pull
```

### 3. 여러 팀원이 사용할 경우
- GitHub에 다른 사용자를 Collaborator로 추가
- Settings → Collaborators → Add people

---

## 🎯 완성 체크리스트

- [ ] GitHub 계정 생성
- [ ] 저장소 생성 (patient-message-template)
- [ ] 파일 업로드 완료
- [ ] Streamlit Cloud 계정 생성
- [ ] 앱 배포 완료
- [ ] 배포 URL 테스트
- [ ] 동료들과 URL 공유
- [ ] 첫 번째 템플릿 추가

---

## 📚 추가 자료

- [Streamlit 공식 문서](https://docs.streamlit.io)
- [GitHub 가이드](https://guides.github.com)
- [Streamlit Cloud FAQ](https://discuss.streamlit.io)

---

**배포가 완료되면 축하합니다! 🎉**
이제 언제 어디서나 환자 문자 템플릿을 관리할 수 있습니다!
