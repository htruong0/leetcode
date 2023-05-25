class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for c in t:
            t_counts[c] = 1 + t_counts.get(c, 0)
        # don't care about characters not in t
        s_counts = {c: 0 for c in t}
        # increment when same count in s_count and t_count
        counter = 0
        # valid substring when counter == target
        target = len(t_counts)
        left = 0
        # pointers to return substring
        pointers = [0, 0]
        minL = float("inf")

        for right, c in enumerate(s):
            if c in s_counts:
                s_counts[c] += 1
                if s_counts[c] == t_counts[c]:
                    counter += 1

            # iterate solution to find minimum length substring
            while counter == target:
                if (right+1-left) < minL:
                    pointers = [left, right]
                    minL = right+1-left
                if s[left] in t_counts:
                    s_counts[s[left]] -= 1
                    if s_counts[s[left]] < t_counts[s[left]]:
                        counter -= 1
                left += 1

        # possible that there isn't a substring
        if minL != float("inf"):
            left, right = pointers
            return s[left:right+1]
        else:
            return ""