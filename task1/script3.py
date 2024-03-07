def analyze_access_log(filename):
    user_agents = {}
    with open(filename, 'r') as file:
        for line in file:
            user_agent = line.split('"')[5]
            user_agents[user_agent] = user_agents.get(user_agent, 0) + 1
    
    total_user_agents = len(user_agents)
    print("Total number of different User Agents:", total_user_agents)
    print("User Agent Statistics:")
    for agent, count in user_agents.items():
        print(f"{agent}: {count} requests")

if __name__ == "__main__":
    filename = input("Enter the access log file name: ")
    analyze_access_log(filename)

