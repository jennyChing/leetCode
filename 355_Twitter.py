'''
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''
import collections
import heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post_dict = collections.defaultdict(list)
        self.follow_dict = collections.defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.timestamp += 1
        self.post_dict[userId].append((self.timestamp, tweetId))
        self.follow_dict[userId] = {userId}

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        #posts = self.post_dict[userId] # can't make them the same mutable object!
        if self.follow_dict[userId] == []:
            return []
        posts = []
        for f in self.follow_dict[userId]:
            posts += self.post_dict[f]
        return [h[1] for h in  heapq.nlargest(10, posts)]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follow_dict[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
if __name__ == "__main__":
    obj = Twitter()
    obj.postTweet(1, 5)
    param_2 = obj.getNewsFeed(1)
    print(param_2)
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    param_2 = obj.getNewsFeed(1)
    print(param_2)
    obj.unfollow(1, 2)
    param_2 = obj.getNewsFeed(1)
    print(param_2)

