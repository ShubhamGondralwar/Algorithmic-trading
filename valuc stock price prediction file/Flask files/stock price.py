
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import logging
import json
import requests
from bs4 import BeautifulSoup
from itertools import groupby 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import logging
import json
from pandas.io.json import json_normalize
import pandas as pd
import requests
#============================================================================================##
#---------------------------------------------initialize logging-------------------------------------#
#
LOG_FILE_NAME = 'Stock price predicting App.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=LOG_FILE_NAME,
                    filemode='w')

#----------------------------------from flask import render_template---------------------------------#
##=================================================================================##
app = Flask(__name__, static_url_path='/static')

##============================================================================##
##Loading pickle files for all models:
sbi_picklemodel = pickle.load(open('sbi.pickle','rb'))
model_muttu = pickle.load(open('muttu.pickle','rb'))
model = pickle.load(open('model.pickle','rb'))
infofysis_pickle = pickle.load(open('info.pickle','rb'))
pnb_picklemodel = pickle.load(open('pnb.pickle','rb'))

##==============================all pickle files loaded=====================##
s = [717.6, 25057.22, 23091.03, 10046.65, 9953.75, 27272.3]
infofysis_pickle = pickle.load(open('info.pickle','rb'))
print(s)
p = infofysis_pickle.predict([s])
print(p)
##=====================mainhtmlpagerouting===================================
@app.route('/')
def hvh():
     return render_template("stock_predict.html")


##===========================================================================  
#scrapping in json.
@app.route('/prediction/<name>',methods=['POST', 'GET'])
def e(name):
    if name=="escortsltd":
        a = request.get_json()[0]
        print(a)
        val = []
        for key in a:
            print(a[key])
            val.append(a[key])
            
        model = pickle.load(open('model.pickle', 'rb'))
        print(val)
        p = model.predict([val])
        print(p)
        return jsonify({"predict": p[0]})
    elif name=="sbi":
        g = request.get_json()[0]
        print(g)
        val = []
        for key in g:
            print(g[key])
            val.append(g[key])
            
        sbi_picklemodel = pickle.load(open('sbi.pickle','rb'))
        print(val)
        p = sbi_picklemodel.predict([val])
        print(p)
        return jsonify({"predict": p[0]})
    elif name=="muthoot":
        f= request.get_json()[0]
        print(f)
        val = []
        for key in f:
            print(f[key])
            val.append(f[key])
            
        model_muttu = pickle.load(open('muttu.pickle','rb'))
        print(val)
        p = model_muttu.predict([val])
        print(p)
        return jsonify({"predict": p[0]})
    elif name=="infosys":
        k= request.get_json()[0]
        print(k)
        val = []
        for key in k:
            print(k[key])
            val.append(k[key])
            
        infofysis_pickle = pickle.load(open('info.pickle','rb'))
        print(val)
        p = infofysis_pickle.predict([val])
        print(p)
        return jsonify({"predict": p[0]})
    elif name=="pnb":
        m= request.get_json()[0]
        print(m)
        val = []
        for key in m:
            print(m[key])
            val.append(m[key])
            
        pnb_picklemodel = pickle.load(open('pnb.pickle','rb'))
        print(val)
        p = pnb_picklemodel.predict([val])
        print(p)
        return jsonify({"predict": p[0]})
          
#=================================================================================##       
        
  
@app.route('/automated/<name>')
def pre(name):
#========================================================================##
        url_NIFTY='https://in.finance.yahoo.com/quote/%5ENSEI?p=^NSEI'
        response1 = requests.get(url_NIFTY)
        soup = BeautifulSoup(response1.text,'html.parser')
        nifty_data = soup.find(id="quote-summary").getText()
        nifty_data = nifty_data.replace(',','')
        nifty_data = nifty_data.split(" ")
        
        res = [''.join(j).strip() for sub in nifty_data for k, j in groupby(sub, str.isdigit)] 
        
        NiftyClose = res[2]+res[3]+res[4]
        NiftyClose =float(NiftyClose)
#==========================================================================#   
        #autrilia
        aust = "^AXJO"
        aust = "https://in.finance.yahoo.com/quote/%5EAXJO?"+aust
        print(aust)
        
        response_3 = requests.get(aust)
        soup = BeautifulSoup(response_3.text,'html.parser')
        aust = soup.find(id="quote-summary").getText()
        aust = aust.replace(',','')
        aust =aust.split(" ")
        #type(aust)
        #print(aust)
        result = [''.join(j).strip() for sub in aust for k, j in groupby(sub, str.isdigit)] 
        print(result)
        
        austclose = result[2]+result[3]+result[4]
        austclose = float(austclose)
#==========================================================================##
         #US
        us = "^IXIC"
        us = "https://in.finance.yahoo.com/quote/%5EIXIC?"+us
        print(us)
        
        response_5 = requests.get(us)
        soup = BeautifulSoup(response_5.text,'html.parser')
        us = soup.find(id="quote-summary").getText()
        us = us.replace(',','')
        us =us.split(" ")
        print(us)
        result = [''.join(j).strip() for sub in us for k, j in groupby(sub, str.isdigit)] 
        print(result)
        
        usclose = result[2]+result[3]+result[4]
        usclose = float(usclose)
        
#==========================================================================#
        #nikkie
        nike= "^N225"
        nike = "https://in.finance.yahoo.com/quote/%5EN225?"+nike
        print(nike)
        
        response_7 = requests.get(nike)
        soup = BeautifulSoup(response_7.text,'html.parser')
        nike = soup.find(id="quote-summary").getText()
        nike = nike.replace(',','')
        nike =nike.split(" ")
        print(nike)
        result = [''.join(j).strip() for sub in nike for k, j in groupby(sub, str.isdigit)] 
        print(result)
        
        nikeclose = result[2]+result[3]+result[4]
        nikeclose = float(nikeclose)
#=========================================================================##
        #hangsanng
        hs= "^HSI"
        hs = "https://in.finance.yahoo.com/quote/%5EHSI?"+hs
        print(hs)
        
        response_6 = requests.get(hs)
        soup = BeautifulSoup(response_6.text,'html.parser')
        hs = soup.find(id="quote-summary").getText()
        hs = hs.replace(',','')
        hs =hs.split(" ")
        print(hs)
        result = [''.join(j).strip() for sub in hs for k, j in groupby(sub, str.isdigit)] 
        print(result)
        
        hsclose = result[2]+result[3]+result[4]
        hsclose = float(hsclose)
#=========================================================================##
##==========================ESCORTS LTD========================================##
        if name == "escortsltd":
            #escorts
            escorts = "ESCORTS.NS"
            escorts_url = "https://finance.yahoo.com/quote/ESCORTS.NS?"+escorts
            print(escorts_url)
            
            response_2 = requests.get(escorts_url)
            soup = BeautifulSoup(response_2.text,'html.parser')
            escort = soup.find(id="quote-summary").getText()
            escort = escort.replace(',','')
            escort =escort.split(" ")
            type(escort)
            print(escort)
        
            result = [''.join(j).strip() for sub in escort for k, j in groupby(sub, str.isdigit)] 
            
            escortclose = result[2]+result[3]+result[4]
            escortclose = float(escortclose)
            
            livevalue = [{'escortclose':escortclose,'NiftyClose':NiftyClose,"nikeclose":nikeclose,"usclose":usclose,"hsclose":hsclose,"austclose":austclose}]
            livevalue = json.dumps(livevalue)
            print(livevalue)
            print(type(livevalue))
            
            
                
            livevalues = [escortclose,NiftyClose,nikeclose,usclose,hsclose,austclose]
            livevalues = [float(i) for i in livevalues] 
        
            return render_template("escort.html",livevalues=livevalues,ls =livevalue )
##=====================================================================================##
##=======================escortsdone=============================================##
        elif name=="sbi":
            #SBI
            sbi = "SBIN.NS"
            url_sbi = 'https://in.finance.yahoo.com/quote/SBIN.NS?'+sbi
            response10 = requests.get(url_sbi)
            soup = BeautifulSoup(response10.text,'html.parser')
            sbi_data = soup.find(id="quote-summary").getText()
            sbi_data = sbi_data.replace(',','')
            sbi_data = sbi_data.split(" ")
            
            type(sbi_data)
            print(sbi_data)
            result = [''.join(j).strip() for sub in sbi_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            sbi_data_close = result[2]+result[3]+result[4]
            sbi_data_close = float(sbi_data_close)
            
            livesbi = [{"sbi_data_close":sbi_data_close,"austclose":austclose,"hsclose":hsclose,"nikeclose":nikeclose,"NiftyClose":NiftyClose,"usclose":usclose}]
            livesbi = json.dumps(livesbi)
            print(livesbi)
            print(type(livesbi))
            
            
                
            livevaluessbi = [sbi_data_close,austclose,hsclose,nikeclose,NiftyClose,usclose,]
            livevaluessbi = [float(i) for i in livevaluessbi] 
        
            return render_template("sbi.html",livevaluessbi=livevaluessbi,ls =livesbi )
                
##====================================================================================##            
        elif name=="muthoot":
            #DJI
            DJ = "^DJI"
            url_dj = 'https://in.finance.yahoo.com/quote/^DJI?'+DJ
            response8 = requests.get(url_dj)
            soup = BeautifulSoup(response8.text,'html.parser')
            Dj_data = soup.find(id="quote-summary").getText()
            Dj_data = Dj_data.replace(',','')
            Dj_data = Dj_data.split(" ")
        
            type(Dj_data)
            print(Dj_data)
            result = [''.join(j).strip() for sub in Dj_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            Dj_data_close = result[2]+result[3]+result[4]
            Dj_data_close = float(Dj_data_close)
            
            #sp500
            sp = "^GSPC"
            url_sp= 'https://in.finance.yahoo.com/quote/^GSPC?'+sp
            response9 = requests.get(url_sp)
            soup = BeautifulSoup(response9.text,'html.parser')
            sp_data = soup.find(id="quote-summary").getText()
            sp_data = sp_data.replace(',','')
            sp_data = sp_data.split(" ")
            
            type(sp_data)
            print(sp_data)
            result = [''.join(j).strip() for sub in sp_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            sp_data_close = result[2]+result[3]+result[4]
            sp_data_close = float(sp_data_close)
            
            #muthoot finance
            mutto = "MUTHOOTFIN.NS"
            url_muthoot = 'https://in.finance.yahoo.com/quote/MUTHOOTFIN.NS?'+mutto
            response12 = requests.get(url_muthoot)
            soup = BeautifulSoup(response12.text,'html.parser')
            muthoot_data = soup.find(id="quote-summary").getText()
            muthoot_data = muthoot_data.replace(',','')
            muthoot_data = muthoot_data.split(" ")
            
            type(muthoot_data)
            print(muthoot_data)
            result = [''.join(j).strip() for sub in muthoot_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            muthoot_data_close = result[2]+result[3]+result[4]
            muthoot_data_close = float(muthoot_data_close)
            
            livemutt = [{"austclose":austclose,"hsclose":hsclose,"nikeclose":nikeclose,"NiftyClose":NiftyClose,"usclose":usclose," muthoot_data_close": muthoot_data_close,"Dj_data_close":Dj_data_close,"sp_data_close":sp_data_close}]
            livemutt = json.dumps(livemutt)
            print(livemutt)
            print(type(livemutt))
            
            
                
            livevaluesmutt = [austclose,hsclose,nikeclose,NiftyClose,usclose,muthoot_data_close,Dj_data_close,sp_data_close]
            livevaluesmutt = [float(i) for i in livevaluesmutt] 
        
            return render_template("muthoot.html",livevaluesmutt=livevaluesmutt,ls =livemutt )
                
##===========================================================================#####
    
        elif name=="infosys":
            #Infosys
            infosys = "INFY.NS"
            url_infosys= 'https://in.finance.yahoo.com/quote/INFY.NS?'+infosys
            response11 = requests.get(url_infosys)
            soup = BeautifulSoup(response11.text,'html.parser')
            infosys_data = soup.find(id="quote-summary").getText()
            infosys_data = infosys_data.replace(',','')
            infosys_data = infosys_data.split(" ")
            
            type(infosys_data)
            print(infosys_data)
            result = [''.join(j).strip() for sub in infosys_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            infosys_data_close = result[2]+result[3]+result[4]
            infosys_data_close = float(infosys_data_close)
            
            #DJI
            DJ = "^DJI"
            url_dj = 'https://in.finance.yahoo.com/quote/^DJI?'+DJ
            response8 = requests.get(url_dj)
            soup = BeautifulSoup(response8.text,'html.parser')
            Dj_data = soup.find(id="quote-summary").getText()
            Dj_data = Dj_data.replace(',','')
            Dj_data = Dj_data.split(" ")
        
            type(Dj_data)
            print(Dj_data)
            result = [''.join(j).strip() for sub in Dj_data for k, j in groupby(sub, str.isdigit)] 
            print(result)
            Dj_data_close = result[2]+result[3]+result[4]
            Dj_data_close = float(Dj_data_close )
            
            liveinfo = [{"infosys_data_close":infosys_data_close,"hsclose":hsclose,"nikeclose":nikeclose,"NiftyClose":NiftyClose,"usclose":usclose,"Dj_data_close":Dj_data_close}]
            liveinfo = json.dumps(liveinfo)
            print(liveinfo)
            print(type(liveinfo))
            
            
                
            livevaluesinfo = [infosys_data_close,hsclose,nikeclose,NiftyClose,usclose,Dj_data_close]
            livevaluesinfo = [float(i) for i in livevaluesinfo] 
        
            return render_template("infosys.html",livevaluesinfo=livevaluesinfo,ls =liveinfo )
            
 ###================================================================================###         
        elif name=="pnb":
                pnb = "PNB.NS"
                url_pnb = 'https://in.finance.yahoo.com/quote/PNB.NS?'+pnb
                response14 = requests.get(url_pnb)
                soup = BeautifulSoup(response14.text,'html.parser')
                pnb_data = soup.find(id="quote-summary").getText()
                pnb_data = pnb_data.replace(',','')
                pnb_data = pnb_data.split(" ")
                
                type(pnb_data)
                print(pnb_data)
                result = [''.join(j).strip() for sub in pnb_data for k, j in groupby(sub, str.isdigit)] 
                print(result)
                pnb_data_close = result[2]+result[3]+result[4]
                pnb_data_close = float(pnb_data_close)
                
                #sangai open
                san = "000001.SS"
                url_san = 'https://finance.yahoo.com/quote/000001.SS?'+san
                response15 = requests.get(url_san)
                soup = BeautifulSoup(response15.text,'html.parser')
                san_data = soup.find(id="quote-summary").getText()
                san_data =san_data.replace(',','')
                san_data = san_data.split(" ")
                
                type(san_data)
                print(san_data)
                result = [''.join(j).strip() for sub in san_data for k, j in groupby(sub, str.isdigit)] 
                print(result)
                
                san_data_open = result[6]+result[7]+result[8]
                san_data_open = float(san_data_open)
                
                livepnb = [{"pnb_data_close":pnb_data_close,"san_data_open":san_data_open}]
                livepnb = json.dumps(livepnb)
                print(livepnb)
                print(type(livepnb))
                
                
                    
                livevaluespnb = [pnb_data_close,san_data_open]
                livevaluespnb = [float(i) for i in livevaluespnb] 
            
                return render_template("pnb.html",livevaluespnb=livevaluespnb,ls =livepnb )  
        
            
                
if __name__ == '__main__':
    app.run()