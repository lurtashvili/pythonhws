# მასივის დასორტირება mergeSort-ით
def mergeSort(array):
    if len(array) > 1:
        # მასივის შუა წერტილი
        r = len(array) // 2
        # მასივის ორ ნაწილად გაყოფა
        L = array[:r]
        M = array[r:]
        # რეკურსიულად დალაგება ამ ორი ნახევრის
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        # დალაგებული ნახევრების თავდაპირველ მასივში დაკავშირება
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # არის თუ არა დარჩენილი ელემენტები L ან M-ში და მათი გაერთიანებულ მასივში დამატება
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
# მასივის ელემენტების ბეჭვდა
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

