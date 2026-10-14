class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        window = deque()
        dic_of_counts = defaultdict(int)
        left = 0
        right = 0
        #dic_of_counts[string[right]] +=1
        biggest_entry_in_dic_of_counts = 0
        max_window =0
        len_window = 0
        while right <= len(string):
            if biggest_entry_in_dic_of_counts >= len_window - k:
                max_window = max(max_window, len_window)
                if right == len(string):
                    return max_window
                right +=1
                len_window +=1
                dic_of_counts[string[right-1]] +=1
                if dic_of_counts[string[right-1]] > biggest_entry_in_dic_of_counts:
                    biggest_entry_in_dic_of_counts = dic_of_counts[string[right-1]]
            else:
                dic_of_counts[string[left]] -= 1
                left +=1
                len_window -= 1
            print(max_window)
        return max_window













        # window = deque()
        # dic_of_counts = defaultdict(int)
        # replacements = 0
        # current_character = string[0]
        # max_len = 0
        # for i, l in enumerate(string):
        #     if l == current_character:
        #         window.append(l)
        #         dic_of_counts[l] +=1
        #         max_len = max(max_len, min(len(string), len(window) +k-replacements))
        #     elif replacements < k:
        #         window.append(l)
        #         dic_of_counts[l] +=1
        #         replacements+=1
        #         max_len = max(max_len, min(len(string), len(window) +k-replacements))
        #     else:
        #         while (len(window)!=0) and (window[0] == current_character):
        #             window.popleft()
        #             dic_of_counts[current_character]-=1
        #         window.append(l)
        #         dic_of_counts[l]+=1
        #         current_character = window[0]
        #         how_many_in_string = dic_of_counts[current_character]
        #         replacements = len(window)-how_many_in_string
        #     print(window)
        # print(replacements)
        # while len(window) != 0:
        #     current_character = window[0]
        #     how_many_in_string = dic_of_counts[current_character]
        #     replacements = len(window)-how_many_in_string
        #     max_len = max(max_len, min(len(string),len(window) + k - replacements))
        #     window.popleft()
        #     dic_of_counts[current_character]-=1
        # # if replacements < k:
        # #     margin = k-replacements
        # #     if len(window) + margin >max_len:
        # #         max_len = min(len(string), len(window) + margin)
        # return max_len


