from langchain_community.agent_toolkits.load_tools import get_all_tool_names

print('=== load_tools ===')
names = sorted(get_all_tool_names())

for name in names:
    print(f' - {name}')
print(f'\n {len(names)} toolkits are available now')