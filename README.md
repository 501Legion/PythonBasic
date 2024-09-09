## 1. 개발환경 구축
### 1-1. 다운로드
- anaconda
- vscode

### 1-2. 아나콘다 세팅
- conda env list    (가상화면 목록 보기)
- conda create -n developer python=3.11 (가상화면 생성)
- conda activate developer  (가상화면 접속)
- pip list                   (라이브러리 목록)
- pip install pandas        (pandas 라이브러리 설치)
- cls                       (화면 클리어)

### 1-3. VSCODE 세팅
1. Extensions 설치
    - Python
    - Prettier
    - Python Extension Pack
    - Atom Material Theme
    - Atom Material Icons
2. Settings
    - [Mouse Wheel Zoom] 켜기
3. Theme 설정
4. 아나콘다 가상환경 주입
    - [Ctrl] + [Shift] + [p] -> "Python: Select Interpreter" 클릭 후
    "developer" 가상환경 선택

### 1-4. 명령어 단축키
- [Ctrl] + [,] : Settings 열기
- [Ctrl] + [`] : 터미널 열기