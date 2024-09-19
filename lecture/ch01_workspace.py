#주석(comment): 실행 x, 메모

# 1. 출력함수(print)
# 

# c언어
# - ''(char) - 문자형
# - ''(string) - 문자열형
# Python
# - '' or "" - 문자열형(String)
print("hello")


# 1. 영어 대소문자, 숫자, 특수문자(_, -)만 사용!
# 2. 숫자로 시작할 수 없음
#    abc123(o), 123abc(x)

# 8. 네이밍 메서드
#   -변수, 함수, 클래스 등의 사용자 정의 이름에 사용하는 기법
#   -프로그래밍 언어별로 Naming Method가 다름\

# 가. PascalCase    (St)
# 나. camelCase
# 다. snake_case
# 라. kebab_case

# 9.
student_num = 24
name = "홍길동"

print("조선대학교 24학번 홍길동입니다") #하드코딩
print("조선대학교 {}학번 {}입니다.".format(student_num, name))