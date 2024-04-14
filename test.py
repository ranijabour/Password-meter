import math
import PESrank
import testpass

# feedback1 - strength
# feedback2 - reuse
# feedback3 - word/prefix
# 4 - mutual string
# feedback5 - dates

def main(password, username):
    [rank,explain] = PESrank.main(username, password, "/Users/gonycohen/Downloads/PESrank-master-3/PESrank/")
    n=905*(10**6)
    ex=0
    indicators = [1,1,0,0,0,0]
    info_list=[1]
    feedback1 = "Your password is "
    feedback2 = ""
    feedback3 = ""
    feedback4 = ""
    feedback5 = ""
    if rank<0:
        rank = 70
        feedback1 = feedback1 + "strong. "
        feedback2 = "Although your password is strong, don't reuse it on any accounts you care about. Password reuse is very insecure!."
        indicators[2] = 1
        info_list.append(2)
    else:
        rank = math.log2(rank)
        if rank<=30:
            feedback1 = feedback1 + "weak. "
            ex=1
        elif (rank)<=50:
            feedback1 = feedback1 + "sub-optimal. "
            ex=1
        else:
            feedback1 = feedback1 + "strong. "
            feedback2 = "Although your password is strong, don't reuse it on any accounts you care about. Password reuse is very insecure!."
            indicators[2] = 1
            info_list.append(2)
    if ex==1:
        indicators[3] = 1
        info_list.append(3)
        feedback3 = "Your password is based on the leaked word: '"+str(explain[0][1])+ "' that was used by " \
                    +str(int(float(explain[0][2])*n))+ " people. "
        for lst in explain[1:]:
            if math.ceil(float(lst[1])*n)>=100:
                if lst[0]==1:
                    feedback3 = feedback3 + "It uses a prefix that was used by "\
                                +str(math.ceil(float(lst[1])*n))+ " people. "
                if lst[0]==3:
                    feedback3 = feedback3 + "It uses a suffix that was used by "\
                                +str(math.ceil(float(lst[1])*n))+ " people. "
                if lst[0]==4:
                    feedback3 = feedback3 + "It uses a capitaliation pattern that was used by "\
                                +str(math.ceil(float(lst[1])*n))+ "people. "
                if lst[0]==5:
                    feedback3 = feedback3+"It uses a l33t pattern that was used by "\
                                +str(math.ceil(float(lst[1])*n))+ " people. "

    indicator, s4 = testpass.contains_mutual_substring(password, username)
    if (indicator):
        info_list.append(4)
        indicators[4] = 1
        feedback4 = feedback4+"The sequence: '" + s4 + "' appears in both your user name and password. " \
                                     "It's not recommended to use your account information in your password."
    result = testpass.find_date(password)
    if result:
        info_list.append(5)
        indicators[5] = 1
        feedback5 = feedback5+"Your password contains the date pattern: '"+result+"'"

    return rank, feedback1, feedback2, feedback3, feedback4, feedback5, indicators, info_list
