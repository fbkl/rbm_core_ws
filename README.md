# rbm\_core

This repository will have only the core parts that need to work as fast as possible, so near the sensors. 

I am separating the launch files and the state machine used for acquisition and make that run remotely, because it uses quite a lot of processing power for things that do not need to be real time. 

It was a challenge in the past to get visualizations to work correctly when done remotely, but now it is necessary, so we are going with this smaller number of packages here.


## TODO:

- right now we need to find the model in the remote host, so in need the rqt acquisition here, which is probably dumb 


