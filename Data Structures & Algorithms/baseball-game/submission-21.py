class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        answer = 0
        for x in operations:
            if x == "+":
                index1 = len(score)-1
                index2 = len(score)-2
                a = int(score[index1])
                b = int(score[index2])

                sumTwoPrevious = a + b
                score.append(sumTwoPrevious)
            elif x == 'D':
                doublePrevious = 2 * int(score[len(score)-1])
                score.append(doublePrevious)
            elif x == 'C':
                score.pop()
            else:
                score.append(int(x))

        for y in score:
            answer += int(y)

        return answer