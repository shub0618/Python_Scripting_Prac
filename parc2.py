# dictorinary
devops={"skill":"Devops", "year":2024, "tech":{"cloud":"aws", "containers":"kb's", "cicd":"jenkins"}}
print(devops) 

#example
# I'm going to repeat once again. Skill is a key value. Here is a string.
# Here value is an in integer. Here value is a dictionary. So again, key value, key value. 
# And GitHub's key, its value is a list.
#devops={"skill":"Devops", "year":2024, "tech":{"cloud":"aws", "containers":"kb's", "cicd":"jenkins", "Gitops":["gitlab", "argocd", "tekton"]}}
#print(devops) 

# now lets simply that line
devops={
        "skill":"Devops", 
        "year":2024, 
        "tech":
            {
             "cloud":"aws", 
             "containers":"kb's", 
             "cicd":"jenkins", 
             "Gitops":
                     [
                      "gitlab", 
                      "argocd", 
                      "tekton"
                     ]
             }
        }   
print(devops)