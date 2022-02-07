import ui
import uuid

inputnumber = ''
firstnumber = ''
secodnumber = ''
operation = ''



def numberButtonAction(event_nds):
	global inputnumber
	inputnumber = inputnumber +event_nds.title
	disp.text = convNumber(inputnumber)
	
def operationButtonAction(event):
	global inputnumber,firstnumber,operation
	operation = event.title
	firstnumber = inputnumber
	inputnumber = ''
	
def equalButtonAction(event):
	global firstnumber,secodnumber,inputnumber
	firstnumber = float(firstnumber)
	secodnumber = float(v['label1'].text)
	
	if operation == '+':
		inputnumber = v['label1'].text= convNumber(firstnumber+secodnumber)
		
	if operation == '-':
		inputnumber = v['label1'].text= convNumber(firstnumber-secodnumber)
		
	if operation == '×':
		inputnumber = v['label1'].text= convNumber(firstnumber*secodnumber)
	
	if operation == '÷':
	  inputnumber = v['label1'].text= convNumber(firstnumber/secodnumber)
	  
def acButtonAction(event):
	global inputnumber, firstnumber
	global secodnumber, operation
	inputnumber = ''
	firstnumber = ''
	secodnumber = ''
	operation = ''
	v['label1'].text = '0'
	
def convNumber(no):
	newno = float(no)
	if newno.is_integer():
		  return str(int(newno))
	else: 
		  return str(newno)

def uuidNumber(uu):
	v['label1'].text = uuid.uuid4()
		  
v = ui.load_view()
disp=v['label1']
v.present('sheet')

