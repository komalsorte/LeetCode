"""
LeetCode - Medium
"""
"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False  # whether this node is an end of a word
        self.children = dict()  # map a char to the child node


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()

            currNode = currNode.children[c]

        currNode.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return currNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root

        for c in prefix:
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]

        return True


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")
    trie.insert("apple")
    trie.search("apple")
    trie.search("app")
    trie.startsWith("app")
    trie.insert("app")
    trie.search("app")
