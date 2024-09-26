#컬렉션 프레임워크
#   1. 리스트(List)
#   2. 튜플
#   3. 딕셔너리
#   4. 세트

# * 순서가 있는 자료형: 리스트, 튜플 ->기차
# * 순서가 없는 자료형: 딕셔너리, 세트 -> 복주머니

# 1. 리스트 

a = []
a = [1, 5, 2]
c = [1, 0.2, "chosun", True, [1,2]]

["a", "b", "c"] #패킹
a, b, c = ["a", "b", "c"] #언패킹

test = [1,2,3]
# 가. append()
# 나. insert()
# 다. extent()
# 라. remove()
# 마. pop()
# 바. index()
test.index(1)

# 사. sorted()
#   +sort() : 원본값을 정렬(원본값 상실)
#   +sorted() : 복제본을 정렬(원본값 유지)

print(sorted(a)) # 오름차순
print(sorted(a, reverse=True))


# 2. 튜플
# 인덱스
# packing과 unpacking 가능
# immutable 생성 후 변경 불가
# 함수 리턴 값 tuple 값

a= [1,2,3]
b= (1,2,3)
d=(5)
num = 3
d = 5,

# 딕셔너리 == JSON
# json(파일로 공유)
# {key : value} 주고 -> key value 1 pair
member = {
    "id": "3ad"

}