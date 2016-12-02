

def selection_sort(seq):
    seq_len = len(seq)
    for i in range(seq_len):
        position = i
        for j in range(i+1, seq_len):
            if(seq[j] > seq[i]):
                position = j

        if(position != i):
            seq[position], seq[i] = seq[i], seq[position]            #swap


array = [88,44,33,4,7,6,8,9,11]
selection_sort(array)
print(array)
