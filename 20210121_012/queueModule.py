#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Queue:
    def __init__(self, size = 5):
        self.queue = []  # 큐 역할을 할 빈 리스트
        self.size = size # 큐의 크기
        self.rear = 0    # 큐의 뒤쪽 포인터 => 큐에 데이터가 입력될 때 마다 1씩 증가한다.
        self.front = 0   # 큐의 앞쪽 포인터 => 큐에서 데이터가 제거될 때 마다 1씩 증가한다.
        
    # add => 입력
    def add(self, data):
        if data not in self.queue:
            if self.size > self.rear:   # overflow?
                self.queue.append(data) # 큐에 데이터 입력
                self.rear += 1          # 큐에 데이터를 추가했으므로 rear를 1증가 시킨다.
                print('큐에 {}을(를) 저장합니다. '.format(data), end = '')
                print('rear = {}, front = {}'.format(self.rear, self.front))
            else:
                print('overflow 발생... 큐가 가득차서 {}를(을) 저장할 수 없습니다.'.format(data))
            # ===== if 끝
        else:
            print('{}는(은) 중복되는 데이터 입니다.'.format(data))
        # ===== if 끝
        self.view()
    
    # remove => 출력
    def remove(self):
        # underflow 인가 검사한다.
        if self.rear <= 0 or self.rear == self.front:
            print('큐에 저장된 데이터가 없습니다.')
        else:
            data = self.queue[self.front] # 큐에 저장된 제거할 데이터를 얻어온다.
            self.queue[self.front] = ''   # 얻어온 데이터를 제거한다.
            self.front += 1               # 데이터를 제거했으므로 front를 1증가 시킨다.
            print('큐에서 제거된 데이터 : {}'.format(data), end = ', ')
            print('rear = {}, front = {}'.format(self.rear, self.front))
            self.view()
    
    # view => 스택에 저장된 데이터 보기
    def view(self):
        print('큐에 저장된 데이터 => ', end = '')
        # underflow 인가 검사한다. 큐는 underflow 조건이 2가지가 있다.
        # 큐에 데이터가 한 건도 입력되지 않았을 경우 rear가 0이므로 underflow가 발생된다.
        # 큐에 데이터가 입력된 후 입력된 데이터가 모두 제거되면 rear와 front가 같아지게 되면서 underflow가 발생된다.
        if self.rear <= 0 or self.rear == self.front:
            print('없음', end = '')
        else:
            # 큐에 저장된 데이터가 있으므로 front 번째 인덱스의 데이터부터 rear - 1 번째 인덱스의 데이터까지 출력한다.
            for i in range(self.front, self.rear):
                print(self.queue[i], end = ' ')
        # ===== if 끝
        print()


# In[43]:


if __name__ == '__main__':
    queue = Queue()
    queue.view()
    queue.remove()
    queue.add(111)
    queue.add(222)
    queue.add(333)
    queue.add(444)
    queue.add(222)
    queue.add(555)
    queue.add(666)
    print('=' * 80)
    queue.view()
    print('=' * 80)
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()


# In[ ]:




