import matplotlib.pyplot as plt
from random import *
def score_finder(l_symp):
    """
    this is how i measure the health_index:
    fever: abs(your fever-37)*100 eg >>> 39.5==250
    tiredness: a number between 0 and 10 *10
    cough: a number between 0 and 10 *10
    difficulty in breathing: a number between 0 and 10 *10
    sneeze: a number between 0 and 5 *10
    then add all the above scores
    """
    #l_symp:[fever,tiredness,cough,difficulty in breathing,sneeze]
    score=0
    score+=abs(l_symp[0]-37)*100+l_symp[2]*10+l_symp[3]*10+l_symp[4]*10
    return score
#NOTE IT:its just an unrealistic example and has no use in real treatment
l_cases=[
    [[36,1,1,1,1],[37,2,2,2,2],[37,1,1,3,1],[37,0,0,0,0]],
    [[37,1,1,1,1],[37.5,2,2,2,2],[38,1,1,3,1],[37,0,0,0,0]],
    [[37.5,1,2,2,1],[38,2,2,2,2],[39,3,2,3,1],[38,2,2,2,0]],
    [[38,2,2,2,1],[39,3,2,3,2],[39.5,3,3,3,2],[38,3,3,2,0]],
    [[39,3,2,2,2],[40,3,2,3,2],[40,4,3,3,2],[39,3,2,2,1]],
    [[40,3,3,3,2],[41,4,3,3,2],[42,4,4,3,2],[41,4,4,3,3]],
    [[41,10,10,3,2],[41,10,10,10,2],[42,8,8,8,5],[41,8,9,4,3]],
]
#again i remind "l_cases" is unreal and we cant use it
def KNN(fever_,tiredness_,cough_,difficulty_in_breathing_,sneeze_):
    l_score=[fever_,tiredness_,cough_,difficulty_in_breathing_,sneeze_]
    health_index=score_finder(l_scores)
    l_best=[float("inf"),float("inf"),float("inf")]
    l_name=[0,0,0]
    for i in range(len(l_cases)):
        score=abs(health_index-score_finder(l_cases[i][0]))
        if score<l_best[0]:
            l_name[2]=l_name[1]
            l_name[1]=l_name[0]
            l_name[0]=i
            l_best[2]=l_best[1]
            l_best[1]=l_best[0]
            l_best[0]=score
        elif score<l_best[1]:
            l_name[2]=l_name[1]
            l_name[1]=i
            l_best[2]=l_best[1]
            l_best[1]=score
        elif score<l_best[2]:
            l_name[2]=i
            l_best[2]=score
    l_future=[[],[],[]]
    for i in range(3):
        for item in range(5):
            score_item=0
            for name in l_name:
                score_item+=l_cases[name][i+1][item]
            score_item=int(score_item/3*10)/10
            l_future[i].append(score_item)
    print("l_future:",l_future)
    l_future_scores=[[score_finder(l_future[0])],[score_finder(l_future[1])],[score_finder(l_future[2])]]
    plt.scatter(l_future_scores,[2,3,4])
    plt.show()
l=["fever","tiredness","cough","difficulty in breathing","sneeze"]
l_scores=[]
for i in l:
    inp=int(input(i+":"))
    l_scores.append(inp)
KNN(l_scores[0],l_scores[1],l_scores[2],l_scores[3],l_scores[4])
#def prescription(l_future):
#35   