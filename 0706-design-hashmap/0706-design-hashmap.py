class MyHashMap:

    def __init__(self):
        self.diction = {}

    def put(self, key: int, value: int) -> None:
        self.diction[key] = value

    def get(self, key: int) -> int:
        if key in self.diction:
            return self.diction[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.diction:
            del(self.diction[key])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)