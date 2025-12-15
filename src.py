
#Add example usage scenarios for testing deadlock detection
def build_wait_for_graph(P, R, allocation, request):
    graph = {i: [] for i in range(P)}
    for i in range(P):
        for j in range(R):
            if request[i][j] == 1:
                for k in range(P):
                    if allocation[k][j] == 1:
                        graph[i].append(k)
    return graph

def dfs(node, graph, visited, rec_stack, cycle):
    visited[node] = True
    rec_stack[node] = True
    cycle.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, rec_stack, cycle):
                return True
        elif rec_stack[neighbor]:
            cycle.append(neighbor)
            return True
    rec_stack[node] = False
    cycle.pop()
    return False

def detect_deadlock(graph, P):
    visited = [False] * P
    rec_stack = [False] * P
    cycle = []
    for process in range(P):
        if not visited[process]:
            if dfs(process, graph, visited, rec_stack, cycle):
                return True, cycle
    return False, []

def main():
    print("=== Automated Deadlock Detection Tool (Python) ===")
    P = int(input("Enter number of processes: "))
    R = int(input("Enter number of resources: "))
    print(f"Enter Allocation Matrix ({P} x {R}):")
    allocation = []
    for i in range(P):
        row = list(map(int, input().split()))
        allocation.append(row)
    print(f"Enter Request Matrix ({P} x {R}):")
    request = []
    for i in range(P):
        row = list(map(int, input().split()))
        request.append(row)
    graph = build_wait_for_graph(P, R, allocation, request)
    deadlock_found, cycle = detect_deadlock(graph, P)
    print("\n=== Deadlock Detection Result ===")
    if deadlock_found:
        print("⚠ Deadlock detected involving processes:")
        printed = set()
        for p in cycle:
            if p not in printed:
                print(f"P{p}", end=" ")
                printed.add(p)
        print("\n\nSuggestion: Break the cycle by terminating or releasing resources.")
    else:
        print("✔ No deadlock detected.")

if __name__ == "__main__":
    main()
