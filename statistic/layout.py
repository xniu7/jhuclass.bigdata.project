#!/usr/bin/env python
import sys

def getLinkNoRep(links):
    new_links = []
    in_node = set()
    out_node = set()
    while(links):
        link=links.pop(0)
        if link[0][0] in in_node or link[1][0] in out_node: continue
        
        in_node.add(link[0][0])
        out_node.add(link[1][0])
        new_links.append(link)
    return new_links

def getLinkInOrder(links):
    new_links=[]
    dic = {}
    in_node=set()
    out_node=set()
    for pos in xrange(len(links)):
        link = links[pos]
        out_node.add(link[1][0])
        dic[link[0][0]]=pos
    for link in links:
        if link[0][0] in out_node:continue
        in_node.add(link[0][0])
    while(len(in_node)>0):
        start = in_node.pop()
        temp=[]
        while(start in dic):
            pos = dic[start]
            link = links[pos]
            temp.append(link)
            start = link[1][0]
        if len(temp)==0 : continue
        
        com_num=0
        for link in temp: com_num+=link[2]
        temp.append(com_num)
        
        new_links.append(temp)
        
    #new_links.sort(key=lambda p: len(p),reverse=True)
    
    new_links.sort(key=lambda p: p[len(p)-1],reverse=True)
    #print new_links
    for link in new_links: link.pop(len(link)-1)
    
    return new_links
    

def getLayout(links):
    links = getLinkNoRep(links)    
    links = getLinkInOrder(links)
    return links
