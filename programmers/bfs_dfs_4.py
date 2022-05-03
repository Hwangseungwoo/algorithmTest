from collections import defaultdict
def solution(tickets):
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint

        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            fp = footprint[:] # deepcopy
            fp.append(country)

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통과한 경우

            routes[key].insert(idx, country) # 통과 못했으면 티켓 반환

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer