class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0  else 1
        r = int(str(s*x)[::-1])
        return s* r * (r<2**31)


def main():
    s=Solution()
    x = 12233945
    result = s.reverse(x)
    print(result)

if __name__ == '__main__':
    main()