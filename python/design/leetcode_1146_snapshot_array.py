
"""
author: Zhengjian Kang
date: 10/08/2020

https://leetcode.com/problems/snapshot-array/

1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the
given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total
number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we
took the snapshot with the given snap_id


Example 1:
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:
1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""


class SnapshotArray:
    def __init__(self, length: int):
        # initialize snap_id with 0 and we will create a nested dictioanries
        # to store snap_id as the key
        # and index and val as the pair of the value of the snap_id
        self.snap_id = 0
        self.snap_dic = collections.defaultdict(dict)

    def set(self, index: int, val: int) -> None:
        # here while setting up the value of the given index we are using
        # snap_id as the key of the main dictionary
        self.snap_dic[self.snap_id].update({index: val})

    def snap(self) -> int:
        # here we are taking the prev snapshot copy to map it with the updated
        # snap_id
        prev_snap = self.snap_dic[self.snap_id].copy()
        self.snap_id += 1
        self.snap_dic[self.snap_id] = prev_snap
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snap_dic:
            return 0
        elif index not in self.snap_dic[snap_id]:
            return 0
        else:
            return self.snap_dic[snap_id][index]
