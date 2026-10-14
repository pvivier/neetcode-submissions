class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        counter_dic = Counter(t)
        dic = defaultdict(int)
        correct_keys = 0
        keys_goal = len(set(t))
        left = 0
        min_left, min_right = 0, 0
        window = deque()
        min_window = []
        for right, l in enumerate(s):
            dic[l] +=1
            if dic[l] == counter_dic[l]:
                correct_keys +=1

            while correct_keys == keys_goal:
                if left == 0:
                    min_right, min_left = right+1, left
                if right - left < min_right -1 - min_left:
                    min_left, min_right = left, right+1
                if dic[s[left]] == counter_dic[s[left]]:
                    correct_keys -=1
                dic[s[left]] -=1
                left +=1

        result = "".join(s[min_left:min_right])
        return result




        # while correct_keys != keys_goal:
        #     if right == len(s)-1:
        #         return ""
        #     right+=1
        #     window.append(s[right])
        #     build_dic[s[right]] +=1
        #     if build_dic[s[right]] == counter_dic[s[right]]:
        #         correct_keys +=1
        #     if correct_keys == keys_goal:
        #         best_string = window.copy()
        # print(build_dic)
        # while left < len(s) -1:
        #     print(window)
        #     print(correct_keys,  left)
        #     if correct_keys == keys_goal:
        #         print('pushing left')
        #         print(right, left, best_string)
        #         if right - left + 1 < len(best_string):
        #             print('in')
        #             print('setting best string')
        #             best_string = window.copy()
        #         if build_dic[s[left]] == counter_dic[s[left]]:
        #             print('in')
        #             print(s[left],build_dic[s[left]])
        #             correct_keys -= 1
        #         build_dic[s[left]] -= 1
        #         left +=1
        #         window.popleft()
        #     elif right == len(s)-1:
        #         result = "".join(best_string)
        #         return result
        #     else:
        #         print('pushing right')
        #         right += 1
        #         window.append(s[right])
        #         build_dic[s[right]] += 1
        #         if build_dic[s[right]] == counter_dic[s[right]]:
        #             correct_keys += 1
        # result = "".join(best_string)
        # return result
        
