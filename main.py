import random
import time
import math
import copy

def trunc(num, digits):
    sp = str(num).split('.')
    return '.'.join([sp[0], sp[:digits]])

Tzmin = 1.0/2.0
Tzmax = 5.0/6.0
Tsmin = 1.0
Tsmax = 5.0

linear = lambda: (random.uniform(Tzmin,Tzmax), random.uniform(Tsmin,Tsmax)) # два равномерно распределенных числа
expon  = lambda: (random.expovariate(1.5), random.expovariate(0.5)) # два экспоненциально распределенных числа

def experiment(random_func, n=3):
    system_state = [{'name':'s'+str(x), 'task_finish':.0, 'task_count':0} for x in range(1,n+1)]
    current_time = 0
    total_tasks = 0
    events = []
    
    while current_time < 3600:
        diff_time,working_time = random_func()
        total_tasks += 1
        current_time += diff_time
        for unit in system_state:
            if unit['task_finish'] <= current_time:
                unit['task_finish'] = current_time + working_time
                unit['task_count'] += 1
                events.append((current_time, unit['name'],'start')) # событие начала задачи
                events.append((unit['task_finish'],unit['name'],'end')) # событие окончания задачи
                break
        # print(current_time, ':',diff_time,working_time,system_state)

    events = sorted(events, key = lambda x: x[0])
    prev = .0
    P = [.0  for x in range(n+1)]
    state = 0
    for e in events:
        curr = e[0]
        diff = curr - prev
        if state <= n:
            P[state] += diff
        else:
            print('Error state value')
        prev = curr
        etype = e[2]
        state += 1 if etype == 'start' else -1
    total_time = max(system_state, key=lambda x:x['task_finish'])
    total_time = total_time['task_finish']
    P = [x/total_time for x in P]

    λ = total_tasks/total_time
    μ = 1/λ
    Pотказа = P[-1]
    Q = 1 - Pотказа
    A = λ*Q
    kср = A/μ
    return {'all tasks':total_tasks, 'P':P, 'Pfailure':Pотказа, 'Q':Q, 'A':A, 'kср':kср}


from tkinter import *

def linear_event_handler():
    now = time.time()
    res = experiment(linear)
    text = ''
    text += 'all tasks : ' + str(res['all tasks']) + '\n'
    for idx,p in enumerate(res['P']):
        text += 'P'+ str(idx) +' = '+ str(p*100) +'%\n'
    text += 'Pfailure = ' + str(res['Pfailure']) + '\n'
    text += 'Q = ' + str(res['Q']) + '\n'
    text += 'kcp = ' + str(res['kср']) + '\n'
    linear_txt.set(text)

def expon_event_handler():
    res = experiment(expon)
    text = ''
    text += 'all tasks : ' + str(res['all tasks']) + '\n'
    for idx,p in enumerate(res['P']):
        text += 'P'+ str(idx) +' = '+ str(p*100) +'%\n'
    text += 'Pfailure = ' + str(res['Pfailure']) + '\n'
    text += 'Q = ' + str(res['Q']) + '\n'
    text += 'kcp = ' + str(res['kср']) + '\n'
    expon_txt.set(text)
 
# родительский элемент
root = Tk()

linear_txt = StringVar()
linear_txt.set("The simulation results \n will be displayed here")
expon_txt = StringVar()
expon_txt.set("The simulation results \n will be displayed here")
# устанавливаем название окна
root.title("three-channel system with failures")
 
# устанавливаем минимальный размер окна 
root.minsize(600, 250)
 
# выключаем возможность изменять окно
root.resizable(width=False, height=False)
 
# создаем рабочую область
frame = Frame(root)
frame.grid()
 
# вставляем текст
linear_label = Label(frame, textvariable=linear_txt).grid(row=1,column=1,pady=(30,0))
expon_label  = Label(frame, textvariable=expon_txt).grid(row=1,column=2, padx=(35,0),pady=(30,0))
# вставляем кнопку
but = Button(frame, text="Linear distribution", command=linear_event_handler).grid(row=2, column=1, padx=30)
but1 = Button(frame,text="Exponential distribution", command=expon_event_handler).grid(row=2, column=2,padx=(40,0))
