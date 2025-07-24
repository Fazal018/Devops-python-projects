def my_tools(tool):
   installed_tools=["Docker","Ansible","Terraform","Jenkins"]
   if tool in installed_tools:
       return f"{tool} is installed !"
   else :
    return f"{tool} is not_installed !"

#Exceptional_handling

try :
    with open("tools.txt","r") as file , open ("health_report.txt","w") as report :
        for line in file :
            tool=line.strip()
            status=my_tools(tool)
            print(status)
            report.write(status + "\n")
            
except FileNotFoundError as e:
    print("File not Found : ", e)
    
except Exception as e :
    print("Error found :", type(e).__name__,"-",e)
finally:   
    print("Finally , Task Completed 'Congratulations'")




