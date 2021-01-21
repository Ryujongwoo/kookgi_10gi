#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Stack:
    # Stack 클래스가 생성될 때 스택의 크기를 넘겨받으면 넘겨받은 크기 만큼의 기억 공간을 가지는 스택을 생성하고 크기를 넘겨받지
    # 않으면 5개의 데이터를 저장할 수 있는 스택을 만든다. => 디폴트 인수를 사용하면 된다. => 변수명 = 기본값
    def __init__(self, size = 5):
        # print('스택의 크기는 {}개'.format(size))
        # 생성자 함수에서 트택을 만든다.
        self.stack = []  # stack => 빈 리스트 => 데이터는 append() 메소드로 추가한다.
        self.size = size # 스택의 크기
        # top, SP(Stack Pointer) => stack에 몇 개의 데이터가 저장되어있나 기억한다. => 데이터가 입력되면 1증가, 출력되면 1감소
        self.top = 0
    
    # push => 입력
    def push(self, data):
        if data not in self.stack: # 스택에 추가하려는 데이터가 스택에 존재하지 않는가?
            # overflow 인가 검사한다.
            # 스택의 크기(self.size)가 5일때 스택으로 사용할 리스트의 인덱스(self.top)는 0, 1, 2, 3, 4만 사용할 수 있다.
            if self.size > self.top:
                # overflow가 발생되지 않았으므로 스택에 데이터를 저장한다.
                self.stack.append(data)
                # 스택에 데이터를 추가했으므로 top을 1증가 시킨다.
                self.top += 1
            else:
                # overflow가 발생되면 스택이 가득찼다는 메시지를 출력한다.
                print('overflow 발생... 스택이 가득차서 {}를(을) 저장할 수 없습니다.'.format(data))
            # ===== if 끝
        else:
            # 추가하려는 데이터가 스택에 존재하기 때문에 중복되는 데이터라고 메시지를 출력한다.
            print('{}는(은) 중복되는 데이터 입니다.'.format(data))
        # ===== if 끝
        # 스택에 저장된 데이터를 출력하는 메소드(view)를 실행한다.
        self.view()
    
    # pop => 출력
    def pop(self):
        # underflow 인가 검사한다.
        if self.top <= 0:
            print('스택에 저장된 데이터가 없습니다.')
        else:
            # 파이썬 리스트의 메소드 중에서 pop() 메소드를 사용해서 스택에 저장된 데이터를 얻어온 후 리스트에서 제거한다.
            data = self.stack.pop() # 스택으로 사용하는 리스트의 마지막 인덱스 위치의 데이터를 얻어와서 data에 저장한 후 제거한다.
            self.top -= 1           # 스택에 저장된 데이터가 출력되었으므로 top을 1감소 시킨다.
            print('pop 데이터 : {}'.format(data), end = ', ')
            self.view()
    
    # view => 스택에 저장된 데이터 보기
    def view(self):
        print('스택에 저장된 데이터 => ', end = '')
        # underflow 인가 검사한다.
        if self.top <= 0:
            # 스택에 저장된 데이터가 없으므로 없다고 출력한다.
            print('없음', end = '')
        else:
            # 스택에 저장된 데이터의 개수만큼 반복하며 스택에 저장된 데이터를 출력한다.
            for i in range(self.top):
                print(self.stack[i], end = ' ')
        # ===== if 끝
        print()


# In[19]:


# 현재 파일이 다른 파일에 모듈로 import 될 때 if __name__ == '__main__': 내부에 코딩한 내용은 자동으로 실행되지 않는다.
if __name__ == '__main__':
    # 테스트 코드
    stack = Stack()
    stack.view()
    stack.pop()
    stack.push(111)
    stack.push(3.141592)
    stack.push('수요일')
    stack.push(True)
    stack.push(111)
    stack.push(555)
    stack.push(777)
    print('=' * 80)
    stack.view()
    print('=' * 80)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




