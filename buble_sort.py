



def bubble_sort(seq):
    seq_len = len(seq)
    for i in range(seq_len):
        print(seq_len)
        for j in range(seq_len-1, i, -1): # for j in range(i, seq_len-1)[::-1]:

            if(seq[j] < seq[j-1]):
                temp = seq[j]
                seq[j] = seq[j-1]
                seq[j-1] = temp

seq = [22,1,33,4,7,6,8,9,11]
bubble_sort(seq)

print(seq)