#노드 클래스 생성
class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
#추가 함수
def insert(root, value):
    # 비어있으면 노드 생성
    if root is None:
        node = TreeNode()
        node.data = value
        return node
    # 루트 값보다 작으면 왼쪽으로 이동하여 재귀함수 호출
    if value < root.data:
        root.left = insert(root.left, value)
    else: # 루트 값보다 크면 오른쪽으로 이동하여 재귀함수 호출
        root.right = insert(root.right, value)
    return root

#search 함수
def search(root, value):
    current = root # 현재 탐색 중인 루트를 current로 지정
    while current:
        if value == current.data:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return None

#delete 함수
def delete(root, value):
    if root is None: # 루트 값이 없을 때 빈 루트 반환
        return root
    if value < root.data: # 작으면 왼쪽으로 이동하여 재귀함수 호출
        root.left = delete(root.left, value)
    elif value > root.data: #크면 오른쪽으로 이동하여 재귀함수 호출
        root.right = delete(root.right, value)
    else: #찾는 값과 동일할 때
        if root.left is None and root.right is None: # 리프 노드 일 때 none
            return None
        elif root.left is None: # 왼쪽이 비어 있으면 오른쪽으로 이동
            return root.right
        elif root.right is None: # 오른쪽이 비어 있으면 왼쪽으로 이동
            return root.left
        else:  # 자식이 두 개인 경우
            root.data = find_min(root.right).data # 루트의 값이 오른쪽 값의 최소값이 되어야 함
            root.right = delete(root.right, root.data)
    return root

# 오른쪽 값의 최소값을 찾는 함수
def find_min(node):
    current = node
    while current.left is not None: #왼쪽이 비지 않을 때마다 왼쪽으로 이동
        current = current.left
    return current
#후위 순회 방식
def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data} ", end='')


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    while True:
        print("\n--- 트리 관리 메뉴 ---")
        print("1. 값 삽입")
        print("2. 값 삭제")
        print("3. 값 찾기")
        print("4. 트리 확인 (후위 오더)")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        if choice == '1':
            value = int(input("삽입할 값을 입력하세요: "))
            root = insert(root, value)
            print(f"{value} 삽입 완료")
        elif choice == '2':
            value = int(input("삭제할 값을 입력하세요: "))
            if search(root, value):
                root = delete(root, value)
                print(f"{value} 삭제 완료")
            else:
                print(f"{value}은(는) 트리에 존재하지 않습니다.")
        elif choice == '3':
            value = int(input("찾고 싶은 값을 입력하세요: "))
            if search(root, value):
                print(f"{value}을(를) 찾았습니다.")
            else:
                print(f"{value}이(가) 존재하지 않습니다.")
        elif choice == '4':
            post_order(root)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")




