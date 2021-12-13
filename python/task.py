import sys
help='''
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
'''
def read():
    task.seek(0)
    l=task.readlines()
    l.sort(key=lambda x:x[0])
    return l

task = open("task.txt","a+")
completed = open("completed.txt","a+")

if len(sys.argv)==1 or sys.argv[1]=='help':
    sys.stdout.buffer.write(help.encode('utf8'))

elif sys.argv[1]=='add':
    if len(sys.argv)>2:
        msg='Added task: "{}" with priority {}'.format(' '.join(sys.argv[3:]),sys.argv[2])
        task.write(' '.join(sys.argv[2:]))
        task.write('\n')
        sys.stdout.buffer.write(msg.encode('utf8'))
    else:
        msg='Error: Missing tasks string. Nothing added!'
        sys.stdout.buffer.write(msg.encode('utf8'))

elif sys.argv[1]=='ls':
    t=read()
    if len(t)>0:
        for i in range(len(t)):
            msg='{}. {} [{}]\n'.format(i+1,t[i][2:-1],t[i][0])
            sys.stdout.buffer.write(msg.encode('utf8'))
    else:
        msg = 'There are no pending tasks!'
        sys.stdout.buffer.write(msg.encode('utf8'))

elif sys.argv[1]=='del':
    if len(sys.argv)>2:
        index=sys.argv[2]
        t=read()
        if int(index)>len(t) or int(index)<1:
            msg='Error: task with index #{} does not exist. Nothing deleted.'.format(index)
            sys.stdout.buffer.write(msg.encode('utf8'))
        else:
            with open("tasks.txt", "w") as f:
                for i in range(len(t)):
                    if i+1 != int(index):
                        f.write(t[i])
            msg='Deleted task #{}'.format(index)
            sys.stdout.buffer.write(msg.encode('utf8'))
    else:
        msg = 'Error: Missing NUMBER for deleting tasks.' 
        sys.stdout.buffer.write(msg.encode('utf8'))

elif sys.argv[1]=='done':
    if len(sys.argv)>2:
        index=sys.argv[2]
        t=read()
        if int(index)>len(t) or int(index)<1:
            msg='Error: no incomplete item with index #{} exists.'.format(index)
            sys.stdout.buffer.write(msg.encode('utf8'))
        else:
            d=t.pop(int(index)-1)
            with open("tasks.txt", "w") as f:
                for i in t:
                        f.write(i)
            completed.write(d)
            msg='Marked item as done.'
            sys.stdout.buffer.write(msg.encode('utf8'))
    else:
        msg = 'Error: Missing NUMBER for marking tasks as done.'
        sys.stdout.buffer.write(msg.encode('utf8'))


task.close()
completed.close()