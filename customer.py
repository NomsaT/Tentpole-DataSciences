from flask import Flask, redirect, request, render_template, url_for
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      file = request.files['file']
      data=pd.read_excel(file)
       
      plotdata=pd.DataFrame(data)

      # plotdata.plot(kind="bar",figsize=(15, 8))

      plotdata.set_index('Month').plot.bar(figsize=(15,10), fontsize=13)
      plt.get_current_fig_manager().canvas.set_window_title('Customers Income and Expenditure')
      plt.title("Customers Income and Expenditure for the last 12 Months",fontsize=14)
      plt.ylabel("Income/Expenses (R)")      
      plt.show()

      return redirect(url_for("home")) #refreshes the page after the figure is closed
   else:
      return render_template("index.html")

if __name__ == '__main__':
   app.run()