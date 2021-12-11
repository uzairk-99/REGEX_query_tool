import re
def regex_query(string,pattern):
    result={}
    
    search_result=re.search(pattern,string)
    try:
        result['search_result']={'span':search_result.span(),'match':search_result.group()}
    except:
        result['search_result']={'span':None,'match':None}
        
    match_result=re.match(pattern,string)
    try:
        result['match_result']={'span':match_result.span(),'match':match_result.group()}
    except:
        result['match_result']={'span':None,'match':None}
        
    findall_result=re.findall(pattern,string)
    try:
        result['findall_result']=findall_result
    except:
        result['findall_result']={'span':None,'match':None}
    return result

def query_result(string,pattern):
    q_res=regex_query(string,pattern)
    print(' Search result : ','Span =',q_res['search_result']['span'],', Match =',q_res['search_result']['match'],'\n','Match result : ','Span =',q_res['match_result']['span'],', Match =',q_res['match_result']['match'],'\n','Findall result : ',q_res['findall_result'])

n=0
while n != 2:
    print(' 1. Start \n 2. Exit')
    n=int(input('Enter your choice : '))

    if n == 1:
        string=input('Enter the string : ')
        pattern=input('Enter the pattern : ')
        
        query_result(string,pattern)
