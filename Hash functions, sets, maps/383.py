class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_char = {}
        note_char = {}
        answer = True

        for c in magazine:
            if c in mag_char:
                mag_char[c] += 1  
            else:
                mag_char[c] = 1
        
        for c in ransomNote:
            if c in note_char:
                note_char[c] += 1 
            else:
                note_char[c] = 1
            if c not in mag_char:
                mag_char[c] = 0

        for c in note_char:
            if note_char[c] > mag_char[c]:
                answer = False
        
        return answer
