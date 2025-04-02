class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key, last=True) # 사용했으니 끝으로 이동
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # evict
        if key not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last=False)  # dict에서 가장 마지막에 있는거 삭제
            
        self.cache[key] = value
        self.cache.move_to_end(key, last=True) # 기존 값이 최신화


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)