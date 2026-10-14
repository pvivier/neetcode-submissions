class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0 for i in range(len(temperatures))]
        dic = defaultdict(int)
        
        for i,t in enumerate(temperatures):
            print('here are i and t :', i,t)
            dic[i] = [0,t]
            todelete = []
            for j,prevtemp in dic.items():
                if j==i:
                    continue
                print('here are j and prevtemp:', j, prevtemp)
                prevtemp[0] += 1
                if t > prevtemp[1]:
                    out[j] = prevtemp[0]
                    todelete.append(j)
            for j in todelete:
                print('hello')
                del dic[j]
            print(dic)
        return out






        # dic = defaultdict(list)
        # final_dic = defaultdict(int)
        # d = deque()
        
        # for i,t in enumerate(temperatures):
        #     if not d:
        #         d.appendt(t)
        #         dic[i] = [t,0]
        #     else:
        #         for j, val in dic.items():
        #             if dic[j][0] > t:
        #                 dic[j][1] +=1
        #             else:
        #                 finaldic[j] = dic[j][1] + 1
        #                 del dic[j]
            