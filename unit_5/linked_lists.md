# Linked Lists
* what is meant by the notion that arrays cannot dynamically grow like linked lists can?
    1. Arrays
        - An array is a contiguous block of memory. This means all elements are stored one after another in memory.
        - When you create an array, you usually specify its size (e.g., arr = [0] * 10 in Python or int arr[10] in C). The system allocates exactly enough memory for that size.
        - Problem with growth: If you want to add more elements than the array currently has space for:
        - There might not be free contiguous memory right after the array.
        - The array must be copied to a new, larger block of memory to accommodate the new elements.
        - This copying operation can be costly (O(n) time), and it’s not automatic in lower-level languages like C/C++. Even in high-level languages (like Python or Java), the language runtime handles it, but it’s still behind-the-scenes copying.
    2. Linked Lists
        - A linked list is made of nodes, each storing data and a pointer to the next node.
        - Nodes can be scattered anywhere in memory, linked together by pointers.
        - Growth is easy: To add a new element, you simply allocate a new node and update the pointers. No need to copy the entire list or find contiguous memory.
    * In short: Arrays have a fixed memory layout that makes growing them costly, while linked lists can grow easily because their nodes are connected via pointers and don’t need contiguous memory.

