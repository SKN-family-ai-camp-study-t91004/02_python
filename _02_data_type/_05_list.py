# sequence type(시퀀스 자료형)
# - str, list, tuple
# - 저장된 값의 순서가 유지됨
# - 인덱싱과 슬라이싱이 가능
# - 순회(iterable) 가능


# list
# - 여러 값(literal)을 묶어서 관리 (컨테이너 자료형)
# - 특징: 동적으로 list 크기가 변할 수 있다(수정 가능)
print("--- list ---")
lst = [1, 2, 3, 4, 5]
print("lst: ", lst)
print("len(lst): ", len(lst))
print("lst[0]: ", lst[0])
print("lst[1]: ", lst[1])
print("lst[4]: ", lst[4])

# list 저장 요소 추가/수정/삭제
# - list는 동적으로 크기 변경이 가능한 mutable 자료형이다!
# - mutable: list, set, dict
# - immutable: int, float, bool, str, tuple
print("--- list mutable check ---")
print("lst: ", lst)
print("추가 전 id: ", id(lst))

before_id = id(lst) # 이전 id

# list.append(값): list 끝에 값 추가
lst.append(999)
print('append 후 lst: ', lst)
print('append 후 lst id: ', id(lst))
print('append 전후 같은 list인가? ', before_id == id(lst))

# list.insert(index, 값)
# - index에 값을 삽입하는 메서드
# - 지정된 index 부터 뒤에 있는 모든 list 값의 index가 1씩 증가(밀려남)
print("--- list.insert() ---")
lst.insert(1, 1.5)
lst.insert(0, 0)
print("insert 후 lst: ", lst)
print("insert 후 lst id: ", id(lst))
print("insert 전후 같은 list인가? ", before_id == id(lst))

# list update(수정)
# list[인덱스] = 값 (변수에 값 대입해서 변경)
print('--- list update ---')
lst[0] = -10
print("lst: ", lst)

# 특정 인덱스 값 제거
# list.pop(index): 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print('--- list remove ---')
lst.pop(2)
print("lst: ", lst)
print('id(lst): ', id(lst))

# 2차원 list
print('--- 2차원 list ---')
students = [
    ['홍길동', 30], # 0번 [0][0]은 홍길동, [0][1]은 30
    ['이순신', 80], # 1번
    ['세종대왕', 100] # 2번
]

print("students: ", students)
print(students[0][0]) # 홍길동