#!/usr/bin/python

import sys

actions = {}
Qvalues = {}
alpha = 0.2 
discount = 0.9

def read_input(file):
    for line in file:
        yield line.strip().split('\t')

def nextStateMaxQ(state):
    res = 0.0
    possible_actions = actions.get(state, [])
    if len(possible_actions) > 1:
        nextStateQ = map(lambda a: Qvalues.get((state, a), 0.0), possible_actions)
        res = max(nextStateQ)
    return res

def main(seperator='\t'):
    data = read_input(sys.stdin)
    for state, action, reward in data:
        # add action into action set  
        if actions.get(state, None) == None:
            actions[state] = set([action])
        else:
            actions[state].update([action])

        # a new record
        if state == action == reward == '0':
            last_state = last_action = None
        else:
            # if current state comes from a known state
            if last_state != None:
                # old value
                current_Qvalue = Qvalues.get((last_state, action), 0.0)
                # update
                Qvalues[(last_state, action)] = \
                     current_Qvalue + alpha * (float(reward) \
                                               + discount * nextStateMaxQ(state) \
                                               - current_Qvalue) 
            last_state = state
            last_action = action


    for (state, action), Qvalue in Qvalues.iteritems():
        print '{}\t{}\t{}'.format(state, action, Qvalue)


if __name__ == '__main__':
    main()
