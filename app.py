from flask import Flask, render_template, request
import fetcher 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_trends():
    if request.method == 'POST':
        country = request.form.get('country')
        trends, sectors = fetcher.trendList(country) 
        return render_template('trends.html', trends=trends, sectors=sectors, country=country)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)