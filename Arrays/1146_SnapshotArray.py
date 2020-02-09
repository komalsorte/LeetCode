"""
Medium
"""


"""
issue with arrays - memory limit exceeds
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.array = [0] * length
        self.snap_ids_dict = dict()
        self.count = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snap_ids_dict[self.count] = list(self.array)
        self.count += 1
        return self.count - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_id_arr = self.snap_ids_dict[snap_id]
        return snap_id_arr[index]


# Your SnapshotArray object will be instantiated and called as such:
if __name__ == '__main__':
    obj = SnapshotArray(4)
    print(obj.snap())
    print(obj.snap())
    print(obj.get(3,1))
    obj.set(2,4)
    print(obj.snap())
    obj.set(1,4)

    print("---------")
    obj = SnapshotArray(3)
    obj.set(0, 1)
    obj.set(2, 17)
    obj.set(0, 19)
    print(obj.snap())
    print(obj.snap())
    print(obj.get(0, 0))
    print(obj.snap())
    print(obj.get(1, 1))
    print(obj.get(2, 0))

    """
    ["SnapshotArray","snap","snap","get","set","snap","set"]
[[4],[],[],[3,1],[2,4],[],[1,4]]

["SnapshotArray","set","set","set","snap","snap","get","snap","get","get"]
[[3],[0,1],[2,17],[0,19],[],[],[0,0],[],[1,1],[2,0]]

Expected: [null,null,null,null,0,1,19,2,0,17]
    """
