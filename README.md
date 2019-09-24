# My training project
# Simulation-modeling
# Three-channel system with failures


Programs arrive randomly distributed according to a linear law:
Tzmin = 1/2 sec, Tzmax = 5/6 sec.
The processing time of one program by the server is a random variable,
distributed linearly: Tsmin = 1 sec, Tsmax = 5 sec

Programs arrive randomly distributed over
exponential law with a frequency of λ = 1.5 1 / s, and the average processing time
the program of each server is tobr = 2 sec

The simulation lasts 1 hour

Computing System Features:

P0 — the probability that there is not a single order in the system, all channels are free;

P1 - the probability that the system has one request, it is served by one channel;

P2 — the probability that the system has two requests, they are served by two channels;

P3 - the probability that there are three requests in the system, they are served by three channels;

Pfailure - probability of failure (the system will not be able to process the request)

Q - relative throughput of the Computing System - average share
programs processed by the Computing System::

kcp - the average waiting time (stay in line) of one application
