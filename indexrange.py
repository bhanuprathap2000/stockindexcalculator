from flask import Flask,render_template,request
from sd_cal import indexrangecal
app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/calculate",methods=["POST","GET"])
def calculate():
    if request.method=="POST":
        indexname=request.form["indexname"]
        spotvalue=float(request.form["spotvalue"])
        daystoexpiry=int(request.form["daystoexpiry"])
        print(type(indexname),type(spotvalue),type(daystoexpiry))
        s1n,s1p,s2n,s2p=indexrangecal(indexname,spotvalue,daystoexpiry)
        
        return render_template("calculate.html",index_name=indexname,lowerbound1n=s1n,upperbound1p=s1p,lowerbound2n=s2n,upperbound2p=s2p)
    

if __name__=="__main__":
    app.run()
    