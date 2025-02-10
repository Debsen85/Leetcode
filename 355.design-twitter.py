#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List

class Tweet:

    def __init__(self, tweetId, userId):
        self.tweetId = tweetId
        self.userId = userId

class Twitter:

    def __init__(self):
        self.twitter = defaultdict(list)
        self.following = defaultdict(set)
        self.feedNumber = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feedNumber += 1
        self.twitter[userId].append((-self.feedNumber, Tweet(tweetId, userId)))

    def getNewsFeed(self, userId: int) -> List[int]:
        answer = []
        newsFeed = self.twitter[userId][:]
        
        for user in self.following[userId]:
            newsFeed.extend(self.twitter[user])

        heapq.heapify(newsFeed)

        while newsFeed and len(answer) < 10:
            if newsFeed[0][1].userId == userId or newsFeed[0][1].userId in self.following[userId]:
                answer.append(newsFeed[0][1].tweetId)
            heapq.heappop(newsFeed)

        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId) if followeeId in self.following[followerId] else None


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

