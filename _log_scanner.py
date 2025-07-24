#Scans a log file line by line
#Detects lines with ERROR, WARNING, or CRITICAL
#Saves the findings to a summary report file
#Uses: functions, file handling, if, try/except

def log_file(error):
    if "ERROR" in error:
        return "Error Found"
    elif "WARNING" in error:
        return "Warning Found"
    elif "CRITICAL" in error:
        return "Critical Found"
    else:
        return "none"
    
try :
    with open("server.log","r") as file , open("findings.txt","w") as summary_report :
        for line in file :
            result=log_file(line.strip())
            if result :
                summary_report.write(result + "-" + line)
                print(result + "-" + line)
                
except FileNotFoundError as e :
    print( " File Not Found ", e )
except Exception as e :
    print("Error found",type(e).__name__)
finally :
    print("Log scan completed !")
    
                

