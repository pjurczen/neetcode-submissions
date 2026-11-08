from collections import defaultdict
from collections import deque

class Tweet:
    userId: int
    tweetId: int
    time: int

    def __init__(self, userId: int, tweetId: int, time: int):
        self.userId = userId
        self.tweetId = tweetId
        self.time = time

    def __str__(self) -> str:
        return f"Tweet[userId={self.userId}, tweetId={self.tweetId}, time={self.tweetId}]"

    def __repr__(self) -> str:
        return self.__str__()

class Twitter:

    follows: dict[int, set[int]] # [followerId, set[followeeId]]
    followers: dict[int, set[int]] # [followeeId, set[followerId]]
    tweets: dict[int, deque[Tweet]] # [userId, list[tweet]]
    feeds: dict[int, deque[Tweet]] # [userId, list[tweet]]
    time: int

    def __init__(self):
        self.follows = defaultdict(set)
        self.followers = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.feeds = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweet = Tweet(userId, tweetId, self.time)
        self.tweets[userId].appendleft(newTweet)
        self.feeds[userId].appendleft(newTweet)
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        if len(self.feeds[userId]) > 10:
            self.feeds[userId].pop()
        for follower in self.followers[userId]:
            self.feeds[follower].appendleft(newTweet)
            if len(self.feeds[follower]) > 10:
                self.feeds[follower].pop()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        return [t.tweetId for t in self.feeds[userId]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
        self._rebuildFeed(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
            self.followers[followeeId].remove(followerId)
            self._rebuildFeed(followerId)

    def _rebuildFeed(self, userId: int) -> None:
        feed = []
        feed.extend(self.tweets[userId])
        for followee in self.follows[userId]:
            feed.extend(self.tweets[followee])
        feed.sort(key=lambda t: -t.time)
        feed = feed[:10]
        self.feeds[userId] = deque(feed)

        
