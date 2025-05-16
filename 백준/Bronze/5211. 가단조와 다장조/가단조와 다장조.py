import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    music = list(input().split('|'))
    last = music[-1][-1]
    dic = dict()
    for m in music:
        if m[0] not in dic:
            dic[m[0]] = 1
        else:
            dic[m[0]] += 1
    minor = dic.get('A', 0) + dic.get('D', 0) + dic.get('E', 0)
    major = dic.get('C', 0) + dic.get('F', 0) + dic.get('G', 0)
    if major > minor:
        print('C-major')
    elif major < minor:
        print('A-minor')
    else:
        print('C-major' if last in ['C', 'F', 'G'] else 'A-minor')


if __name__ == '__main__':
    main()