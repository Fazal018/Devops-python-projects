import sys

def suggest_tool(tool_name):
    tool_info= {
        "git": "Version Control System",
        "docker": "Containerization Tool",
        "jenkins": "CI/CD Pipeline Automation",
        "kubernetes": "Container Orchestration",
        "ansible": "Configuration Management",
        "terraform": "Infrastructure as Code"
    }
    
    tool_name=tool_name.lower()
    
    if tool_name in tool_info:
        return f"Tool : {tool_name.title()} -> {tool_info[tool_name]}"
    else :
        return f"Tool : {tool_name.title()} -> Unknown tool , Keep exploring devops ! "
    
if len(sys.argv)< 2 :
    print("please provide a tool name as an argument.\nExample: python tool_suggestor.py Docker")
else : 
    tool_arg = sys.argv[1]
    print(suggest_tool(tool_arg))
        
