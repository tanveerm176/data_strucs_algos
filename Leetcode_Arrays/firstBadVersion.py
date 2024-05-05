bad_version = 7


def isBad(n):
    return True if n >= bad_version else False

def createVersionList(n):
    versions = []

    for i in range(n):
        versions.append(i+1)
    return versions

def firstBadVersion(n):

    print(createVersionList(n))

    left = 1
    right = n

    while left < right:
        print(f'left = {left} and right = {right}')
        mid = (left+right)//2
        print(f'mid = {mid}')

        if isBad(mid) == True:
            right = mid
            print(f'isBad AND new right = {right}')
        else:
            left = mid + 1
            print(f'isNOTBad AND new left = {left} ({mid}+1)')
    
    print(f'final left = {left} and final right = {right}')
    return right




firstBadVersion(11)
