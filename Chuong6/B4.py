from flask import Flask 
ungdung = Flask(__name__) 
@ungdung.route('/') 
def hello(): 
    tentruong = ' Đại Học Văn Lang!' 
    lienket = '<a href="https://www.vanlanguni.edu.vn">' +tentruong+' </a> <br>' 
    chuoi = lienket  
    import datetime 
    nam = datetime.date.today().year 
    chuoi = chuoi + ' <b>Xin <i>chào</i> Tân sinh viên năm ' + str(nam) + '!</b> ' 
    return chuoi 
if __name__ == "__main__": 
    ungdung.run() 