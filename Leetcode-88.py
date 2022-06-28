if __name__ == "__main__":
    nums1 = list(map(int,input().split()))
    m = int(input())
    nums2 = list(map(int,input().split()))
    n = int(input())
    l = list()
    for i in range(m):
        l.append(nums1[i])
    for i in range(n):
        l.append(nums2[i])
    l.sort()
    nums1.clear()
    for i in range(len(l)):
        nums1.append(l[i])
    print(nums1)
        