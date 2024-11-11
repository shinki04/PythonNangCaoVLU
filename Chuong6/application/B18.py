from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DienTen(FlaskForm):
    ten = StringField('Tên bạn là gì?', validators=[DataRequired()])
    nut_guilenserver = SubmitField('Gửi')

# Lưu ý:  SubmitField sẽ đại diện cho 1 phần tử trong trang web có type = “submit”