my_dict={"ali" : (90,100,95,),
         "taha": (95,100,98),
         "kamran" : (90,95,99)}
result=my_dict
print(result["taha"])
avg_score=sum(result["taha"]) / 3, sum(result["ali"])/3 ,sum(result["kamran"])/3
print(avg_score)
print(max(avg_score))
