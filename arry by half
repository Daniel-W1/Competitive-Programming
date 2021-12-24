def minSetSize(arr):
        the_dict={}
        for i in arr:
            the_dict[i]=0
        for i in arr:
            the_dict[i]+=1
        the_list=list(the_dict.items())
        the_list=sorted(the_list, key=lambda item: item[1], reverse= True)
        the_ans=[item[1] for item in the_list]
        cnt=0
        sum=0
        for i in the_ans:
            sum+=i
            cnt+=1
            if sum> len(arr)/2:
                break
        return cnt, the_ans
print(minSetSize([1,1,1,1,2,2]))
