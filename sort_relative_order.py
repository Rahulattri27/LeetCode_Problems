def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        new_ls=[]
        for i in arr2:
            while i in arr1:
                arr1.remove(i)
                new_ls.append(i)
        # print(new_ls+arr1)
        arr1=sorted(arr1)
        return new_ls+arr1

        