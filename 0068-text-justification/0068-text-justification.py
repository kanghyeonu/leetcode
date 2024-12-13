class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        s = ""
        for word in words:
            if len(s + word) > maxWidth:
                word_list = s.strip().split(" ")
                rest_space = maxWidth - len("".join(word_list))
                s = word_list[0]
                # only too long a word
                if len(word_list) == 1:
                    s = " " * maxWidth
                    s = word_list[0] + s[len(word_list[0]):]
                # distribute space among words
                else:
                    base_space = rest_space // (len(word_list) - 1)
                    remainder = rest_space % (len(word_list) - 1)
                    distribution = [base_space] * (len(word_list) - 1)
                    
                    for i in range(remainder):
                        distribution[i] += 1

                    for i, w in enumerate(word_list[1:]):
                        s += (" " * distribution[i]) + w
                    
                answer.append(s)
                s = word + " "
            # fit
            elif len(s + word) == maxWidth:
                s += word
                answer.append(s)
                s = ""
            # s < maxWidth
            else:
                s += word + " " 

        
        # rest words
        if len(s) > 0:
            word_list = s.strip().split(" ")
            s = " ".join(word_list)
            s += " " * (maxWidth - len(s))
            answer.append(s)

        return answer