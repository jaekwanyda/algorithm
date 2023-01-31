# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def solution(bridge_length, weight, truck_weights):
    time=0;truck_q=[];time_q=[]
    while truck_weights:
        time+=1
        if truck_q and time_q and time-time_q[0]>=bridge_length:
            truck_q.pop(0);time_q.pop(0)
        if sum(truck_q)+truck_weights[0]<=weight:
            truck_q.append(truck_weights.pop(0));time_q.append(time)
            
    
    return time+bridge_length
