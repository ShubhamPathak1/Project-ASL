Data Folder contains all the numpy files for each signs (Hello, Help, Thank you, me, yes, want). Till now, only these signs are detected.
Logs has the trained model in it.
The model is further saved into action.h5 and action1.h5.
action.h5 model can detect hello, hep, me, thankyou
action1.h5 mdoel can detect yes and want.
_makefolders.py makes the directory Data and sub directory Hello, Help, Me.... and inside each of them, folders from 0 to 29 to have numpy files inside them.
datacollect.py is used to collect frames for each folders in Data. Currently, datacollect.py was used to collect data for Want and Yes.
traimodel.py can be run to train the model further more. It is for Hello, Help, Thankyou, me.
trainmodel.py saved the model into action.h5.
trainnewmodel.py is for Want and Yes.
trainnewmodel.py saved the model into action1.h5.
test.py currently tests only for action.h5 model. (i.e. hello, help, thankyou and mee)
test1.py is incomplete as i have tried to test both the model at once, but i haven't successfully done it.
testagain.py is similar to test.py till now, i have been working on calculating probabiites of each sign detected.

So, you can clone this and directly run TEST.PY file to see the results. 
