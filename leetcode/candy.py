"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
__author__ = 'Yang'

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        num = len(ratings)

        if not num:    return 0
        elif num == 1:    return 1
        elif num == 2:    return 2

        else:
            indexmin = ratings.index(min(ratings))
            if indexmin == 0:
                left = 0
                right = self.candyRight(ratings)
            elif indexmin == len(ratings) - 1:
                left = self.candyLeft(ratings)
                right = 0
            else:
                right = self.candyRight(ratings[indexmin: ])
                left = self.candyLeft(ratings[: indexmin+1]) - 1

            return left + right

    def candyRight(self, ratings):
        length = len(ratings)
        candies = [0] * length
        candies[0] = 1
        prior = ratings[0]

        if length == 1:
            return 1

        else:
            index = 1
            while(1 <= index < length):
                now = ratings[index]
                if now > prior:
                    candies[index] = candies[index - 1] + 1
                    prior = now
                    index += 1

                elif now == prior:
                    candies[index] = 1
                    index += 1

                else:
                    candies[index] = 1

                    if candies[index] == candies[index - 1]:
                        bindex = index
                        while(bindex >= 1 and ratings[bindex] < ratings[bindex-1]
                              and candies[bindex] == candies[bindex-1]):
                            candies[bindex - 1] += 1
                            bindex -= 1
                    prior = now
                    index += 1
            return sum(candies)


    def candyLeft(self, ratings):
        ratings.reverse()
        return self.candyRight(ratings)


if __name__ == "__main__":
    ratings = [2, 3, 8, 4, 1, 5, 5, 4, 2, 8, 6, 3, 5, 6, 6]
    ratings1 = [2, 3, 8, 4, 1]
    ratings2 = [1, 4, 8, 3, 2]
    ratings3 = [58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89]
    rating3Left = [58, 21, 72, 77, 48, 9, 38, 71, 68, 77, 82, 47, 25, 94, 89, 54, 26, 54, 54, 99, 64, 71, 76, 63, 81, 82, 60, 64, 29, 51, 87, 87, 72, 12, 16, 20, 21, 54, 43, 41, 83, 77, 41, 61, 72, 82, 15, 50, 36, 69, 49, 53, 92, 77, 16, 73, 12, 28, 37, 41, 79, 25, 80, 3, 37, 48, 23, 10, 55, 19, 51, 38, 96, 92, 99, 68, 75, 14, 18, 63, 35, 19, 68, 28, 49, 36, 53, 61, 64, 91, 2]
    rating3Right = [2, 43, 68, 34, 46, 57, 82, 22, 67, 89]
    s = Solution()
    print s.candy(rating3Left) - 1
    # print s.candy(rating3Right)
    print s.candyRight(rating3Right)
    print s.candyLeft(rating3Left) - 1




