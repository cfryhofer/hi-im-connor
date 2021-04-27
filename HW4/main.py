#Connor Fryhofer 1853826

num_calls = 0


def partition(user_ids, i, k):

    ind = (i-1)         # index of smaller element

    pivot = user_ids[k]     # pivot

    for j in range(i, k):

        if user_ids[j] <= pivot:

            ind = ind+1

            user_ids[ind], user_ids[j] = user_ids[j], user_ids[ind]

    user_ids[ind+1], user_ids[k] = user_ids[k], user_ids[ind+1]

    return (ind+1)


def quicksort(user_ids, i, k):

    global num_calls

    num_calls = num_calls + 1

    if len(user_ids) == 1:

        return user_ids

    if i < k:

        pi = partition(user_ids, i, k)

        quicksort(user_ids, i, pi-1)

        quicksort(user_ids, pi+1, k)



if __name__ == "__main__":

    user_ids = []

    user_id = input()

    while user_id != "-1":

        user_ids.append(user_id)

        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:

        print(user_id)