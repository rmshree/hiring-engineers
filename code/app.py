{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red200\green20\blue201;\red255\green255\blue255;\red0\green0\blue0;
\red64\green11\blue217;\red180\green36\blue25;\red46\green174\blue187;\red193\green101\blue28;}
{\*\expandedcolortbl;;\cssrgb\c83396\c23075\c82664;\csgray\c100000;\csgray\c0;
\cssrgb\c32308\c18668\c88227;\cssrgb\c76409\c21698\c12524;\cssrgb\c20196\c73240\c78250;\cssrgb\c80553\c47366\c13835;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \cb3 \CocoaLigature0 from\cf4  flask \cf2 import\cf4  Flask\
\cf2 import\cf4  logging\
\cf2 import\cf4  sys\
\
\cf5 # Have flask use stdout as the logger\cf4 \
main_logger = logging.getLogger()\
main_logger.setLevel(logging.DEBUG)\
c = logging.StreamHandler(sys.stdout)\
formatter = logging.Formatter(\cf6 '%(asctime)s - %(name)s - %(levelname)s - %(message)s'\cf4 )\
c.setFormatter(formatter)\
main_logger.addHandler(c)\
\
app = Flask(__name__)\
\
\cf2 @\cf7 app.route\cf4 (\cf6 '/'\cf4 )\
\cf8 def\cf4  \cf7 api_entry\cf4 ():\
    \cf8 return\cf4  \cf6 'Entrypoint to the Application'\cf4 \
\
\cf2 @\cf7 app.route\cf4 (\cf6 '/api/apm'\cf4 )\
\cf8 def\cf4  \cf7 apm_endpoint\cf4 ():\
    \cf8 return\cf4  \cf6 'Getting APM Started'\cf4 \
\
\cf2 @\cf7 app.route\cf4 (\cf6 '/api/trace'\cf4 )\
\cf8 def\cf4  \cf7 trace_endpoint\cf4 ():\
    \cf8 return\cf4  \cf6 'Posting Traces'\cf4 \
\
\cf8 if\cf4  __name__ == \cf6 '__main__'\cf4 :\
    app.run(host=\cf6 '0.0.0.0'\cf4 , port=\cf6 '5050'\cf4 )}