{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red200\green20\blue201;\red255\green255\blue255;\red0\green0\blue0;
\red64\green11\blue217;\red193\green101\blue28;\red47\green180\blue29;\red180\green36\blue25;\red46\green174\blue187;
}
{\*\expandedcolortbl;;\cssrgb\c83396\c23075\c82664;\csgray\c100000;\csgray\c0;
\cssrgb\c32308\c18668\c88227;\cssrgb\c80553\c47366\c13835;\cssrgb\c20238\c73898\c14947;\cssrgb\c76409\c21698\c12524;\cssrgb\c20196\c73240\c78250;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \cb3 \CocoaLigature0 import\cf4  random\
\
\cf5 # the following try/except block will make the custom check compatible with any Agent version\cf4 \
\cf6 try\cf4 :\
    \cf5 # first, try to import the base class from old versions of the Agent...\cf4 \
    \cf2 from\cf4  checks \cf2 import\cf4  AgentCheck\
\cf6 except\cf4  \cf7 ImportError\cf4 :\
    \cf5 # ...if the above failed, the check is running in Agent version 6 or later\cf4 \
    \cf2 from\cf4  datadog_checks.checks \cf2 import\cf4  AgentCheck\
\
\cf5 # content of the special variable __version__ will be shown in the Agent status page\cf4 \
__version__ = \cf8 "1.0.0"\cf4 \
\
\
\cf6 class\cf4  \cf9 MetricCheck\cf4 (AgentCheck):\
    \cf6 def\cf4  \cf9 check\cf4 (self, instance):\
        self.gauge(\cf8 'my_metric'\cf4 , random.randint(\cf8 0\cf4 , \cf8 1000\cf4 ))}