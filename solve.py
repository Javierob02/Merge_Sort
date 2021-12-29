def solve(items):
    """
    Merge sort is a divide and conquer algorithm, that recursively breaks down the problem into tow or more sub-problems
    until they become simple enough to be solved directly. This solutions are then combined to form the final solution.
    """
    if len(items) > 1:
        centre = len(items) // 2  #Dividir lista en 2 listas
        left = items[:centre]
        right = items[centre:]

        solve(left)  #Ordenar listas
        solve(right)

        #Unir ambas lista
        i = 0   #Índice de 'left'
        j = 0   #Índice de 'right'
        k = 0   #Índice de 'items'

        while i < len(left) and j < len(right):
            if left[i] < right[j]:      #Si left[i] más pequeño, introduce en 'items'
                items[k] = left[i]
                i += 1
            else:                       #Si right[i] más pequeño o igual, introduce en 'items'
                items[k] = right[j]
                j += 1
            k += 1

        while i < len(left):    #Terminar de vaciar 'left'
            items[k] = left[i]
            i += 1
            k += 1

        while j < len(right):   #Terminar de vaciar 'right'
            items[k] = right[j]
            j += 1
            k += 1

    return