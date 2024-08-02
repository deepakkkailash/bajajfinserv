from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='RA2111031010095')

@app.route('/bfhl',methods=['get','post'])
def compute():
    response = dict()
    if(request.method=='GET'):
        response = {
            "statuscode" : 200,
            "operation_code":1
        }
        return json.dumps(response)
    elif(request.method=='POST'):
        value = request.form.get('json')
        options = request.form.getlist('multiple')
        response['success']= True
        response['user_id']='DeepakKailash_Balamurugan_18022004'
        response['rollno']='RA2111031010095'
        value = json.loads(value)

        for i in options:
            if(i=='Alphabets'):
                data = value['data']
                response['Alphabets']= []
                for i in data:
                    if(i.isalpha()):
                        response['Alphabets'].append(i)
            elif(i=='Numbers'):
                data = value['data']
                response['Numbers'] = []
                for i in data:
                    if (i.isdigit()):
                        response['Numbers'].append(i)
            elif(i=='HighestAlphabet'):
                if(not response.get('Alphabets')):
                    response['HighestAlphabet']=[]
                else:
                    response['HighestAlphabet'] = sorted(response['Alphabets'],reverse=True)[0]

        print(value,options)
        return response
if(__name__=='__main__'):
    app.run(debug=True)