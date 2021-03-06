"# data-structures" 

-=STACK=-

A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO.

There are 3 implementations of the stack using different data structures:

1. List
Pros:
- list is the most familiar structure used in these implementations
Cons:
- some append calls may take longer than others due to the contiguous arrangement of list items in memory
- list is not thread-safe

2. Deque from collections
Pros:
- interface same as list
- append and pop operations are atomic (thread-safe)
Cons:
- operations with deque except append and pop is not thread-safe

3. LifoQueue from queue
Pros:
- full thread-safe
Cons:
- unfamiliar data structure with interface other than list and deque
- may be slow due to multi-threading design 



-=QUEUE=-

A queue is a data structure that stores items in an First-In/First-Out manner. This is frequently referred to as FIFO.

There are 4 implementations of the stack using different data structures:

1. List
Pros:
- list is the most familiar structure used in these implementations
Cons:
- some append calls may take longer than others due to the contiguous arrangement of list items in memory
- list is not thread-safe

2. Deque from collections
Pros:
- interface same as list
- append and pop operations are atomic (thread-safe)
Cons:
- operations with deque except append and pop is not thread-safe

3. Queue from queue
Pros:
- design for multi-threading
Cons:
- unfamiliar data structure with interface other than list and deque
- may be slow due to multi-threading design

4. Queue from multiprocessing
Pros:
- design for multiprocessing
Cons:
- unfamiliar data structure with interface other than list and deque
- may be slow due to multiprocessing design