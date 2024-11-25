def heapify(arr, n, i, update_callback):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        update_callback(arr, n, i, f"Intercambiando {arr[i]} con {arr[largest]}\n")
        heapify(arr, n, largest, update_callback)

def heap_sort(arr, ascending=True, update_callback=None):
    n = len(arr)

    # Construir el Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, update_callback)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        update_callback(arr, n, i, f"Moviendo {arr[i]} al final\n")
        heapify(arr, i, 0, update_callback)

    # Invertir para orden descendente si es necesario
    if not ascending:
        arr.reverse()