#문자열의 이해(String)
#   - 데이터 분석
#   - 자연어 처리
#   - 유효성 체크(사용자로부터 입력받은 값 체크)


# 문제1. "cherry1004@gmail.com" , "cherry01@gmail.com", "cherry0@gmail.com" 에서
#         아이디만 추출하는 코드 작성
# 
# 문제2. 
# www.naver.com
# www.daum.net
# www.google.com
# naver, daum, google만 추출 

name1 = "cherry1004@gmail.com"
name2 = "cherry01@gmail.com"
name3 = "cherry0@gmail.com"

print(name1[0:name1.find("@")])


url1 = "www.naver.com"
print(url1[url1.index(".",0,5)+1:url1.index(".",6)])