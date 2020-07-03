def solution(l):
    l.sort(key=lambda s: map(int, s.split('.')))
    print(l)


solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
