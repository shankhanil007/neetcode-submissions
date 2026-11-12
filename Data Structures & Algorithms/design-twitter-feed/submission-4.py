class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Twitter:

    def __init__(self):
        self.follows = {}
        self.userTweets = {}
        self.timer = 1
        self.tweetTimings = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.userTweets.get(userId, None) != None:
            self.userTweets[userId].append(tweetId)
        else:
            self.userTweets[userId] = [tweetId]
        self.tweetTimings[tweetId] = self.timer
        self.timer += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        seen = set()
        head = self.follows.get(userId, None)
        while head != None:
            fid = head.val
            for tweet in self.userTweets.get(fid, []):
                seen.add(tweet)
                heapq.heappush(maxHeap, (self.tweetTimings[tweet]*-1, tweet))
            head = head.next
        for tweet in self.userTweets.get(userId, []):
            if tweet not in seen:
                heapq.heappush(maxHeap, (self.tweetTimings[tweet]*-1, tweet))
        feedList = []
        for itr in range(0, 10):
            if maxHeap:
                feed = heapq.heappop(maxHeap)
                feedList.append(feed[1])
        return feedList


    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId, None):
            self.follows[followerId] = Node(followeeId)
        else:
            head = self.follows[followerId]
            while head.next != None:
                if head.val == followeeId:
                    return
                head = head.next
            if head.val != followeeId:
                head.next = Node(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        head = self.follows.get(followerId, None)
        dummy = Node(-1)
        dummy.next = head
        prev, nxt = dummy, None

        while head != None:
            nxt = head.next
            if head.val == followeeId:
                prev.next = nxt
                head.nxt = None
            prev = head
            head = nxt
        self.follows[followerId] = dummy.next
        
