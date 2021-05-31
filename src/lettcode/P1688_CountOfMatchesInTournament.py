"""
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team.
A total of n / 2 matches are played, and n / 2 teams advance to the next round.

If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired.
A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.

Return the number of matches played in the tournament until a winner is decided.


您得到了一个整数n，在一场比赛中团队数量具有奇怪规则:

如果当前的团队数是偶数，则每个团队将与另一个团队配对。
总共进行了n / 2场比赛，并且n / 2队进入下一轮。

如果当前的团队数是奇数，则其中一支队伍会随机进入比赛，而其余的则会配对。
总共进行（n-1）/ 2场比赛，并且（n-1）/ 2 +1支队伍进入下一轮。

返回比赛中的比赛次数，直到确定获胜者为止。


Example 1:

Input: n = 7
Output: 6

Explanation: Details of the tournament:
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.

Example 2:

Input: n = 14
Output: 13

Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.


Constraints:

1 <= n <= 200

"""


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        if n == 1:
            return result

        if n % 2 == 0:
            matches = n / 2
            advance_teams = n / 2
        else:
            matches = (n - 1) / 2
            advance_teams = (n - 1) / 2 + 1

        result += int(matches)
        result += self.numberOfMatches(int(advance_teams))

        return result
