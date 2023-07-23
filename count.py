def socks(arr):
    sock_counts = {}
    single_count = 0

    for sock_id in arr:
        sock_counts[sock_id] = sock_counts.get(sock_id, 0) + 1

    # single socks
    for count in sock_counts.values():
        if count % 2 == 1:
            single_count += 1

    return single_count

if __name__ == "__main__":
    arrNum = [80,90,80,70,60,50,60,70]
    result = socks(arrNum)
    print("Count of singular socks =", result)
