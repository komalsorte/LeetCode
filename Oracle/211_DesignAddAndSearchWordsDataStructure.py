"""
LeetCode - Medium
"""
"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current_node = self.root

        for w in word:
            if w not in current_node.children:
                current_node.children[w] = TrieNode()
            current_node = current_node.children[w]
        current_node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_recurse(self.root, word)

    def search_recurse(self, current_node, word):
        for i, w in enumerate(word):
            if w in current_node.children:
                current_node = current_node.children[w]

            elif w == "." and len(current_node.children)!=0:
                for node in current_node.children:
                    if self.search_recurse(current_node.children[node], word[i + 1:]):
                        return True
                    else:
                        return False
            else:
                return False

        return current_node.isEnd



# Your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("ab")
    print(obj.search("a"))
    print(obj.search(".."))
    print(obj.search("..."))